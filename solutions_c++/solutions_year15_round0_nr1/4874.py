#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;

void main()
{
    FILE *infile = fopen("A-large.in", "r");
    FILE *outfile = fopen("A-large.out", "w");

    int n;
    fscanf(infile, "%d", &n);
    
    for (int i = 0; i < n; ++i)
    {
        int topShy;
        fscanf(infile, "%d", &topShy);

        fgetc(infile);
        int curCount = 0;
        int totalCount = 0;
        for (int j = 0; j <= topShy; ++j)
        {
            if (curCount < 0)
            {
                totalCount += (-curCount);
                curCount = 0;
            }
            

            int curShyCount = fgetc(infile) - '0';
            --curCount;
            curCount += curShyCount;
        }
        fprintf(outfile, "Case #%d: %d\n", i + 1, totalCount);
    }

    fclose(infile);
    fclose(outfile);
}
