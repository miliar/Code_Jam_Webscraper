#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#define ll long long
#define db double
using namespace std;

int t,n,m,k;
char s[110][110];
int u[110][110];
int p[110][110][4];
int nx[110];

int dfs(int x,int y)
{
    u[x][y]=1;
    if(s[x][y]=='<')
    {
        if(p[x][y][0]==-1) return 0;
        if(u[x][p[x][y][0]]) return 1;
        int res=dfs(x,p[x][y][0]);
        if(res) return 1;
        return 0;
    }
    if(s[x][y]=='>')
    {
        if(p[x][y][2]==-1) return 0;
        if(u[x][p[x][y][2]]) return 1;
        int res=dfs(x,p[x][y][2]);
        if(res) return 1;
        return 0;
    }
    if(s[x][y]=='^')
    {
        if(p[x][y][1]==-1) return 0;
        if(u[p[x][y][1]][y]) return 1;
        int res=dfs(p[x][y][1],y);
        if(res) return 1;
        return 0;
    }
    if(s[x][y]=='v')
    {
        if(p[x][y][3]==-1) return 0;
        if(u[p[x][y][3]][y]) return 1;
        int res=dfs(p[x][y][3],y);
        if(res) return 1;
        return 0;
    }
}

int main()
{
#ifdef Haha
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out","w",stdout);
#endif // Haha
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        scanf("%d%d",&n,&m);
        memset(u,0,sizeof(u));
        memset(p,-1,sizeof(p));
        memset(nx,-1,sizeof(nx));
        for(int i=0; i<n; i++) scanf("%s",s[i]);
        for(int i=0; i<n; i++)
        {
            int ny=-1;
            for(int j=0; j<m; j++)
            {
                if(s[i][j]=='.') continue;
                p[i][j][0]=ny;
                p[i][j][1]=nx[j];
                ny=j;
                nx[j]=i;
            }
        }
        memset(nx,-1,sizeof(nx));
        for(int i=n-1; i>=0; i--)
        {
            int ny=-1;
            for(int j=m-1; j>=0; j--)
            {
                if(s[i][j]=='.') continue;
                p[i][j][2]=ny;
                p[i][j][3]=nx[j];
                ny=j;
                nx[j]=i;
            }
        }
        int ans=0;
        int flag=0;
        for(int i=0; i<n; i++)
        {
            if(flag) break;
            for(int j=0; j<m; j++)
            {
                if(s[i][j]=='.') continue;
                if(p[i][j][0]==-1&&p[i][j][1]==-1&&p[i][j][2]==-1&&p[i][j][3]==-1)
                {
                    flag=1;
                    break;
                }
                if(!u[i][j])
                {
                    int res=dfs(i,j);
                    if(res==0) ans++;
                }
            }
        }
        if(flag) printf("Case #%d: IMPOSSIBLE\n",cas);
        else printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
