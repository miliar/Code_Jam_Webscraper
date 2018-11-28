#include <cstdio>
#define ss(a) scanf("%d",&a)
#define ds(a,b) scanf("%d %d",&a,&b)
int p[105][105];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t,n,m,k,i,j;
    ss(t);
    for(k=1;k<=t;k++)
    {
        int flag=1;
        ds(n,m);
        for(i=1;i<=n;i++)
        {
            int zd=-1;
             for(j=1;j<=m;j++)
             {
                 ss(p[i][j]);
                 if(p[i][j]>zd)
                 zd=p[i][j];
             }
             p[i][0]=zd;

        }
        for(j=1;j<=m;j++)
        {
            int zd=-1;
             for(i=1;i<=n;i++)
             {
                 if(p[i][j]>zd)
                 zd=p[i][j];
             }
             p[0][j]=zd;
        }
        for(i=1;i<=n;i++)
        for(j=0;j<=m;j++)
        {
            if(p[i][j]==p[0][j]||p[i][j]==p[i][0])
            continue;
            else
            flag=0;
        }
        if(flag)
      printf("Case #%d: YES\n",k);
      else
      printf("Case #%d: NO\n",k);
    }
    return 0;


}

