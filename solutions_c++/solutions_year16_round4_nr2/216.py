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
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

void solve() {
  int N = in();
  int K = in();

  double P[256];
  for (int i = 0; i < N; ++i) {
    P[i] = fin();
  }
  sort(P, P + N);

  double res = 0.0;
  for (int i = 0; i <= K; ++i) {
    double Q[256];
    for (int j = 0; j < i; ++j) {
      Q[j] = P[j];
    }
    for (int j = i; j < K; ++j) {
      Q[j] = P[N - 1 - (j - i)];
    }
    sort(Q, Q + K);

    double dp[222][222];
    for (int j = 0; j <= K; ++j) {
      fill(dp[j], dp[j] + K + 1, 0.0);
    }
    dp[0][0] = 1.0;

    for (int j = 0; j < K; ++j) {
      for (int y = 0; y <= j; ++y) {
        dp[j + 1][y + 1] += dp[j][y] * Q[j];
        dp[j + 1][y] += dp[j][y] * (1.0 - Q[j]);
      }
    }

    chmax(res, dp[K][K / 2]);
  }

  printf("%.9f\n", res);
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
