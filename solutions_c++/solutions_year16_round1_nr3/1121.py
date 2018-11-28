#include <cstdio>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>

#include <iostream>
#include <numeric>

using namespace std;

int Solve(const vector<size_t>& fs) {
  size_t ret = 0;

  vector<vector<size_t>> adj(fs.size());

  struct State { size_t cur, root, dist; };
  queue<State> q;
  for (size_t i = 0; i < fs.size(); i++) {
    if (fs[fs[i]] == i) {
      q.push(State { i, fs[i], 1 });
      q.push(State { fs[i], i, 1 });
    }
    else
      adj[fs[i]].push_back(i);

    vector<int> dt(fs.size(), 0); int cur_dt = 0;
    auto u = i;
    for (u = i; ; u = fs[u]) {
      dt[u] = ++cur_dt;
      if (dt[fs[u]]) break;
    }
    size_t cycle_len = dt[u] - dt[fs[u]] + 1;
    ret = max(ret, cycle_len);
  }

  vector<size_t> sizes(fs.size());
  vector<bool> vis(fs.size(), false);
  for (; !q.empty(); q.pop()) {
    const auto& u = q.front();
    if (vis[u.cur]) continue;
    vis[u.cur] = true;
    sizes[u.root] = max(sizes[u.root], u.dist);
    for (const auto& v : adj[u.cur]) {
      q.push(State{ v, u.root, u.dist + 1 });
    }
  }
  size_t ret_hub = accumulate(sizes.begin(), sizes.end(), 0);
  ret = max(ret, ret_hub);

  return ret;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 0; tc < t; ++tc) {
    int n; scanf("%d", &n);
    vector<size_t> fs(n);
    for (int i = 0; i < n; i++) {
      int f; scanf("%d", &f);
      fs[i] = --f;
    }
    printf("Case #%d: %d\n", tc + 1, Solve(fs));
  }
  return 0;
}
