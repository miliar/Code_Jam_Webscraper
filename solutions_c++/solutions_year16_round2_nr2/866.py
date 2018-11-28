/**************************************************
    WhatTheFua
    Anan Schuett
    arnan_s@msn.com
**************************************************/

#define BK back()
#define BL for(int K = 1; K <= T; K++)
#define F first
#define INF 2147483647LL
#define LNF 8000000000000000000LL
#define P107 1000000007LL
#define P109 1000000009LL
#define PB push_back
#define PF push_front
#define I insert
#define E erase
#define S second
#define SZ size()
#define IT iterator
#define db double
#define ll long long int
#define mp make_pair

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

char C[20], J[20];

bool fit(int x, int l, char* S)
{
    char tmp[5];

    for(int i = l - 1; i >= 0; i--)
    {
        tmp[i] = (x % 10) + '0';
        x /= 10;
    }

    tmp[l] = '\0';

    for(int i = 0; i < l; i++)
    {
        if((tmp[i] != S[i]) && (S[i] != '?'))
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int T, Cf, Jf, i, j, B, M;

    scanf("%d", &T);

    BL
    {
        scanf("%s%s", C, J);

        M = 1;

        for(i = 0; i < strlen(C); i++)
        {
            M *= 10;
        }

        B = INF;

        for(i = 0; i < M; i++)
        {
            for(j = 0; j < M; j++)
            {
                if(fit(i, strlen(C), C) && fit(j, strlen(C), J))
                {
                    if(abs(i - j) < B)
                    {
                        B = abs(i - j);
                        Cf = i;
                        Jf = j;
                    }
                }
            }
        }

        if(strlen(C) == 1)
        {
            printf("Case #%d: %01d %01d\n", K, Cf, Jf);
        } else if(strlen(C) == 2) {
            printf("Case #%d: %02d %02d\n", K, Cf, Jf);
        } else if(strlen(C) == 3) {
            printf("Case #%d: %03d %03d\n", K, Cf, Jf);
        }
    }
}
