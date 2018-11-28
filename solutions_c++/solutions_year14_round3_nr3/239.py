#include<cstdio>
#include<algorithm>
using namespace std;

#define INF 1000001

int T,N,M,K;

bool mine[25][25];
bool done[25][25];
int ans;
int minans;
int cnt;

int dfs(int x, int y){
  if(x < 0 || x>=N || y<0 || y>=M) return INF;
  if(done[x][y]) return 0;
  if(mine[x][y]) return 0;
  done[x][y]=true;
  int myans=1;
  for(int i=-1;i<=1;i++) for(int j=-1;j<=1;j++) if(i*i+j*j==1){
    myans += dfs(x+i,y+j);
  }
  return myans;
}

int main(){
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    scanf("%d%d%d",&N,&M,&K);
    minans=N*M;
    for(int b=0;b<(1<<(N*M))-1;b++){
      for(int i=0;i<N;i++) for(int j=0;j<M;j++){
        mine[i][j] = (b & (1<<(i*M+j)));
        //printf("i(%d),j(%d): %d\n",i,j,mine[i][j]);
      }
      for(int i=0;i<N;i++) for(int j=0;j<M;j++){
        done[i][j]=false;
      }
      ans=cnt=0;
      for(int i=0;i<N;i++) for(int j=0;j<M;j++){
        if(mine[i][j]){ ans++; cnt++; }
        if(!done[i][j] && !mine[i][j]){
          int now=dfs(i,j);
          if(now<INF) ans+=now;
        }
      }
      if(ans>=K) minans=min(minans,cnt);
    }
    printf("Case #%d: %d\n",t,minans);
  }
  return 0;
}
