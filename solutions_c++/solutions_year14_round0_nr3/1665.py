#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
//#include<set>
#include<stdlib.h>
#include<ctype.h>
#include<utility>
#include<cmath>
using namespace std;
//#define REP(k,x,y) for(k=x;k<y;k++)
#pragma comment(linker, "/STACK:1024000000,1024000000")
#define eps 1e-9
#define ll long long
#define i64 __int64
#define INF 2000000000
#define pb push_back
#define sz(b) (int)b.size()
#define lson k<<1
#define rson k<<1|1
#define MOD 10007
#define CLR(t,x) memset(t,x,sizeof(t));
#define N 1000005
#define ls ch[p][0]
#define rs ch[p][1]
#define rp ch[rt][1]
#define lrp ch[rp][0]
int G[6][6],del[36],num[6][6],vis[6][6],n,m,k;
int dir[8][2]={{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
inline bool check(int x,int y)
{
    if(x>=0&&x<n&&y>=0&&y<m) return 1;
    return 0;
}
inline int dfs(int pos)
{
    if(!del[pos]) del[pos]=1;
    int x=pos/m,y=pos%m;
    for(int i=0;i<8;i++)
    {
        int xx=x+dir[i][0];
        int yy=y+dir[i][1];
        if(!num[x][y]&&check(xx,yy)&&!G[xx][yy]&&!del[xx*m+yy]) del[xx*m+yy]=1;
    }
    int cnt=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(!G[i][j]&&del[i*m+j]) cnt++;
    if(cnt==n*m-k) return 1;
    for(int i=0;i<8;i++)
    {
        int xx=x+dir[i][0];
        int yy=y+dir[i][1];
        if(!num[x][y]&&check(xx,yy)&&!G[xx][yy]&&!vis[xx][yy]&&!num[xx][yy])
        {
            vis[xx][yy]=1;
            if(dfs(xx*m+yy)) return 1;
        }
    }
    return 0;
}
int main()
{
    freopen("E:\\C-small-attempt6.in","r",stdin);
    freopen("E:\\C-small-attempt6.out","w",stdout);
    int cas,cnt,ok,flag,tt=1;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d%d%d",&n,&m,&k);
        printf("Case #%d:\n",tt++);
        ok=0;
        for(int i=0;i<(1<<(n*m));i++)
        {
            cnt=0;
            CLR(G,0);CLR(num,0);
            for(int j=0;j<n*m;j++) if(i&(1<<j)) G[j/m][j%m]=1,cnt++;
            if(cnt==k)
            {
                for(int i=0;i<n;i++)
                    for(int j=0;j<m;j++)
                    {
                        if(!G[i][j])
                        {
                            for(int k=0;k<8;k++)
                            {
                                int x=dir[k][0]+i;
                                int y=dir[k][1]+j;
                                if(check(x,y)&&G[x][y]) num[i][j]++;
                            }
                        }
                    }
                for(int i=0;i<n;i++)
                {
                    for(int j=0;j<m;j++)
                    {
                        CLR(del,0);CLR(vis,0);vis[i][j]=1;
                        if(!G[i][j]&&dfs(i*m+j)) {ok=1;flag=i*m+j;break;}
                    }
                    if(ok) break;
                }
            }
            if(ok) break;
        }
        if(ok)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<m;j++)
                {
                    if(flag==i*m+j) printf("c");
                    else if(G[i][j]) printf("*");
                    else printf(".");
                }
                puts("");
            }
        }
        else puts("Impossible");
    }
    return 0;
}
