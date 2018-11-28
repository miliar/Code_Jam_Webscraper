#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;

map<string, int> X;
map<string, int> Y;
vector<int> G[MAXN];
int mate[MAXN], vis[MAXN];

bool dfs(int u) {
  for (auto &v: G[u]) if (!vis[v]) {
    vis[v] = true;
    if (mate[v] == -1 || dfs(mate[v])) {
      mate[v] = u; return true;
    }
  }
  return false;
}

int match() {
  memset(mate, -1, sizeof(mate));
  int ret = 0;
  for (int i = 0; i < X.size(); ++i) {
    memset(vis, 0, sizeof(vis));
    if (dfs(i)) ++ret;
  }
  return ret;
}

void run(int cas) {
  printf("Case #%d: ", cas);
  X.clear(); Y.clear();
  int n; scanf("%d", &n);
  for (int i = 0; i < MAXN; ++i) G[i].clear();
  for (int i = 0; i < n; ++i) {
    string s, t; cin >> s >> t;
    int u, v;
    if (X.count(s)) u = X[s];
    else u = X.size(), X[s] = u;
    if (Y.count(t)) v = Y[t];
    else v = Y.size(), Y[t] = v;
    G[u].push_back(v);
  }
  int x = match();
  printf("%d\n", n - (int)X.size() - (int)Y.size() + x);
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}
