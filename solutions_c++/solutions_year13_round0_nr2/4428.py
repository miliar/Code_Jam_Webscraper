/*
 * Author:heroming
 * File:Lawnmower.cpp
 * Time:2013/4/13 13:25:21
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair

#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))
#define SZ(v) ((int)(v).size())
#define FOR(it,a) for (__typeof((a).begin()) it=(a).begin();it!=(a).end();++it)

typedef long long lint;
typedef unsigned long long ulint;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

const int maxn = 110;

int t, n, m, w[maxn][maxn];

bool valid(const int x, const int y)
{
        int s = 2;
        for (int i = 1; i <= n; ++ i)
                if (w[x][y] < w[i][y])
                {
                        -- s;
                        break;
                }
        for (int i = 1; i <= m; ++ i)
                if (w[x][y] < w[x][i])
                {
                        -- s;
                        break;
                }
        return s;
}

bool solve()
{
        for (int i = 1; i <= n; ++ i)
                for (int j = 1; j <= m; ++ j)
                        if (! valid(i, j))
                              return 0;  
        return 1;
}

int main()
{
        freopen("data.out", "w", stdout);
        scanf("%d", &t);
        for (int l = 1; l <= t; ++ l)
        {
                scanf("%d%d", &n, &m);
                for (int i = 1; i <= n; ++ i)
                        for (int j = 1; j <= m; ++ j)
                                scanf("%d", &w[i][j]);
                if (solve())
                        printf("Case #%d: YES\n", l);
                else
                        printf("Case #%d: NO\n", l);
        }
        return 0;
}
