#include<cstdio>
#include<algorithm>
using namespace std;
const int N=6;
int T,C,n,i,j,b[N][N],v[N],p[N],ans,flag;char a[N][N];
void dfs2(int x){
  if(flag)return;
  if(x==n)return;
  int y=p[x],can=0;
  for(int i=0;i<n;i++)if(b[y][i]&&!v[i])can=1;
  if(!can){flag=1;return;}
  for(int i=0;i<n;i++)if(b[y][i]&&!v[i]){
    v[i]=1;
    dfs2(x+1);
    v[i]=0;
  }
}
bool cal(){
  int i;
  flag=0;
  for(i=0;i<n;i++)p[i]=i;
  do{
    for(i=0;i<n;i++)v[i]=0;
    dfs2(0);
    if(flag)return 0;
  }while(next_permutation(p,p+n));
  if(flag)return 0;
  return 1;
}
void dfs(int x,int y,int w){
  if(w>=ans)return;
  if(x==n){
    if(cal())ans=w;
    return;
  }
  if(!a[x][y]){
    b[x][y]=0;
    int X=x,Y=y+1;
    if(Y==n)X++,Y=0;
    dfs(X,Y,w);
  }
  b[x][y]=1;
  int X=x,Y=y+1;
  if(Y==n)X++,Y=0;
  dfs(X,Y,w+1-a[x][y]);
}
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    scanf("%d",&n);
    ans=n*n;
    for(i=0;i<n;i++){
      scanf("%s",a[i]);
      for(j=0;j<n;j++)a[i][j]-='0';
    }
    dfs(0,0,0);
    printf("Case #%d: %d\n",C,ans);
  }
  return 0;
}