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
    int i, j, k, l;

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
        int Smax;
        int total = 0;
        int invite = 0;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr2);
        Smax = atoi(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        for (j=0; j<Smax+1; j++)
        {
            /* k is the number of people of shyness j */
            k = subtoken[j] - '0';
            //printf("%d people of shyness %d, ", k, j);
            if (total < j)
            {
                //printf("but total only %d\n", total);
                invite += j - total;
                //printf("have to invite %d more!\n", j-total);
                total = j;
            }
            else
            {
                //printf("total of %d is ok\n", total);
            }
            total += k;
            //printf("==>total now %d\n", total);
        }

        printf("Case #%d: %d\n", i+1, invite);
    }

    fclose(fp);
    return 0;
}
