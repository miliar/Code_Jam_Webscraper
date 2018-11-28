#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

int T,n,k;
double p[210];
long double p1[210];
long double f[210][210];

inline long double check(int x)
{
    for(int i=1;i<=k;i++)
        if(i<=x)
            p1[i]=(long double)p[i];
        else
            p1[i]=(long double)p[n-(k-i+1)+1];
    memset(f,(long double)0.0,sizeof(f));

    f[0][0]=1;
    for(int i=1;i<=k;i++)
    {
        f[i][0]=(long double)f[i-1][0]*(1.0-p1[i]);
        for(int j=1;j<=i;j++)
            f[i][j]=(long double)f[i-1][j-1]*p1[i]+(long double)f[i-1][j]*(1-p1[i]);
    }
    return f[k][k/2];
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
            scanf("%lf",p+i);
        sort(p+1,p+n+1);

        long double ma=(long double)0.0;
        for(int i=0;i<=k;i++)
        {
            long double temp=check(i);
            if(temp>ma)ma=(long double)temp;
        }

        printf("Case #%d: %.10lf\n",t,(double)ma);
    }
}
