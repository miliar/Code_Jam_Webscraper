#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "C"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

const ll INF = ll(1000000000) * 1000000000;

ll PointDist(int x0, int y0, int x1, int y1) {
  return max(max(abs(x0 - x1), abs(y0 - y1)) - 1, 0);
}

ll PointDist(pii a, pii b) {
  return PointDist(a.first, a.second, b.first, b.second);
}

vector<pii> GetCorners(int x0, int y0, int x1, int y1) {
  vector<pii> res;
  res.push_back(MP(x0, y0));
  res.push_back(MP(x0, y1));
  res.push_back(MP(x1, y1));
  res.push_back(MP(x1, y0));
  return res;
}

bool Between(int x, int a, int b) {
  return (x >= min(a, b) && x <= max(a, b));
}

ll PointLineDist(pii x, pii a, pii b) {
  if (a.first == b.first && Between(x.second, a.second, b.second)) {
    pii y = MP(a.first, x.second);
    return PointDist(x, y);
  } else if (a.second == b.second && Between(x.first, a.first, b.first)) {
    pii y = MP(x.first, a.second);
    return PointDist(x, y);
  } else {
    return INF;
  }
}

ll ComputeDist(int ax0, int ay0, int ax1, int ay1, int bx0, int by0, int bx1, int by1) {
  vector<pii> a = GetCorners(ax0, ay0, ax1, ay1);
  vector<pii> b = GetCorners(bx0, by0, bx1, by1);
  ll res = INF;
  for (int i = 0; i < a.size(); ++i) {
    for (int j = 0; j < b.size(); ++j) {
      res = min(res, PointDist(a[i], b[j]));
      res = min(res, PointLineDist(a[i], b[j], b[(j + 1) % b.size()]));
      res = min(res, PointLineDist(b[j], a[i], a[(i + 1) % a.size()]));
    }
  }
  return res;
}

ll ComputeMaxFlowFast(int W, int H, int B, const vi& x0, const vi& y0, const vi& x1, const vi& y1) {
  int N = B + 2;
  int s = N - 1;
  int t = N - 2;    
  vector< vector<ll> > G(N, vector<ll>(N, INF));
  G[s][t] = W;
  for (int i = 0; i < B; ++i) {
    G[s][i] = x0[i];
    G[i][t] = W - 1 - x1[i];
  }
  for (int i = 0; i < B; ++i) {
    for (int j = 0; j < B; ++j) {
      G[i][j] = ComputeDist(x0[i], y0[i], x1[i], y1[i], x0[j], y0[j], x1[j], y1[j]);
    }
  }
  vector<ll> dists(N, INF);
  dists[s] = 0;
  vb done(N, false);
  for (int i = 0; i < N; ++i) {
    int min_index = -1;
    ll min_dist = INF;
    for (int j = 0; j < N; ++j) {
      if (!done[j] && dists[j] < min_dist) {
        min_index = j;
        min_dist = dists[j];
      }
    }
    if (min_index == -1) {
      cerr << "WTF!" << endl;
      abort();
    }
    done[min_index] = true;
    for (int j = 0; j < N; ++j) {
      if (!done[j] && dists[j] > min_dist + G[min_index][j]) {
        dists[j] = min_dist + G[min_index][j];
      }
    }
  }
  ll result = dists[t];
  return result;
}

// Regular max flow
vvi G;
int N;
int s;
int t;
vb done;

int dfs(int a, int by) {
  if (done[a]) {
    return 0;
  }
  done[a] = true;
  if (a == t) {
    return by;
  }
  for (int i = 0; i < N; ++i) {
    if (G[a][i] > 0) {
      int am = dfs(i, min(by, G[a][i]));
      if (am > 0) {
        G[a][i] -= am;
        G[i][a] += am;
        return am;
      }
    }
  }
  return 0;
}

int MaxFlow() {
  int fl = 0;
  int am = 1;
  while (am > 0) {
    done.assign(N, false);
    
    am = dfs(s, 1000000000);
    if (am > 0) {
      fl += am;
    }
  }
  return fl;
}

ll ComputeMaxFlowSlow(int W, int H, int B, const vi& x0, const vi& y0, const vi& x1, const vi& y1) {
  N = 2 * W * H + 2;
  s = N - 1;
  t = N - 2;
  G.assign(N, vi(N));
  vvi field(W, vi(H, 0));
  for (int i = 0; i < B; ++i) {
    for (int x = x0[i]; x <= x1[i]; ++x) {
      for (int y = y0[i]; y <= y1[i]; ++y) {
        field[x][y] = 1;
      }
    }
  }
  for (int x = 0; x < W; ++x) {
    if (!field[x][0]) {
      G[s][x] = 1;
    }
    if (!field[x][H - 1]) {
      G[(H - 1) * W + x][t] = 1;
    }
  }
  for (int x = 0; x < W; ++x) {
    for (int y = 0; y < H; ++y) {
      if (!field[x][y]) {
        G[H * W + y * W + x][y * W + x] = 1;
        for (int dx = -1; dx <= 1; ++dx) {
          for (int dy = -1; dy <= 1; ++dy) {
            if (abs(dx) + abs(dy) == 1) {
              int nx = x + dx;
              int ny = y + dy;
              if (nx >= 0 && nx < W && ny >= 0 && ny < H && !field[nx][ny]) {
                G[y * W + x][W * H + ny * W + nx] = 1;
              }
            }
          }
        }
      }
    }
  }
  return MaxFlow();
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int W, H, B;
    cin >> W >> H >> B;
    cerr << test_index + 1 << ' ' << W << ' ' << H << ' ' << B << endl;
    vi x0(B), y0(B), x1(B), y1(B);
    for (int i = 0; i < B; ++i) {
      cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
    }
    /*if (W * H > 3000) {
      continue;
    }*/
    ll result1 = ComputeMaxFlowFast(W, H, B, x0, y0, x1, y1);
    //ll result2 = ComputeMaxFlowSlow(W, H, B, x0, y0, x1, y1);
    /*if (result1 != result2) {
      cerr << "Wrong answer!" << endl;
      cerr << result1 << ' ' << result2 << endl;
      cerr << W << ' ' << H << ' ' << B << endl;
      for (int i = 0; i < B; ++i) {
        cerr << x0[i] << ' ' << y0[i] << ' ' << x1[i] << ' ' << y1[i] << endl;
      }
      break;
    } else {
      cerr << "OK" << endl;
    }*/
    cout << "Case #" << (test_index + 1) << ": " << result1 << endl;
  }
  return 0;
}
