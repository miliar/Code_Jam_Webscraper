//
//  main.cpp
//  Osmos
//
//  Created by Ahmed Mohammed Abdurahman on 5/4/13.
//  Copyright (c) 2013 Better MDM LLC. All rights reserved.
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
    if (argc < 3)
    {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        exit(1);
    }
    
    // open files
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open())
    {
        printf("Unable to open input file\n");
        exit(1);
    }
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open())
    {
        printf("Unable to open output file\n");
        exit(1);
    }
    fout.seekp(0);
    
    
    
    // solve test cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        int64_t a, n;
        fin >> a >> n;
        
        vector<int64_t> m(n);
        for (int64_t i = 0; i < n; i++) fin >> m[i];
        
        int64_t steps = 0;
        if (a < 2) steps = n;
        else
        {
            sort(m.begin(), m.end());
            
            int64_t requiredSteps[n];
            
            for (int64_t i = 0; i < n; i++)
            {
                requiredSteps[i] = 0;
                if (m[i] >= a)
                {
                    requiredSteps[i] = ceil( ((double)m[i]) / (a - 1) );
                    int b = 31;
                    for (; b; b--) if (requiredSteps[i] & (1L << b)) break;
                    if (requiredSteps[i] == (1L << b)) requiredSteps[i] = b;
                    else requiredSteps[i] = b + 1;
                    
                    a = (1 << requiredSteps[i]) * (a - 1) + 1;
                }
                
                a += m[i];
            }
            
//            if (true)//tcase == 6)
//            {
//                printf("\n\nCase %lld\n", tcase + 1);
//                for (int64_t i = 0; i < n; i++)
//                {
//                    printf("%lld ", m[i]);
//                }
//                printf("\n");
//                for (int64_t i = 0; i < n; i++)
//                {
//                    printf("%lld ", requiredSteps[i]);
//                }
//            }
            
            int64_t i = n - 1, ri = n, c = 0;
            for (; i >= 0; i--)
            {
                if ((requiredSteps[i] + c) < (n - i))
                {       // include
                    c += requiredSteps[i];
                }
                else
                {       // remove
                    ri = i;
                    c = 0;
                }
            }
            
            for (int64_t i = 0; i < ri; i++) steps += requiredSteps[i];
            steps += (n - ri);
        }
        
        fout << "Case #" << (tcase + 1) << ": " << steps << endl;
    }
    
    
    
    fin.close();
    fout.close();
    
    return 0;
}
