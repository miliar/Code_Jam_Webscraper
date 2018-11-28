#!/usr/bin/env python2
#Author Phinfinity <rndanish@gmail.com>


def ispal(n):
    n = str(n)
    return n[::-1] == n


pal_list = []
i = 1
while True:
    if (ispal(i) and ispal(i*i)):
        print "%d (%d)"%(i*i,i)
    i = i+1
