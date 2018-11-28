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

char str[20];

ll pow(int x, int b)
{
    ll res = 1LL;

    for(int i = 0; i < b; i++)
    {
        res *= (ll)x;
    }

    return res;
}

int main()
{
    printf("Case #1:\n");

    for(int i = 0; i < 500; i++)
    {
        int x = i;

        for(int j = 13; j >= 0; j--)
        {
            str[j] = (x % 2) + '0';
            x /= 2;
        }

        str[14] = '\0';

        printf("1%s11%s1", str, str);

        for(int j = 2; j <= 10; j++)
        {
            printf(" %lld", pow(j, 16) + 1);
        }

        printf("\n");
    }
}
