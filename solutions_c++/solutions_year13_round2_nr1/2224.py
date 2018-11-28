//
//  main.cpp
//  Osmos
//
//  Created by jiusi on 5/5/13.
//  Copyright (c) 2013 jiusi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int s, n;

int ca(int s, int i, int a[]) {
    
    if(i == n)
        return 0;

    if(s <= a[i]) {
        
        if(s == 1) {
            return n;
        }

        int add = 1 + ca(2*s-1, i, a);
        int rem = 1 + ca(s, i+1, a);
        
        return add < rem ? add : rem;
    } else {
        return ca(s+a[i], i+1, a);
    }
        
}



int main(int argc, const char * argv[])
{
//    ifstream in("/Users/jiusi/test.in");
    ifstream in("/Users/jiusi/Downloads/A-small-attempt2.in");
    ofstream out("/Users/jiusi/out.out");
    
    int count;
    in >> count;
    
    for(int c = 0; c < count; c++) {

        in >> s >> n;
        int a[n];
        for(int i=0; i<n; i++) {
            in >> a[i];
        }
        
        sort(a, a+n);
        
        out << "Case #" << c+1 << ": " << ca(s, 0, a) << endl;
    }
    
}

