#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdarg>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define mp make_pair
#define pb push_back
#define sz(c) (int)(c).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const int maxn = 200;
const int maxm = maxn * maxn;
int p, q, n;
int h[maxn];
int g[maxn];

int dp[maxn][maxm][2];
pair<int, int> dp0[maxm];

pair<int, int> kill(int s) {
  if (s <= 0) return mp(0, -1);
  pair<int, int> &res = dp0[s];
  if (res.first != -1) return res;
  res = mp(0, -1);
  if (s <= p) res = max(res, mp(1, 0));
  pair<int, int> t = kill(s - q);
  t.second += 1;
  res = max(t, res);
  t = kill(s - p - q);
  res = max(res, t);
  //eprintf("kill %d = %d %d\n", s, res.first, res.second);
  return res;
}

int f(int i, int r, int fl) {
  //eprintf("f %d %d\n", i, r);
  assert(r < maxm);
  assert(i < maxn);
  if (i == n) return 0;
  int &res = dp[i][r][fl];
  if (res != -1) return res;
  res = 0;
  int hh = h[i];
  int ttt = (hh + p - 1) / p;
  if (ttt <= r) {
    res = max(res, g[i] + f(i + 1, r - ttt, 1));
  }
  if (fl) {
    hh -= q;
  }
  hh = max(0, hh);
  res = max(f(i + 1, r + (hh + q - 1) / q, 0), res);
  for (int t = 0; t <= r && hh - t * p > 0; t++) {
    pair<int, int> tu = kill(hh - t * p);
    if (tu.first) {
//      eprintf("shoot %d %d\n", i, r);
      res = max(res, g[i] + f(i + 1, r - t + tu.second, 1));
    }
  }
  // eprintf("f %d %d = %d\n", i, r, res);
  return res;
}

void solve(int test) {
  scanf("%d%d%d", &p, &q, &n);
  // if (test == 39) {
  //  eprintf("%d %d %d\n", p, q, n);
  //}
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &h[i], &g[i]);
    // if (test == 39) {
    //  eprintf("%d %d\n", h[i], g[i]);
    //}
  }
  memset(dp, -1, sizeof dp);
  for (int i = 0; i < maxm; i++) dp0[i] = mp(-1, -1);
  printf("Case #%d: %d\n", test, f(0, 0, 0));
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
