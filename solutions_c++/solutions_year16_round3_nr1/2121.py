//
//  a.cpp
//  CodeJam16
//
//  Created by Ahmed Mohammed on 5/8/16.
//  Copyright © 2016 Akhmed. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
#include <cassert>

#include <gmp.h>

using namespace std;


typedef uint32_t u32;
typedef uint64_t u64;

int cmp(pair<int, int> &l, pair<int, int> &r) { return l.second > r.second; }

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
        cout << "Case #" << (tcase + 1) << endl;
        fout << "Case #" << (tcase + 1) << ": ";
        
        int N; fin >> N;
        vector<pair<int, int>> P(N);
        int tot = 0;
        for (int i = 0; i < N; i++) { int p; fin >> p; P[i].first = i; P[i].second = p; tot += p; }
        
        while (tot > 2)
        {
            sort(P.begin(), P.end(), cmp);
            
            fout << (char)('A' + P[0].first);
            
            if ((P[1].second == P[0].second) && (tot > 3))
            {
                fout << (char)('A' + P[1].first);
                P[1].second--;
                tot--;
            }
            
            P[0].second--;
            tot--;
            
            fout << ' ';
        }
        
        for (int i = 0; i < N; i++)
            if (P[i].second) fout << (char)('A' + P[i].first);
        
        fout << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}