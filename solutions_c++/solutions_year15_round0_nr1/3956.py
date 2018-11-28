//
//  main.cpp
//  codejam_standing_ovation
//
//  Created by Alexandru Andronache on 11/04/15.
//  Copyright (c) 2015 Alexandru Andronache. All rights reserved.
//

#include <iostream>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

const int MAX = 2000;

int T, N;
char sir[MAX];


int main(int argc, const char * argv[])
{
    fscanf(f, "%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        fscanf(f, "%d ", &N);
        fgets(sir, N + 2, f);
        
        int current = sir[0] - '0', needed = 0;
        
        for (int i = 1; i <= N; ++i)
        {
            if (sir[i] != '0')
            {
                if (i > current)
                {
                    needed = needed + i - current;
                    current = current + sir[i] - '0' + i - current;
                }
                else
                {
                    current = current + sir[i] - '0';
                }
            }
        }
        
        fprintf(g, "Case #%d: %d\n", t, needed);
    }
    
    return 0;
}
