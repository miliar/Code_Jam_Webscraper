#include <iostream>
#include <cassert>
#include <string>
#include <map>
#include <vector>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int dfs(const vector<vector<int>> &adj, vector<int> &used, vector<int> &m, int x) {
  if (x == -1) {
    return 1;
  }
  if (used[x]) {
    return 0;
  }
  used[x] = 1;
  for (auto y : adj[x]) {
    if (dfs(adj, used, m, m[y])) {
      m[y] = x;
      return 1;
    }
  }
  return 0;
}

void solve(int test) {
  int N;
  scanf("%d", &N);
  map<string, int> ah, bh;
  vector<pair<int, int>> e;
  int an = 0, bn = 0;
  for (int i = 0; i < N; i++) {
    string x, y;
    cin >> x >> y;
    if (ah.count(x) == 0) {
      ah[x] = an++;
    }
    if (bh.count(y) == 0) {
      bh[y] = bn++;
    }
    e.push_back(pair<int, int>(ah[x], bh[y]));
  }
  vector<vector<int> > adj(an);
  for (auto x : e) {
    adj[x.first].push_back(x.second);
  }
  vector<int> used(an, 0);
  vector<int> m(bn, -1);
  int res = 0;
  for (int i = 0; i < an; i++) {
    fill(begin(used), end(used), 0);
    res += dfs(adj, used, m, i);
  }
  printf("Case #%d: %d\n", test, N - res - (an + bn - 2 * res));
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
