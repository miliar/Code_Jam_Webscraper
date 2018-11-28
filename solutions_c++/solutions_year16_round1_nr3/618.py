#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
int _T;
int N, A[MAXN], res;
int tail[MAXN], dep[MAXN];
bool vis[MAXN];

void dfs(int v, int p, int d){
  if(vis[v]){
    res = max(res, d - dep[v]);
    if(A[v] == p){
      tail[v] = max(tail[v], d - 1);
    }
    return;
  }
  vis[v] = 1;
  dep[v] = d;
  dfs(A[v], v, d + 1);
}

int main(){
  scanf("%d", &_T);
  for(int _t = 1; _t <= _T; _t++){
    printf("Case #%d: ", _t);
    scanf("%d", &N);
    for(int i = 0; i < N; i++){
      scanf("%d", &A[i]);
      A[i] -= 1;
    }
    res = 0;
    fill(tail, tail + N, 0);
    for(int i = 0; i < N; i++){
      fill(vis, vis + N, 0);
      dfs(i, -1, 0);
    }
    int tot = 0;
    for(int i = 0; i < N; i++){
      tot += tail[i];
    }
    res = max(res, tot);
    printf("%d\n", res);
  }
}
