#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int d[1010],x1[1010],y1[1010],x2[1010],y2[1010],a[1010][1010];
bool vis[1010];
int main()
{
    int TT;
    scanf("%d",&TT);
    while (TT--)
    {
        int R,C,n;
        scanf("%d%d%d",&R,&C,&n);
        for (int i=1;i<=n;i++)
        {
            scanf("%d%d%d%d",&x1[i],&y1[i],&x2[i],&y2[i]);
            x1[i]++,y1[i]++,x2[i]++,y2[i]++;
        }
        int S=n+1,T=S+1;
        x1[S]=0,y1[S]=1,x2[S]=0,y2[S]=C;
        x1[T]=R+1,y1[T]=1,x2[T]=R+1,y2[T]=C;
        n+=2;
        memset(a,63,sizeof(a));
        for (int i=1;i<=n;i++)
            for (int j=i+1;j<=n;j++)
            {
                int dx=0,dy=0;
                if (x2[i]<x1[j])
                    dx+=x1[j]-x2[i]-1;
                if (x2[j]<x1[i])
                    dx+=x1[i]-x2[j]-1;
                if (y2[i]<y1[j])
                    dy+=y1[j]-y2[i]-1;
                if (y2[j]<y1[i])
                    dy+=y1[i]-y2[j]-1;
                a[i][j]=a[j][i]=max(dx,dy);
            }
        memset(d,63,sizeof(d));
        d[S]=0;
        memset(vis,0,sizeof(vis));
        for (int i=1;i<=n;i++)
        {
            int k=-1;
            for (int j=1;j<=n;j++)
                if (!vis[j] && (k==-1 || d[j]<d[k]))
                    k=j;
            vis[k]=true;
            for (int j=1;j<=n;j++)
                if (d[k]+a[k][j]<d[j])
                    d[j]=d[k]+a[k][j];
        }
        static int id=0;
        printf("Case #%d: %d\n",++id,d[T]);
    }
    return(0);
}

