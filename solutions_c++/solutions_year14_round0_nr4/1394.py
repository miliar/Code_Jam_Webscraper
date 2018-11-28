#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>
#include <map>
#include <stack>
#include <iostream>
using namespace std;
typedef long long ll;
const double eps = 1e-8;
const double PI = acos(-1);
const int maxn =1005;
const int MAXN=1005;
const int inf = 0x3fffffff;
const int mod = 1000000007;

int n;
double a[maxn],b[maxn];
bool vis[maxn];

int nx, ny, m, g[MAXN][MAXN], sy[MAXN], cx[MAXN], cy[MAXN];

int path(int u)
{
    for (int v = 1; v <= ny; v++)if (g[u][v] && !sy[v])
        {
            sy[v] = 1;
            if (!cy[v] || path(cy[v]))
            {
                cx[u] = v;
                cy[v] = u;
                return 1;
            }
        }
    return 0;
}

int MaximumMatch()
{
    int i, ret = 0;
    memset(cx, 0, sizeof (cx));
    memset(cy, 0, sizeof (cy));
    for (i = 1; i <= nx; i++)if (!cx[i])
        {
            memset(sy, 0, sizeof (sy));
            ret += path(i);
        }
    return ret;
}


int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,ncase=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for(int i=1; i<=n; i++)scanf("%lf",&a[i]);
        for(int i=1; i<=n; i++)scanf("%lf",&b[i]);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        int ret1,ret2=0;
        for(int i=1; i<=n; i++)
            vis[i]=0;
        for(int i=1; i<=n; i++)
        {
            int idx=-1;
            for(int j=1; j<=n; j++)
            {
                if(!vis[j]&&a[i]+eps<b[j])
                {
                    idx=j;
                    vis[j]=1;
                    break;
                }
            }
            if(idx==-1)
            {
                ret2++;
                for(int j=1; j<=n; j++)
                    if(!vis[j])
                    {
                        vis[j]=1;
                        break;
                    }
            }
        }
        ret1=ret2;
        nx=ny=n;
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++)
            {
                if(b[j]+eps<a[i])g[i][j]=1;
                else g[i][j]=0;
            }
        ret1=MaximumMatch();
        printf("Case #%d: %d %d\n",++ncase,ret1,ret2);
    }
    return 0;
}
