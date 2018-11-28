#include <cstdio>
#include <vector>
#include <algorithm>
#define For(i,N) for(int i=0; i<N; i++)

using namespace std;

int T,N,M;
vector<vector<int> > V;
vector<int> x_max,y_max;

int main(){
  scanf("%d",&T);
  For(t,T){
    x_max.clear(); y_max.clear(); V.clear();
    scanf("%d %d",&N, &M);
    V.resize(N, vector<int>(M));
    x_max.resize(N,0);
    y_max.resize(M,0);
    For(i,N) For(j,M){ 
      scanf(" %d ",&V[i][j]);
      x_max[i] = max(x_max[i],V[i][j]);
      y_max[j] = max(y_max[j],V[i][j]);
    }
    bool vys = 1;
    For(i,N) For(j,M) if(x_max[i] > V[i][j] && y_max[j] > V[i][j]) vys = 0;
    printf("Case #%d: %s\n",t+1,vys ? "YES" : "NO");
  }
  return 0;
}