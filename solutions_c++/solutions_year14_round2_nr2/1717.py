//
//  main.cpp
//  Magic Trick
//
//  Created by Alexandru Andronache on 9/1/13.
//  Copyright (c) 2013 Alexandru Andronache. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T, A, B, K;

long long rez = 0;

int main()
{
    fscanf(f, "%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        rez = 0;
        fscanf(f, "%d %d %d\n", &A, &B, &K);
        for (int i = 0; i < A; ++i)
        {
            for (int j = 0; j < B; ++j)
            {
                //if (i != j)
                {
                    if ((i & j) < K)
                    {
                        rez++;
                    }
                }
            }
        }
        
        fprintf(g, "Case #%d: %lld\n", t, rez);
    }
    
    fclose(f);
    fclose(g);
}


