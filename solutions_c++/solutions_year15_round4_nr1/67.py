#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void read() { }
template<typename... T> void read(int &h, T &... t) {
  scanf("%d", &h); read(t...);
}
template<typename... T> void read(LL &h, T &... t) {
  scanf("%lld", &h); read(t...);
}
template<typename... T> void read(double &h, T &... t) {
  scanf("%lf", &h); read(t...);
}

const int maxint = 0x7f7f7f7f;
const double eps = 1e-8, pi = acos(-1.0);

const int maxN = 201;
int n, m;
char mp[maxN][maxN];
const int dxy[4][2] = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
pair<int, int> adj[maxN][maxN][4];
bool edge[maxN][maxN];

bool in(int x, int y) {
  return x >= 1 && x <= n && y >= 1 && y <= m;
}

pair<int, int> go(int x, int y, int dir) {
  x += dxy[dir][0];
  y += dxy[dir][1];
  while (in(x, y)) {
    if (mp[x][y] != '.') return make_pair(x, y);
    x += dxy[dir][0];
    y += dxy[dir][1];
  }
  return make_pair(-1, -1);
}

int solve() {
  int cnt = 0;
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      if (mp[i][j] == '.') continue;
      bool flag = false;
      for (int d = 0; d < 4; ++d) {
        adj[i][j][d] = go(i, j, d);
        if (in(adj[i][j][d].first, adj[i][j][d].second)) flag = true;
      }
      edge[i][j] = !flag;
      int what;
      if (mp[i][j] == '^') {
        what = 1;
      } else if (mp[i][j] == 'v') {
        what = 0;
      } else if (mp[i][j] == '>') {
        what = 2;
      } else {
        what = 3;
      }
      if (!in(adj[i][j][what].first, adj[i][j][what].second)) {
        if (edge[i][j]) return -1;
        else ++cnt;
      }
    }
  }
  return cnt;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int tests;
  read(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    scanf("%d%d\n", &n, &m);
    for (int i = 1; i <= n; ++i) {
      gets(mp[i] + 1);
    }
    mset0(edge);
    int a = solve();
    printf("Case #%d: ", tt);
    if (a == -1) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", a);
    }
  }
  return 0;
}