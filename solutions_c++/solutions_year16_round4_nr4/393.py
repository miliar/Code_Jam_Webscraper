#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int n;
int g[25][25],h[25];
int id[25];
int ans;
bool check(int worker)
{
    if (worker == n)
        return true;
    int res=0;
    for(int i=0; i<n; ++i)
        if (!h[i] && g[id[worker]][i])
        {
            ++res;
            h[i]=1;
            if (!check(worker + 1))
                return false;
            h[i]=0;
        }
    return res;
}
void solve(int worker, int mac, int cur)
{
    if (cur >= ans)
        return;
    if (mac == n)
    {
        mac=0;
        worker++;
    }
    if (worker == n)
    {
        memset(h, 0, sizeof(h));
        bool flag=1;
        for(int i=0; i<n; ++i)
            id[i]=i;
        do
        {
            if (!check(0))
            {
                flag=0;
                break;
            }
        }
        while (next_permutation(id, id + n));
        if (flag)
            ans=cur;
        return;
    }
    solve(worker, mac + 1, cur);
    if (!g[worker][mac])
    {
        g[worker][mac]=1;
        solve(worker, mac + 1, cur + 1);
        g[worker][mac]=0;
    }
}
int main()
{
    freopen("D-small-attempt0 (1).in","r",stdin);
    freopen("d.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                scanf("%1d",&g[i][j]);
        ans=n*n;
        solve(0, 0, 0);
        printf("Case #%d: %d\n",++ca,ans);
    }
}
