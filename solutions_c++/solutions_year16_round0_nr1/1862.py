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

int arr[10];

int main()
{
    int T, n, i, j, x;

    scanf("%d",&T);

    BL
    {
        scanf("%d",&n);

        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", K);
            continue;
        }

        for(i = 0; i < 10; i++)
        {
            arr[i] = 0;
        }

        for(i = 1; i < 100; i++)
        {
            x = i * n;

            while(x != 0)
            {
                arr[x % 10] = 1;
                x /= 10;
            }

            for(j = 0; j < 10; j++)
            {
                if(arr[j] != 1)
                {
                    break;
                }
            }

            if(j == 10)
            {
                break;
            }
        }

        if(i == 100)
        {
            printf("Case #%d: INSOMNIA\n", K);
            return 0;
        } else {
            printf("Case #%d: %d\n", K, i * n);
        }
    }
}
