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

int H[128], G[128];
int dp[128][1024][2];

void solve() {
  int Q = in();
  int P = in();
  int N = in();
  for (int i = 0; i < N; ++i) {
    H[i] = in();
    G[i] = in();
  }

  for (int i = 0; i <= N; ++i) {
    for (int j = 0; j < 1024; ++j) {
      dp[i][j][0] = dp[i][j][1] = -1;
    }
  }
  dp[0][0][0] = 0;

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < 1024; ++j) {
      for (int k = 0; k < 2; ++k) {
        if (dp[i][j][k] >= 0) {
          // cerr<<i<<' '<<j<<' '<<k<<' '<<dp[i][j][k]<<endl;
          // don't kill
          chmax(dp[i + 1][j + (H[i] + P - 1) / P - k][0], dp[i][j][k]);

          // kill
          int hp = H[i];
          if (k > 0 && hp - P <= 0) {
            if ((hp + Q - 1) / Q <= j) {
              chmax(dp[i + 1][j - (hp + Q - 1) / Q][1], dp[i][j][k] + G[i]);
            }
          } else {
            hp -= P * k;
            int need = 0;
            for (int hh = hp; ; ) {
              int modp = hh % P;
              if (modp == 0) modp = P;
              if (modp <= Q) {
                break;
              }
              ++need;
              hh -= Q;
            }
            // cerr<<hp<<' '<<need<<endl;
            if (hp - need * Q - need * P >= 1) {
              int rem = hp - need * Q - need * P;
              chmax(dp[i + 1][j + (rem + P - 1) / P - 1][1], dp[i][j][k] + G[i]);
            } else {
              int use = 0;
              while (hp - need * Q - (need - use) * P <= 0) {
                ++use;
              }
              if (use <= j) {
                chmax(dp[i + 1][j - use][1], dp[i][j][k] + G[i]);
              }
            }
          }
        }
      }
    }
  }

  int res = 0;
  for (int j = 0; j < 1024; ++j) {
    chmax(res, max(dp[N][j][0], dp[N][j][1]));
  }
  printf("%d\n", res);
}

int main()
{
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
