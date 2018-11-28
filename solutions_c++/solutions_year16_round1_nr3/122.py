// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int N;
int F[1001];
vector<int> FF[1001];
int d[1001];
int root[1001];
int solve1() {
  int ans = 0;
  for (int i=1; i<=N; ++i) {
    d[i] = -1;
  }
  for (int i=1; i<=N; ++i) {
    if (d[i] == -1) {
      int x;
      int m = 0;
      for(x=i; d[x]==-1; x=F[x]) {
        d[x] = m;
        root[x] = i;
        ++m;
      }
      if (root[x] == i) {
        ans = max(ans, m - d[x]);
      }
    }
  }
  return ans;
}
int solve2() {
  int ans = 0;
  for (int i=1; i<=N; ++i) {
    d[i] = -1;
  }
  for (int i=1; i<=N; ++i) {
    if (d[i] == -1 && F[F[i]] == i) {
      int m=1;
      queue<int> Q;
      d[i] = 1;
      Q.push(i);
      while(!Q.empty()) {
        int u = Q.front(); Q.pop();
        for (int v : FF[u]) {
          if (v != F[i] && d[v] == -1) {
            d[v] = d[u] + 1;
            m = max(m, d[v]);
            Q.push(v);
          }
        }
      }
      ans += m;
      
      m=1;
      d[F[i]] = 1;
      Q.push(F[i]);
      while(!Q.empty()) {
        int u = Q.front(); Q.pop();
        for (int v : FF[u]) {
          if (v != i && d[v] == -1) {
            d[v] = d[u] + 1;
            m = max(m, d[v]);
            Q.push(v);
          }
        }
      }
      ans += m;
    }
  }
  return ans;
}
void solve(int T) {
  scanf("%d", &N);
  for (int i=1; i<=N; ++i) {
    FF[i].clear();
  }
  for (int i=1; i<=N; ++i) {
    scanf("%d", &F[i]);
    FF[F[i]].push_back(i);
    d[i] = -1;
  }
  printf("Case #%d: %d\n", T, max(solve1(), solve2()));
  return;
}
int main(){
  int T;
  scanf("%d\n", &T);
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
