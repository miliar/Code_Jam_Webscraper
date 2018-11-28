//
//  main.cpp
//  Lawnmower
//
//  Created by Ahmed Mohammed Abdurahman on 4/13/13.
//  Copyright (c) 2013 Better MDM LLC. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>

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
    
    
    
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {           // process each test case
        int n, m;
        fin >> n >> m;
        
        int lawn[n][m];
        int rowMax[n], colMax[m];
        
        // read
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                fin >> lawn[i][j];
        
        // determine row maximums
        for (int i = 0; i < n; i++)
        {
            rowMax[i] = 0;
            for (int j = 0; j < m; j++)
                if (lawn[i][j] > rowMax[i]) rowMax[i] = lawn[i][j];
        }
        
        // determine column maximums
        for (int j = 0; j < m; j++)
        {
            colMax[j] = 0;
            for (int i = 0; i < n; i++)
                if (lawn[i][j] > colMax[j]) colMax[j] = lawn[i][j];
        }
        
        
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if ((lawn[i][j] < rowMax[i]) && (lawn[i][j] < colMax[j]))
                {
                    fout << "Case #" << (tcase + 1) << ": NO" << endl;
                    goto case_done;
                }
        
        fout << "Case #" << (tcase + 1) << ": YES" << endl;

    case_done:;
        
        
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}