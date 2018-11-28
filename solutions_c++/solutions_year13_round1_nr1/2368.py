//
//  main.cpp
//  GOOGLE_1A_A
//
//  Created by Cheng Wayne on 4/27/13.
//  Copyright (c) 2013 Stooge. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("/Users/chengwayne/Downloads/A-small-attempt1.in.txt");
    ofstream fout("/Users/chengwayne/Downloads/out.txt");
    
    int T;
    fin >>T;
    for (int i = 1; i <= T; i++) {
        long long r, t;
        fin >>r >>t;
        long count = 0;
        
        while (t >= r + r + 1) {
            count++;
            t -= r + r + 1;
            r += 2;
        }
        
        fout <<"Case #" <<i <<": " <<count <<endl;
    }
    return 0;
}

