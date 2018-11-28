#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

double p[5000];
bool was[202][202];
double dp[202][202][202];

int count(int x) {
  int ret = 0;
  while (x) {
    if (x & 1) {
      ++ret;
    }
    x >>= 1;
  }
  return ret;
}

double DFS(int l, int r, int k) {
  if (!k) {
    return 1.0;
  }
  if (k > r - l) {
    return 0;
  }
  if (r == l + 1) {
    return k ? p[l] : (1 - p[l]);
  } else {
    if (dp[l][r][k] > -0.5) {
      return dp[l][r][k];
    }
    int len = r - l;
    int mid = l + len / 2;
    double ret = 0;
    for (int k1 = 0; k1 <= k; ++k1) {
      ret = max(ret, DFS(l, mid, k1) * DFS(mid, r, k - k1));
    }
    return dp[l][r][k] = ret;
  }
}

double v[205];
double gg[205];

double DoIt(int n) {
  memset(gg, 0, sizeof gg);
  gg[0] = 1.0;
  for (int i = 0; i < n; ++i) {
    for (int j = n; j >= 0; --j) {
      gg[j] *= (1 - v[i]);
      if (j) {
        gg[j] += v[i] * gg[j - 1];
      }
    }
  }
  return gg[n / 2];
}

void Solve() {
  /*
  for (int i = 0; i < 202; ++i) {
    for (int j = 0; j < 202; ++j) {
      for (int k = 0; k < 202; ++k) {
        dp[i][j][k] = -1;
      }
    }
  }*/
  int n, k;
  cin >> n >> k;
  for (int i = 0; i < n; ++i) {
    cin >> p[i];
  }
  sort(p, p + n);
  double ans = 0;
  for (int i = 0; i <= k; ++i) {
    for (int j = 0 ; j < i; ++j) {
      v[j] = p[j];
    }
    for (int j = 0; j + i <= k; ++j) {
      v[i + j] = p[n - 1 - j];
    }
    ans = max(ans, DoIt(k));
  }

  printf("%.9lf\n", ans);
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
