#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

int N,M,S,L;
int A[100];

int id[20][20][4];
int n;

const int dir[4][2]={{0,-1},{-1,0},{0,1},{1,0}};

inline int inside(int x,int y){return x>=0&&x<=N&&y>=0&&y<=M;}

int tar[100];

int fst[100];
int find(int a){return (fst[a]==a?a:(fst[a]=find(fst[a])));}

int sol[20][20];

int getbit(int msk,int x,int y){
  int k = x * M + y;
  return !!(msk&(1<<k));
}

void join(int x,int y){
  fst[find(x)]=find(y);
}

bool check(int msk) {
  for(int i=0;i<n;++i)fst[i]=i;
  for(int i=0;i<N;++i){
    for(int j=0;j<M;++j){
      if(getbit(msk,i,j)) { // dir < / >
        join(id[i][j][2],id[i][j][3]);
        join(id[i+1][j+1][0],id[i+1][j+1][1]);
      } else { // dir < \ >
        join(id[i][j][2],id[i+1][j+1][1]);
        join(id[i][j][3],id[i+1][j+1][0]);
      }
    }
  }
  
  for(int i=0;i<L;++i){
    int x = tar[A[i]];
    int y = tar[A[i^1]];
    if(find(x) != find(y)) return false;
    for(int j=0;j<L;++j){
      if(j != i && (j != (i ^ 1)) && find(x) == find(tar[A[j]])) return false;
    }
  }
  return true;
}

void run() {
  cin >> N >> M;
  S=N*M;
  L=2*(N+M);
  int a;
  for(int i=0;i<L;++i){
    cin >> A[i];
  }
  n = 0;
  memset(id,-1,sizeof(id));
  for(int x=0;x<=N;++x){
    for(int y=0;y<=M;++y){
      for(int d=0;d<2;++d){
        int tx=x+dir[d][0];
        int ty=y+dir[d][1];
        if(inside(tx,ty)){
          id[x][y][d]=id[tx][ty][(2+d)&3]=n;
          ++n;
        }
      }
    }
  }
  
  for(int k=1;k<=M;++k){
    tar[k]=id[0][k][0];
    tar[k + N + M]=id[N][M+1-k][0];
  }
  for(int k=1;k<=N;++k){
    tar[M + k] = id[k][M][1];
    tar[M+N+M+k] = id[N+1-k][0][1];
  }
  
  memset(sol,-1,sizeof(sol));
  for(int msk=0;msk<(1<<S);++msk){
    if(check(msk)) {
      for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
          sol[i][j]=getbit(msk,i,j);
        }
      }
      break;
    }
  }
  
  if(sol[0][0]<0){
    cout << "IMPOSSIBLE" << endl;
  } else {
    for(int i=0;i<N;++i){
      for(int j=0;j<M;++j){
        if(sol[i][j]){
          cout << '/' ;
        } else 
          cout << '\\';
      }
      cout << endl;
    }
  }
}

int main() {
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  int test;
  cin >> test;
  for(int no=1;no<=test;++no){
    cout<<"Case #"<<no<<":"<<endl;
    run();
  }
}
