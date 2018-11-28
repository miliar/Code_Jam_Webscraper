//
//  a.cpp
//  CodeJam16
//
//  Created by Ahmed Mohammed on 4/30/16.
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


static string names[] =
{
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};


bool solve(int* counts, int tcount, string& result)
{
    if (!tcount) return true;
    
    for (int i = 0; i <= 9; i++)
    {
        int const tc = tcount - (int)names[i].length();
        if (tc < 0) continue;
        
        bool fail = false;
        for (char const *ch = names[i].data(); *ch; ch++) { counts[(*ch)-'A']--; if (counts[(*ch)-'A'] < 0) fail = true; }
        if (false == fail)
        {
            result.push_back('0' + i);
            if (solve(counts, tc, result)) return true;
            result.pop_back();
        }
        for (char const *ch = names[i].data(); *ch; ch++) counts[(*ch)-'A']++;
    }
    
    return false;
}

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
        fout << "Case #" << (tcase + 1) << ": ";
        
        string S; fin >> S;
        
        int counts[26];
        memset(counts, 0, sizeof(counts));
        for (int i = 0; i < S.length(); i++) counts[S[i]-'A']++;
        
        string ans;
        assert(solve(counts, (int)S.length(), ans));
        
        fout << ans << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}