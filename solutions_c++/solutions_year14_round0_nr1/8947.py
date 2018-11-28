#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

int getbits(FILE *fp)
{
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int i, j, k, row;
    int retval = 0;

    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    row = atoi(token);

    for (i=0; i<4; i++)
    {
        fgets(strBuf, BUFSZ, fp);
        if ((i+1) == row) // match
        {
            // parse the row
            token = strtok_r(strBuf, "\r\n", &sptr1);

            for (j=0; j<4; j++)
            {
                subtoken = strtok_r((j==0)?token:NULL, " ", &sptr2);
                k = atoi(subtoken);
//                printf("k=%d\n", k);
                retval += (1 << (k-1));
            }
        }
    }
//    printf("Retval = %04x\n", retval);
    return retval;
}

int samebit(int a, int b)
{
    int i, num=0;

    for (i=0; i<16; i++)
    {
        if ((a & b) & (1 << i))
        {
            if (num == 0)
            {
                num = i+1;
//                printf("num found @%d\n", num);
            }
            else
            {
                num = 0;
//                printf("toast! @%d\n", i+1);
                break;
            }
        }
    }
//    printf("num=%d\n", num);
    return num;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1;
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
        int val1, val2;

        val1 = getbits(fp);
        val2 = getbits(fp);

        printf("Case #%d: ", i+1);
        if ((val1 & val2) == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            val1 = samebit(val1, val2);
            if (val1 == 0)
            {
                printf("Bad magician!\n");
            }
            else
            {
                printf("%d\n", val1);
            }
        }
    }

    fclose(fp);
    return 0;
}
