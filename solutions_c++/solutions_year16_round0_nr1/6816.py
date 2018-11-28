#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000
#define MYCAP 1000

//#define TEST


int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int i, j, k, l;
#ifdef TEST
    int maxloops = 0;
    int maxbasenum;
#endif

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

#ifdef TEST
for (i=0; i<=1000000; i++)
#else
    for (i=0; i<T; i++)
#endif
    {
        int foundarray = 0;
        int basenum;
        int currnum;
        int tempnum;

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        basenum = atoi(token);
#ifdef TEST
basenum=i;
#endif

        if (basenum == 0)
        {
#ifdef TEST
            printf("Case #%d: INSOMNIA\n", basenum);
#else
            printf("Case #%d: INSOMNIA\n", i+1);
#endif
            continue;
        }

        for (j=0; j<MYCAP; j++)
        {
            tempnum = currnum = basenum * (j+1);
            while (tempnum / 10)
            {
                foundarray |= (1 << (tempnum%10));
                tempnum /= 10;
            }
            foundarray |= (1 << (tempnum));
            if (foundarray == 0x3ff)
            {
#ifdef TEST
                if (j+1 > maxloops)
                {
                    maxloops = j+1;
                    maxbasenum = basenum;
                }
#endif
                break;
            }
        }

#ifdef TEST
        printf("Case #%d: %d\t[%d]\n", basenum, currnum, j);
#else
        printf("Case #%d: %d\n", i+1, currnum);
#endif
    }
#ifdef TEST
    printf("Hit maxloops of %d at %d\n", maxloops, maxbasenum);
#endif

    fclose(fp);
    return 0;
}
