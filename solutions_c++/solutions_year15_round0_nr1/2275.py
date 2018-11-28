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

char inp[1010];
int qs[1010];

int main()
{
    int T,n,i,r;

    scanf("%d",&T);

    BL
    {
        scanf("%d%s",&n,inp);

        qs[0] = inp[0] - '0';

        for(i = 1; i <= n; i++)
        {
            qs[i] = inp[i] - '0' + qs[i - 1];
        }

        r = 0;

        for(i = 1; i <= n; i++)
        {
            if(i > qs[i - 1])
            {
                r = max(r,i - qs[i - 1]);
            }
        }

        printf("Case #%d: %d\n",K,r);
    }
}

