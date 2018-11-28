//
//  main.cpp
//  Round_1C_2014
//
//  Created by Ahmed Mohammed Abdurahman on 5/11/14.
//  Copyright (c) 2014 Better LLC. All rights reserved.
//

#include <iostream>


#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;




int main(int argc, const char * argv[])
{
    if (argc < 3) { printf("Usage: %s <input file> <output file>\n", argv[0]); exit(1);}
    
    // open files
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open()) { printf("Unable to open input file\n"); exit(1);}
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open()) { printf("Unable to open output file\n"); exit(1);}
    fout.seekp(0);
    
    fout.precision(7);
    fout.setf(ios::fixed);
    
    
    // solve test cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        cout << "Case #" << (tcase + 1) << ": ";
        fout << "Case #" << (tcase + 1) << ": ";
        
        uint64_t p;
        uint64_t q;
        
        char c;
        fin >> p; fin >> c; fin >> q;
        
        p *= (1LL << 40);
        uint64_t f = p / q;
        
        if ((f * q) < p)
        {
            cout << "impossible" << endl;
            fout << "impossible" << endl;
            continue;
        }
        
        p = f;
        int g = 41;
        while (p)
        {
            p = p >> 1;
            g--;
        }
        
        if (g == 41)
        {
            cout << "impossible" << endl;
            fout << "impossible" << endl;
            continue;
        }
        
        cout << g << endl;
        fout << g << endl;
        
    }
    
    return 0;
}

