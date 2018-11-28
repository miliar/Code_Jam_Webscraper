#!/bin/python

V = set(['a','e','i','o','u'])
N = int(raw_input())

def get_substrings(name):
    l = len(name)
    for i in xrange(l+1):
        for j in xrange(i+1, l+1):
            yield name[i:j]

for x in range(N):
    name, n = raw_input().split()
    n = int(n)
    name = name.lower()
    l = len(name)
    n_val = 0
    for sub in get_substrings(name):
        if len(sub) < n:
            continue
        sub_l = len(sub)
        #print sub, sub_l-n+1
        for i in xrange(sub_l-n+1):
            sub_n = sub[i:i+n]
            #print "   ", sub_n
            if all(map(lambda x: not x in V, sub_n)):
                n_val += 1
                break
            
    print "Case #%d: %d" % (x+1, n_val)
