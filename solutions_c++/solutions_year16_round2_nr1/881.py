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

int cnt[300];
char str[2010];
int n[10];

int main()
{
    int T, i, j;

    scanf("%d", &T);

    BL
    {
        scanf("%s", str);

        for(i = 0; i < 10; i++)
        {
            n[i] = 0;
        }

        for(i = 0; i < 300; i++)
        {
            cnt[i] = 0;
        }

        for(i = 0; str[i] != 0; i++)
        {
            cnt[str[i]]++;
        }

        n[0] = cnt['Z'];

        cnt['Z'] -= n[0];
        cnt['E'] -= n[0];
        cnt['R'] -= n[0];
        cnt['O'] -= n[0];


        n[2] = cnt['W'];

        cnt['T'] -= n[2];
        cnt['W'] -= n[2];
        cnt['O'] -= n[2];

        n[4] = cnt['U'];

        cnt['F'] -= n[4];
        cnt['O'] -= n[4];
        cnt['U'] -= n[4];
        cnt['R'] -= n[4];

        n[5] = cnt['F'];

        cnt['F'] -= n[5];
        cnt['I'] -= n[5];
        cnt['V'] -= n[5];
        cnt['E'] -= n[5];

        n[6] = cnt['X'];

        cnt['S'] -= n[6];
        cnt['I'] -= n[6];
        cnt['X'] -= n[6];

        n[7] = cnt['V'];

        cnt['S'] -= n[7];
        cnt['E'] -= n[7];
        cnt['V'] -= n[7];
        cnt['E'] -= n[7];
        cnt['N'] -= n[7];

        n[8] = cnt['G'];

        cnt['E'] -= n[8];
        cnt['I'] -= n[8];
        cnt['G'] -= n[8];
        cnt['H'] -= n[8];
        cnt['T'] -= n[8];

        n[1] = cnt['O'];

        cnt['O'] -= n[1];
        cnt['N'] -= n[1];
        cnt['E'] -= n[1];

        n[9] = cnt['I'];

        cnt['N'] -= n[9];
        cnt['I'] -= n[9];
        cnt['N'] -= n[9];
        cnt['E'] -= n[9];

        n[3] = cnt['T'];

        printf("Case #%d: ", K);

        for(i = 0; i < 10; i++)
        {
            for(j = 0; j < n[i]; j++)
            {
                printf("%d", i);
            }
        }

        printf("\n");
     }
}
