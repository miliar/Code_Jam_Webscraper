#include<stdio.h>
#include <algorithm>
#include <cstring>
#include <queue>
#include <cmath>
#include <vector>
#include <iostream>
#include <map>
#include <stdlib.h>
using namespace std;
#define eps 1e-8
#define inf 0x7f7f7f7f
#define LL long long
#define MOD 1000000007
#define MAXN 20
#define MAXK 110
#include <string>
#include <queue>
#include <ctime>
int m, n;

LL  cnt, num;

int judge(LL x)
{
    LL t = x;
    LL tmp = 0;
    while(t)
    {
        tmp = 10 * tmp + t % 10;
        t /= 10;
    }
    if(x == tmp) return 1;
    return 0;
}

//int find(LL x)
//{
//    int l = 0, r = cnt;
//    while(l < r)
//    {
//        int m = l + (r - l) / 2;
//        if(pl[m] >= x) r = m;
//        else l = m + 1;
//    }
//    return l;
//}

int d[1001][1001];
int mxc[1001], mxr[1001];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    num = 0;
    int n, m;
    while(t--)
    {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < m; ++j)
            {
                scanf("%d", &d[i][j]);
            }
        }
        memset(mxc, 0, sizeof(mxc));
        memset(mxr, 0, sizeof(mxr));
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0;j < m; ++j)
            {
                mxr[i] = max(mxr[i], d[i][j]);
            }
        }
        for(int j = 0; j < m; ++j)
        {
            for(int i = 0;i < n; ++i)
            {
                mxc[j] = max(mxc[j], d[i][j]);
            }
        }
        int flg = 0;
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0;j < m; ++j)
            {
                if(mxc[j] != d[i][j] && mxr[i] != d[i][j])
                {
                    flg = 1;
                    break;
                }
            }
            if(flg == 1) break;
        }
        if(flg == 1)
        {
            printf("Case #%d: NO\n", ++cas);
        }
        else
        {
            printf("Case #%d: YES\n", ++cas);
        }
    }
    return 0;
}
