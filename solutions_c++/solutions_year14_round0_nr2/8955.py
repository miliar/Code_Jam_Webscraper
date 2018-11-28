#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

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
        double C, F, X;
        double t, t1, t2;
        double rate;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr2);
        C = atof(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        F = atof(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        X = atof(subtoken);

        // initial vals
        t = 0;
        rate = 2;

        if (X <= C)
        {
            // done
            t = X/rate;
        }
        else
        {
            t += C/rate;
            t1 = (X-C)/rate;
            t2 = X/(rate+F);
            while (t1 > t2)
            {
                rate += F;
                t += C/rate;
                t1 = (X-C)/rate;
                t2 = X/(rate+F);
            }
            t += t1;
        }

        printf("Case #%d: ", i+1);
        printf("%0.7f\n", t);
    }


    fclose(fp);
    return 0;
}
