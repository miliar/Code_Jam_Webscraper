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

int inp[1010],cal[1010];

int main()
{
    int T,d,i,j,x;

    scanf("%d",&T);

    BL
    {
        scanf("%d",&d);

        for(i = 0; i < d; i++)
        {
            scanf("%d",inp + i);
        }

        for(i = 1; i <= 1000; i++)
        {
            cal[i] = 0;

            for(j = 0; j < d; j++)
            {
                if(inp[j] > i)
                {
                    cal[i] += (inp[j] + i - 1) / i - 1;
                }
            }
        }

        x = INF;

        for(i = 1; i <= 1000; i++)
        {
            x = min(x,cal[i] + i);
        }

        printf("Case #%d: %d\n",K,x);
    }
}

