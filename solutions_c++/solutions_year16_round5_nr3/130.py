#include <bits/stdc++.h>
using namespace std;
bool visited[1005];
int x[1005], y[1005], z[1005];
int n, s;
double b;
void dfs(int a) {
  if (visited[a]) return ;
  visited[a] = true;
  for (int i = 0; i < n; i++) {
    if ((x[a] - x[i]) * (x[a] - x[i]) + 
        (y[a] - y[i]) * (y[a] - y[i]) + 
        (z[a] - z[i]) * (z[a] - z[i]) <= b * b) {
      dfs(i);
    }
  }
}
bool check(double k) {
  b = k;
  memset(visited, 0, sizeof visited);
  dfs(0);
  return visited[1];
}
double solve() {
  scanf("%d %d", &n, &s);
  for (int i = 0; i < n; i++) {
    scanf("%d %d %d %*d %*d %*d", &x[i], &y[i], &z[i]);
  }
  double l = 0.0, r = 2000.0;
  for (int i = 0; i < 100; i++) {
    double mid = (l + r) / 2.0;
    if (check(mid)) {
      r = mid;
    } else {
      l = mid;
    }
  }
  return l;
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: %.9f", t, solve());
    printf("\n");
  }
  return 0;
}

