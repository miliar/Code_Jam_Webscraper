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

string A[1010], B[1010];
set<string> S1, S2;

int c0b(int x, int n)
{
    int res = 0;

    for(int i = 0; i < n; i++)
    {
        if((x & (1 << i)) == 0)
        {
            res++;
        }
    }

    return res;
}

int cal(int n)
{
    int res = 0, i, j;

    for(i = 0; i < (1 << n); i++)
    {
        S1.clear();
        S2.clear();

        for(j = 0; j < n; j++)
        {
            if(i & (1 << j))
            {
                S1.I(A[j]);
                S2.I(B[j]);
            }
        }

        for(j = 0; j < n; j++)
        {
            if((i & (1 << j)) == 0)
            {
                if(S1.find(A[j]) == S1.end() || S2.find(B[j]) == S2.end())
                {
                    break;
                }
            }
        }

        if(j == n)
        {
            res = max(res, c0b(i, n));
        }
    }

    return res;
}

int main()
{
    int T, n, i;

    scanf("%d", &T);

    BL
    {
        scanf("%d", &n);

        for(i = 0; i < n; i++)
        {
            cin >> A[i] >> B[i];
        }

        printf("Case #%d: %d\n",K, cal(n));
    }
}
