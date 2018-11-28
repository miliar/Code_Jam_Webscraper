#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
long long t,n,m,h[102][102];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%lld",&t);
    for(int o=1; o<=t; o++)
    {
        scanf("%lld%lld",&n,&m);
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                scanf("%lld",&h[i][j]);
            }
        }
        for(int i=1; i<=m; i++) h[n+1][i]=0;
        for(int i=1; i<=n; i++) h[i][m+1]=0;
        printf("Case #%d: ",o);
        int e=0;
        for(int i=1; i<=n; i++)
        {
            long long max1=0;
            for(int j=1; j<=m; j++)
            {
                max1=max(max1,h[i][j]);
            }
            for(int j=1; j<=m; j++)
            {
                if(h[i][j]==max1) continue;
                for(int l=1; l<=n; l++)
                {
                    if(h[l][j]>h[i][j]) {printf("NO\n"); e=1; break;}
                }
                if(e==1) break;
            }
            if(e==1) break;
        }
        if(e==0) printf("YES\n");
    }
    return 0;
}
