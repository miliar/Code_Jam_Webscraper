#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
struct Point
{
    int x,y,z;
    Point(){}
    Point(int _x,int _y,int _z):x(_x),y(_y),z(_z){}
    Point operator - (const Point &t)const
    {
        return Point(x-t.x,y-t.y,z-t.z);
    }
    int len2()
    {
        return x*x+y*y+z*z;
    }
}p[1005],v[1005];
bool g[1005][1005],vis[1005];
void dfs(int u,int &n)
{
    vis[u]=1;
    for(int i=1;i<=n;i++)
        if(!vis[i] && g[u][i])dfs(i,n);
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,s;
        scanf("%d%d",&n,&s);
        for(int i=1;i<=n;i++)
        {
            scanf("%d%d%d",&p[i].x,&p[i].y,&p[i].z);
            scanf("%d%d%d",&v[i].x,&v[i].y,&v[i].z);
        }
        int l=0,r=100000000;
        while(l<r)
        {
            int m=(l+r)>>1;
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++)
                    g[i][j]=g[j][i]=(p[i]-p[j]).len2()<=m;
            for(int i=1;i<=n;i++)
                vis[i]=0;
            dfs(1,n);
            if(vis[2])r=m;
            else l=m+1;
        }
        printf("Case #%d: %.7f\n",ca,sqrt(l));
    }
    return 0;
}
