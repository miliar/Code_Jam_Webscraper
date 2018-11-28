#include <cstdio>
#include <algorithm>

using namespace std;

double v[210],d[210][210];
int v1[210];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,k;
        double sol=0;
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++) scanf("%lf",&v[i]);
        for(int mask=1;mask<(1<<n);mask++)
        {
            int nr=0;
            for(int i=0;i<n;i++)
                if(mask&(1<<i)) v1[++nr]=i;
            if(nr!=k) continue;
            d[0][0]=1;
            for(int i=1;i<=k;i++)
            {
                d[i][0]=d[i-1][0]*(1-v[v1[i]]);
                int lim=min(i,k);
                for(int j=1;j<=nr;j++)
                    d[i][j]=d[i-1][j-1]*v[v1[i]]+d[i-1][j]*(1-v[v1[i]]);
            }
            sol=max(sol,d[k][k/2]);
        }
        printf("Case #%d: %.7f\n",t,sol);
    }
    return 0;
}
