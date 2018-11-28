#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

long long list[1000] = {1,4,9,121,484};
int dromes = 5;


bool checkdrome(long long num)
{
    int i;
    /* exceeds 10^14 limit */
    if ((num / 100000000000000) >= 1)
        return false;

    int digits[14];
    int digcount=0;

    for (i=0; num > 0 && i<14; i++)
    {
        digits[i] = num % 10;
        num = num / 10;
        digcount++;
    }

    for (i=0; i<digcount/2; i++)
    {
//        printf("comparing dig %d and %d:\n",digits[i],digits[digcount-i-1]);
        if (digits[i] != digits[digcount-i-1])
        {
            return false;
        }
    }
    return true;
}

void gendromes(void)
{
    long long genlist[] = {
        101,111,121,202,212,222,
        1001,1111,1221,2002,2112,2222,
        10001,10101,10201,11011,11111,11211,12021,12121,12221,20002,20102,20202,21012,21112,21212,22022,22122,22222,
        100001,101101,102201,110011,111111,112211,120021,121121,122221,200002,201102,202202,210012,211112,212212,220022,221122,222222,
        1000001,1001001,1002001,1010101,1011101,1012101,1020201,1021201,1022201,
        1100011,1101011,1102011,1110111,1111111,1112111,1120211,1121211,1122211,
        1200021,1201021,1202021,1210121,1211121,1212121,1220221,1221221,1222221,
        2000002,2001002,2002002,2010102,2011102,2012102,2020202,2021202,2022202,
        2100012,2101012,2102012,2110112,2111112,2112112,2120212,2121212,2122212,
        2200022,2201022,2202022,2210122,2211122,2212122,2220222,2221222,2222222};
    long long gen;
    long long gensq;
    int i;

    for (i=0; i<102; i++)
    {
        gensq = genlist[i] * genlist[i];

        if (checkdrome(gensq))
        {
            list[dromes++] = gensq;
//            printf("found %d: %lld\n", dromes, gensq);
            if (dromes == 1000)
            {
                printf("FULL!\n");
                return;
            }
        }
    }
}
int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    long long A, B;
    int i, j, k;
    int num;

    gendromes();
//    printf("%d dromes found\n", dromes);
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
        A = atoll(subtoken);

        subtoken = strtok_r(NULL, " ", &sptr2);
        B = atoll(subtoken);

        num = 0;
        for (j=0; j<dromes; j++)
        {
            if (A <= list[j] && list[j] <= B) num++;
        }

        printf("Case #%d: %d\n", i+1, num);
    }


    fclose(fp);
    return 0;
}
