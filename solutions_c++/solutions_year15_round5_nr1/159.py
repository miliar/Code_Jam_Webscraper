#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);
 
void read() { }
template<typename... T> void read(int &h, T &... t) { scanf("%d", &h); read(t...); }
template<typename... T> void read(LL &h, T &... t) { scanf("%lld", &h); read(t...); }
template<typename... T> void read(double &h, T &... t) { scanf("%lf", &h); read(t...); }

const int maxN = 1000000 + 10;
int tests;
int s0, as, cs, rs;
int m0, am, cm, rm;
int n, diff, parent[maxN], salary[maxN];
vector<int> edge[maxN];
int dset[maxN], block[maxN];
bool active[maxN], deleted[maxN];

void init() {
  for (int i = 0; i < n; ++i) {
    dset[i] = i;
    block[i] = 1;
    active[i] = false;
    deleted[i] = false;
  }
}

int find(int u) {
  if (u == dset[u]) return u;
  dset[u] = find(dset[u]);
  return dset[u];
}

void unite(int u, int v) {
  u = find(u);
  v = find(v);
  if (u != v) {
    dset[u] = v;
    block[v] += block[u];
  }
}

  queue<int> q;

void bfs(int root) {
  while (!q.empty()) q.pop();
  q.push(root);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    if (deleted[u]) continue;
    deleted[u] = true;
    active[u] = false;
    block[find(u)] -= 1;
    for (int v : edge[u]) {
      if (!deleted[v]) {
        q.push(v);
      }
    }
  }
}

void insert(int u) {
  active[u] = true;
  for (int v : edge[u]) {
    if (active[v]) {
      unite(u, v);
    }
  }
  if (u && active[parent[u]]) {
    unite(u, parent[u]);
  }
}

void remove(int u) {
  bfs(u);
}

int main() {
 freopen("A-large.in", "r", stdin);
 freopen("A-large.out", "w", stdout);
  read(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    clog << tt << endl;
    read(n, diff);
    read(s0, as, cs, rs);
    read(m0, am, cm, rm);
    salary[0] = s0;
    for (int i = 0; i < n; ++i) edge[i].clear();
    for (int i = 1; i < n; ++i) {
      s0 = (1ll * s0 * as + cs) % rs;
      m0 = (1ll * m0 * am + cm) % rm;
      parent[i] = m0 % i;
      salary[i] = s0;
      edge[parent[i]].push_back(i);
    }
    init();
    vector<pair<int, int>> pv;
    for (int i = 0; i < n; ++i) {
      pv.push_back(make_pair(salary[i], i));
    }
    sort(pv.begin(), pv.end());
    int p1 = 0, p2 = 0, ans = 0;
    for (int lower = 0; lower <= 1000000; ++lower) {
      int upper = lower + diff;
      while (p2 < n && pv[p2].first <= upper) {
        insert(pv[p2].second);
        p2 += 1;
      }
      while (p1 < n && pv[p1].first < lower) {
        remove(pv[p1].second);
        p1 += 1;
      }
      if (active[0]) {
        ans = max(ans, block[find(0)]);
      }
    }
    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
