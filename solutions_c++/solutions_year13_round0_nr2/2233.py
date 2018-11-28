#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

bool checkgoodheight(int *a, int row, int col, int height, int width)
{
    /* good if either others in row/col have lower height */
    int target = a[row*100+col];
    int i;

    for (i=0; i<height; i++)
    {
        if (target < a[i*100+col])
        {
            /* fail! try other */
            break;
        }
    }
    if (i == height) return true;

    for (i=0; i<width; i++)
    {
        if (target < a[row*100+i])
        {
            return false;
        }
    }
    return true;
}
int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int N, M;
    int a[10000];
    int i, j, k;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr2);
        N = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        M = atoi(subtoken);

        for (j=0; j<N; j++)
        {
            fgets(strBuf, BUFSZ, fp);
            token = strtok_r(strBuf, "\r\n", &sptr1);
            for (k=0; k<M; k++)
            {
                if (k==0)
                {
                    subtoken = strtok_r(token, " ", &sptr2);
                }
                else
                {
                    subtoken = strtok_r(NULL, " ", &sptr2);
                }
                a[j*100+k] = atoi(subtoken);
            }
        }
        /* everything in the col or row must be either my height or lower */

        int YES = 1;
        for (j=0; j<N && YES == 1; j++)
        {
            for (k=0; k<M; k++)
            {
                if (!checkgoodheight(a,j,k,N,M))
                {
                    YES = 0;
                    break;
                }
            }
        }

        printf("Case #%d: ", i+1);
        if (YES == 1) printf("YES\n");
        else printf("NO\n");
    }


    fclose(fp);
    return 0;
}
