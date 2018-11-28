#include<iostream>
using namespace std;
int n,m,a[2000],b[2000],c[2000];
int cost(int x)
{
    return n*x-(x-1)*x/2;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int TT=1;TT<=T;++TT)
    {
        scanf("%d%d",&n,&m);
        for (int i=1;i<=m;++i)
            scanf("%d%d%d",&a[i],&b[i],&c[i]);
        int ans=0;
        bool flag=1;
        while (flag)
        {
            flag=0;
            int cura,curb,curc=0;
            for (int i=1;i<m;++i)
                for (int j=i+1;j<=m;++j)
                    if (c[i]>0&&c[j]>0&&a[i]<=b[j]&&a[j]<=b[i])
                    {
                        int v=cost(b[i]-a[i])+cost(b[j]-a[j])-cost(b[j]-a[i])-cost(b[i]-a[j]);
                        if (v>curc) {flag=1;cura=i;curb=j;curc=v;}
                    }
            if (flag)
            {
                int p=min(c[cura],c[curb]);
                ans+=curc*p;
                c[cura]-=p;c[curb]-=p;
                a[++m]=a[cura];b[m]=b[curb];c[m]=p;
                a[++m]=a[curb];b[m]=b[cura];c[m]=p;
            }
        }
        printf("Case #%d: %d\n",TT,ans);
    }
}
