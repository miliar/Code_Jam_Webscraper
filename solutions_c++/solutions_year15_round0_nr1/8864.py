//
//  main.cpp
//  Jam
//
//  Created by Irina Korneeva on 11/04/15.
//  Copyright (c) 2015 Irina Korneeva. All rights reserved.
//
#include <cstdio>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


using namespace std;
int main()
{
    int n;
   
    FILE * f, *f1;
    f = fopen("SInputFile2.txt", "r");
    f1 = fopen("SInputFile1.txt", "w");
    char x;
    
    char s[10000];
   
    fgets(s, 10000, f);
    n = atoi(s);
    //cout << n;
    for(int i = 0; i < n; i++)
    {
        int sum = 0;
        int ans = 0;
        fscanf(f, "%s", s);
        int p = atoi(s);
        
        
        x = fgetc(f);
        
        
        for(int j = 0; j < p + 1; j++)
        {
            x = fgetc(f);
            //cout << x;
            
            int r = x - '0';
            if(!j)
            {
                sum = r;
            }
            else
            {
                if(r)
                {
                    if(sum >= j)
                    {
                        sum = sum + r;
                    }
                    else
                    {
                        ans = ans + j - sum;
                        sum = j;
                        sum = sum + r;
                    }
                }
                
            }
            
        }
        //cout << ans << endl;
        
        fprintf(f1, "Case #%d: %d\n", i + 1, ans);
        
        
    }
    fclose(f);
    fclose(f1);
}