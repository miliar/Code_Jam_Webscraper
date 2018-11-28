#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3f3f3f3f
#define LL long long
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}
const int N = 105;
int n, m, h[N][N];
int row[N], col[N];
int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B.out", "w", stdout);
    int t, cas = 1, i, j;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &m);
        for(i = 1; i <= n; i++)
        {
            row[i] = 0;
            for(j = 1; j <= m; j++)
            {
                scanf("%d", &h[i][j]);
                checkMax(row[i], h[i][j]);
            }
        }
        for(i = 1; i <= m; i++)
        {
            col[i] = 0;
            for(j = 1; j <= n; j++)
                checkMax(col[i], h[j][i]);
        }
        for(i = 1; i <= n; i++)
        {
            for(j = 1; j <= m; j++)
            {
                if(h[i][j] != row[i] && h[i][j] != col[j])
                    break;
            }
            if(j <= m)  break;
        }
        printf("Case #%d: ", cas++);
        if(i <= n)  printf("NO\n");
        else        printf("YES\n");
    }
    return 0;
}
