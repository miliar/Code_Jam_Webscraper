#include <cstdio>
#include <algorithm>

using namespace std;

int v[1010],d[1010];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,maxx=0,sol=2000000000;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&v[i]);
            maxx=max(maxx,v[i]);
        }
        for(int i=1;i<=maxx;i++)
        {
            int s=i;
            for(int j=1;j<=n;j++) d[v[j]]++;
            for(int j=maxx;j>i;j--)
            {
                s+=d[j];
                d[j-i]+=d[j];
                d[j]=0;
            }
            sol=min(sol,s);
        }
        printf("Case #%d: %d\n",t,sol);
    }
    return 0;
}
