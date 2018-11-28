#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }

int cur_T;

struct st {
  int b, s;
  st(int b, int s) : b(b), s(s) { }
};
bool operator < (const st& a, const st& b) {
  return a.s > b.s;
}

int adj[1024][1024];

int dist(int a0, int b0, int a1, int b1) {
  return max(0, max(a1 - b0, a0 - b1) - 1);
}

void solve() {
  int W = in();
  int H = in();
  int B = in();

  int X0[1024], Y0[1024], X1[1024], Y1[1024];
  vector<int> ys;
  for (int i = 0; i < B; ++i) {
    X0[i] = in();
    Y0[i] = in();
    X1[i] = in();
    Y1[i] = in();
  }

  for (int i = 0; i < B; ++i) {
    adj[i][i] = 0;
    for (int j = i + 1; j < B; ++j) {
      int dx = dist(X0[i], X1[i], X0[j], X1[j]);
      int dy = dist(Y0[i], Y1[i], Y0[j], Y1[j]);
      adj[i][j] = adj[j][i] = max(dx, dy);
    }
  }

  int dist[1024];
  priority_queue<st> Q;
  for (int i = 0; i < B; ++i) {
    dist[i] = X0[i];
    Q.push(st(i, dist[i]));
  }

  int res = W;
  while (!Q.empty()) {
    st s = Q.top(); Q.pop();
    if (s.s != dist[s.b]) {
      continue;
    }

    chmin(res, s.s + (W - X1[s.b] - 1));
    for (int i = 0; i < B; ++i) {
      int d = s.s + adj[s.b][i];
      if (dist[i] > d) {
        dist[i] = d;
        Q.push(st(i, d));
      }
    }
  }

  printf("%d\n", res);
}

int main()
{
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    cur_T = CN;
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
