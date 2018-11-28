#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#define FOR(i, x, y) for(int i = x; i <= y; ++i)
#define rFOR(i, x, y) for(int i = x; i >= y; --i)
#define MS(a, b) memset(a, b, sizeof(a))
using namespace std;
int t, n, k, b[210];
double a[210], ans, temp;
bool vis[210], vis2[210];
void dfs2(int start, int level)
{
    if(level == k / 2)
    {
        double temp1 = 1.0, temp2 = 1.0;
        FOR(i, 1, k)
        {
            if(vis2[i])
            {
                temp1 *= a[b[i]];
                temp2 *= (1.0 - a[b[i]]);
            }else
            {
                temp2 *= a[b[i]];
                temp1 *= (1.0 - a[b[i]]);
            }
        }
        temp += temp1 + temp2;
        return;
    }
    FOR(i, start + 1, k) if(!vis2[i])
    {
        vis2[i] = true;
        dfs2(i, level + 1);
        vis2[i] = false;
    }
}
void dfs1(int start, int level)
{
    if(level == k)
    {
        temp = 0.0;
        dfs2(0, 0);
        temp /= 2.0;
        if(temp > ans) ans = temp;
        return;
    }
    FOR(i, start + 1, n) if(!vis[i])
    {
        vis[i] = true;
        b[level + 1] = i;
        dfs1(i, level + 1);
        vis[i] = false;
    }
}
int main()
{
	scanf("%d", &t);
	FOR(m, 1, t)
	{
	    printf("Case #%d: ", m);
	    MS(vis, 0); MS(vis, 0);
	    ans = 0.0;
	    scanf("%d%d", &n, &k);
	    FOR(i, 1, n) scanf("%lf", &a[i]);
	    dfs1(0, 0);
	    printf("%.8f\n", ans);
	}
	return 0;
}
