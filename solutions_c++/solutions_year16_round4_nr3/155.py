#include<cstdio>
#include<algorithm>
using namespace std;
const int N=200;
int T,C,n,m,i,j,x,y,cnt,id[N][N],f[N],DX[N],DY[N],a[N][N],flag;
struct P{
  int x,y;
  P(){}
  P(int _x,int _y){x=_x,y=_y;}
}pos[N];
bool check(){
  for(int i=1;i<=cnt;i++){
    int x=pos[i].x,y=pos[i].y;
    int dx=DX[i],dy=DY[i];
    x+=dx,y+=dy;
    while(1){
      if(id[x][y])break;
      swap(dx,dy);
      if(!a[x][y])dx*=-1,dy*=-1;
      x+=dx,y+=dy;
    }
    if(id[x][y]!=f[i])return 0;
  }
  return 1;
}
void dfs(int x,int y){
  if(flag)return;
  if(x>n){
    if(check()){
      flag=1;
      for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++)
          if(a[i][j]==0)putchar('/');else putchar('\\');
        puts("");
      }
    }
    return;
  }
  int X,Y;
  a[x][y]=0;
  X=x,Y=y+1;
  if(Y>m)X++,Y=1;
  dfs(X,Y);
  a[x][y]=1;
  X=x,Y=y+1;
  if(Y>m)X++,Y=1;
  dfs(X,Y);
}
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    scanf("%d%d",&n,&m);
    cnt=0;
    for(i=0;i<=n+1;i++)for(j=0;j<=m+1;j++)id[i][j]=0;
    for(i=1;i<=m;i++){
      pos[++cnt]=P(0,i);
      DX[cnt]=1;
      DY[cnt]=0;
    }
    for(i=1;i<=n;i++){
      pos[++cnt]=P(i,m+1);
      DX[cnt]=0;
      DY[cnt]=-1;
    }
    for(i=m;i;i--){
      pos[++cnt]=P(n+1,i);
      DX[cnt]=-1;
      DY[cnt]=0;
    }
    for(i=n;i;i--){
      pos[++cnt]=P(i,0);
      DX[cnt]=0;
      DY[cnt]=1;
    }
    for(i=1;i<=cnt;i++)id[pos[i].x][pos[i].y]=i;
    for(i=1;i<=n+m;i++){
      scanf("%d%d",&x,&y);
      f[x]=y;
      f[y]=x;
    }
    printf("Case #%d:\n",C);
    flag=0;
    dfs(1,1);
    if(!flag)puts("IMPOSSIBLE");
  }
  return 0;
}