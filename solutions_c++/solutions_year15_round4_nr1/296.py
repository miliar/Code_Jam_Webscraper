#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<map>
#include<set>
#include<vector>
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,n) for(int i=1; i<=n; i++)

typedef long long LL;
using namespace std;
#define N 110
#define UP 0
#define DOWN 1
#define LEFT 2 
#define RIGHT 3

int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};

int n,m,ans,vis[N][N],g[N][N];
bool check(int x,int y){
  return (x>=0 && y>=0 && x<n && y<m);
}
bool dfs(int x,int y){
  if(vis[x][y])return 1;
  vis[x][y]=1;
  int kt=g[x][y];
  for(int xt=x+dx[kt],yt=y+dy[kt]; check(xt,yt); xt+=dx[kt],yt+=dy[kt]){
    if(g[xt][yt]!=4)
      return dfs(xt,yt);
  }
  ans++;
  REP(k,4)if(k!=kt){
    for(int xt=x+dx[k],yt=y+dy[k]; check(xt,yt); xt+=dx[k],yt+=dy[k]){
      if(g[xt][yt]!=4)
        return dfs(xt,yt);
    }
  }
}
char s[N][N];
int main(){
#ifdef QWERTIER
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);
#endif 
  int T;
  scanf("%d",&T);
  FOR(kase,T){
    printf("Case #%d: ",kase);
    scanf("%d%d",&n,&m);
    REP(i,n)scanf("%s",s[i]);
    REP(i,n)REP(j,m){
      if(s[i][j]=='.')g[i][j]=4;
      if(s[i][j]=='^')g[i][j]=UP;
      if(s[i][j]=='v')g[i][j]=DOWN;
      if(s[i][j]=='<')g[i][j]=LEFT;
      if(s[i][j]=='>')g[i][j]=RIGHT;
    }
    memset(vis,0,sizeof(vis));
    ans=0;
    REP(i,n)REP(j,m)if(g[i][j]!=4){
      if(!dfs(i,j)){
        ans=-1;
        break;
      }
    }
    if(ans==-1)puts("IMPOSSIBLE");
    else printf("%d\n",ans);
  }
  return 0;
}
