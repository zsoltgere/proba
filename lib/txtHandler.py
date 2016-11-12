#  -*- coding: utf-8 -*-
from lib.xmlBasedHandler import XmlBasedHandler


class TxtHandler(XmlBasedHandler):

    EXTENSION=".txt"
    SEPARATOR = '\n'

    def __init__(self,path):
        super(TxtHandler,self).__init__(path)

        self.open_file()

    def open_file(self):
        with open(self.path,'r') as txt_file:

            temp = ""
            separator_line_counter=0

            for line in txt_file:
                #if a line equal to the separator
                if line == self.SEPARATOR:
                    #increment separator counter by 1
                    separator_line_counter+=1
                    # if the temp str is not empty (if it's empty that means the previous line was the end of a paragraph)
                    if temp != "":
                        # append the paragraph to the list
                        self.paragraph_list.append(temp)
                        # reset the temp -> end of the paragraph
                        temp=""

                    # if the current line is the second separator line in a row, it could be == 2 too
                    if separator_line_counter % 2 == 0:
                        # append the separator to the paragraph list
                        self.paragraph_list.append(self.SEPARATOR)
                        # reset the counter
                        separator_line_counter=0
                        # reset the temp -> end of the paragraph
                        temp=""
                # if the line not equal to the separator
                else:
                    # append it to the temp
                    temp+=line
                    # reset the separator counter
                    separator_line_counter=0
            # after the last line, check there is no text in the temp
            if temp !="":
                # if there is, add it to the list
                self.paragraph_list.append(temp)

        self.para=self.paragraph_list

    def update(self,list):

        if not list:
            return
        if len(list) != len(self.paragraph_list):
            print ("Incorrect list length")
            return

        self.para=list

    def print(self):
        for i in self.paragraph_list:
            print(i)
            print(self.SEPARATOR)

    def save(self,name):
        with open(name+self.EXTENSION,'w') as file:
            # store the number of paragraphs
            ln=len(self.para)
            # iterate through the paragraphs
            for i in range(ln):
                # write i. paragraph
                file.write(self.para[i])
                # if i is not the last paragraph
                if i != ln-1:
                    # write predefined separator line between two paragraphs
                    file.write(self.SEPARATOR)