#include<cstdio>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int xx[1005],yy[1005],zz[1005];
double dd[1005][1005];
int fa[1005];
int find(int x){ return fa[x]==x?fa[x]:fa[x]=find(fa[x]);}
main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n,s;
        scanf("%d%d",&n,&s);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d%d%*d%*d%*d",&xx[i],&yy[i],&zz[i]);
        }
        memset(dd,0,sizeof(dd));
        for(int i=0;i<n;i++)
        for(int j=0;j<i;j++)
        dd[i][j]=dd[j][i]=sqrt((xx[i]-xx[j])*(xx[i]-xx[j])+(yy[i]-yy[j])*(yy[i]-yy[j])+(zz[i]-zz[j])*(zz[i]-zz[j]));
        double l=0,r=20000,mid;
        int t=100;
        while(t--)
        {
            mid=(l+r)/2;
            for(int i=0;i<n;i++) fa[i]=i;
            for(int i=0;i<n;i++)
            for(int j=0;j<i;j++) if(dd[i][j]<mid)
            {
                int fi=find(i),fj=find(j);
                if(fi!=fj) fa[fi]=fj;
            }
            if(find(0)!=find(1)) l=mid;
            else r=mid;
        }
        printf("Case #%d: %.8f\n",++cas,mid);
    }
}
