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
        int count=0;
        int len;
        char curchar;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        len = strlen(token);
        curchar = token[0];

        // Count the number of sign changes
        for (j=1; j<len; j++)
        {
            if (curchar != token[j])
            {
                curchar = token[j];
                count++;
            }
        }
        if (curchar == '-') count++;

        printf("Case #%d: %d\n", i+1, count);
    }


    fclose(fp);
    return 0;
}
