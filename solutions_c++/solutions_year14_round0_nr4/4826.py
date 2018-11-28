#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <queue>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;
int n;
int solve1(double *a,double *b)
{
    sort(a,a+n);
    sort(b,b+n);
    int ans=0;
    bool vis[1005];
    memset(vis,0,sizeof(vis));
    for(int i=0;i<n;i++)
    {
        int j;
        for(j=0;j<n;j++)
        {
            if(vis[j]) continue;
            if(b[j]<a[i]) break;
        }
        if(j<n)
        {
            ans++;
            vis[j]=true;
        }
        else
        {
            for(j=n-1;j>=0;j--) if(!vis[j]) break;
            vis[j]=true;
        }
    }
    return ans;
}
int solve2(double *a,double *b)
{
    sort(a,a+n);
    sort(b,b+n);
    int ans=0;
    bool vis[1005];
    memset(vis,0,sizeof(vis));
    for(int i=0;i<n;i++)
    {
        int j;
        for(j=0;j<n;j++)
        {
            if(vis[j]||b[j]<a[i]) continue;
            else break;
        }
        if(j<n) vis[j]=true;
        else
        {
            ans++;
            for(j=0;j<n;j++) if(!vis[j]) break;
            vis[j]=true;
        }
    }
    return ans;
}
int main()
{
   // freopen("out.txt","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        double a[1005],b[1005];
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%lf",&a[i]);
        for(int i=0;i<n;i++) scanf("%lf",&b[i]);
        printf("Case #%d: %d %d\n",cas++,solve1(a,b),solve2(a,b));
    }
    return 0;
}
