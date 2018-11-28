#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
const int maxn=20;
int T,n,r,c,cas=1;
bool mp[maxn][maxn];
inline int f(int st)
{
    int ret=0;
    while (st) ret+=st&1,st>>=1;
    return ret;
}
const int dx[]={0,0,1,-1};
const int dy[]={1,-1,0,0};
bool in(int x,int y){return 0<=x&&x<r&&0<=y&&y<c;}
int calc(int st)
{
    memset(mp,0,sizeof(mp));
    for (int i=r*c-1;i>=0;i--) if(st&(1<<i)) mp[i/c][i%c]=1;
    int ret=0;
    for (int i=0;i<r;i++)
        for (int j=0;j<c;j++)
            if (mp[i][j])
            {
                for (int k=0;k<4;k++)
                {
                    int x=i+dx[k],y=j+dy[k];
                    if (!in(x,y)) continue;
                    if (mp[x][y]) ret++;
                }
            }
    return ret>>1;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("outbbbbbbbb.txt","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d%d",&r,&c,&n);
        int ans=0x3f3f3f3f;
        for (int st=(1<<r*c)-1;st>=0;st--)
        {
            if (f(st)!=n) continue;
            ans=min(ans,calc(st));
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
