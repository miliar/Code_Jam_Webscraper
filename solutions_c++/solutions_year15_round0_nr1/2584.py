//
//  a.cpp
//  CodeJam15
//
//  Created by Ahmed Mohammed on 4/11/15.
//

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
    
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open()) { printf("Unable to open input file\n"); exit(1);}
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open()) { printf("Unable to open output file\n"); exit(1);}
    fout.seekp(0);
    
    fout.precision(7);
    fout.setf(ios::fixed);
    
    
    // solve cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        int sm = 0;     // Smax
        fin >> sm;
        
        int s[sm+1];
        for (int i = 0; i <= sm; i++) { char h; fin >> h; s[i] = h - '0';}
        
        int a = 0;
        int c = 0;
        for (int i = 0; i <= sm; i++)
        {
            if (c < i)
            {
                a += i - c;
                c = i;
            }
            
            c += s[i];
        }
        
        fout << "Case #" << (tcase + 1) << ": " << a << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}

