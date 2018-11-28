//
//  main.cpp
//  Round_1B_2014
//
//  Created by Ahmed Mohammed Abdurahman on 5/3/14.
//  Copyright (c) 2014 Better LLC. All rights reserved.
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


char s[200][101];
int lens[200];

struct Ci
{
    char ch;
    int counts[200];
    int minCount;
    int maxCount;
};
typedef struct Ci Ci;

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
        
        int N; fin >> N;
        for (int i = 0; i < N; i++)
        {
            fin >> s[i];
            lens[i] = (int)strlen(s[i]);
        }
        
        vector<Ci> v;
        Ci c0;
        c0.ch = s[0][0];
        c0.counts[0] = 1;
        c0.minCount = 1;
        c0.maxCount = 1;
        v.push_back(c0);
        
        char ch = c0.ch;
        for (int i = 1; i < lens[0]; i++)
        {
            if (s[0][i] == ch)
            {
                Ci *c = &v.back();
                c->counts[0]++;
                c->minCount++;
                c->maxCount++;
            }
            else
            {
                Ci ci;
                ci.ch = s[0][i];
                ci.counts[0] = 1;
                ci.minCount = 1;
                ci.maxCount = 1;
                v.push_back(ci);
                
                ch = ci.ch;
            }
        }
        
        bool possible = true;
        
        
        for (int i = 1; i < N; i++)
        {
            int vi = 0;
            Ci *c = &v[vi];
            c->counts[i] = 0;
            for (int j = 0; j < lens[i]; j++)
            {
                if (s[i][j] == c->ch) c->counts[i]++;
                else
                {
                    if (c->counts[i])
                    {
                        vi++;
                        
                        if (vi < v.size())
                        {
                            if (c->minCount > c->counts[i]) c->minCount = c->counts[i];
                            else if (c->maxCount < c->counts[i]) c->maxCount = c->counts[i];
                            
                            c = &v[vi];
                            c->counts[i] = 0;
                            j--;
                            continue;
                        }
                    }
                    
                    possible = false;
                    goto Done;
                }
            }
            
            if (vi != v.size() - 1)
            {
                possible = false;
                goto Done;
            }
            
            if (c->minCount > c->counts[i]) c->minCount = c->counts[i];
            else if (c->maxCount < c->counts[i]) c->maxCount = c->counts[i];
        }
        
        
    Done:
        if (possible)
        {
//            uint64_t count = 0;
//            
//            for (int i = 0; i < v.size(); i++)
//            {
//                uint64_t cc = 101;
//                
//                for (int j = v[i].minCount; j <= v[i].maxCount; j++)
//                {
//                    uint64_t steps = 0;
//                    for (int k = 0; k < N; k++) steps += abs(v[i].counts[k] - j);
//                    if (cc > steps) cc = steps;
//                }
//                
//                count += cc;
//            }
//            
//            cout << count << endl;
//            fout << count << endl;
            
            uint64_t count = 0;
            for (int i = 0; i < v.size(); i++)
            {
                count += abs(v[i].counts[0] - v[i].counts[1]);
                if (count > 100)
                {
                    
                }
            }
            
            
            cout << count << endl;
            fout << count << endl;
        }
        else
        {
            cout << "Fegla Won" << endl;
            fout << "Fegla Won" << endl;
        }
        
    }
    
    return 0;
}

