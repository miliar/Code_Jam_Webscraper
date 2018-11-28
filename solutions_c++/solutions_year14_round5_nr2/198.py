#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

#define REP(i, n) FOR(i, 0, n)
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int main(void)
{
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    int p, q, n; scanf("%d %d %d", &p, &q, &n);

    const int MAXN = 101;
    const int MAXK = MAXN*11 + 123;
    const int inf = 1e9;

    static int dp[MAXN][MAXK][2];
    REP(i, n+1) REP(j, MAXK) REP(k, 2) dp[i][j][k] = -inf;
    dp[0][0][0] = 0;

    auto chmax = [](int& a, int b) { if (b > a) a = b; };
    REP(i, n) {
      int h, g; scanf("%d %d", &h, &g);

      REP(k, 2) {
        int step = 0;
        if (p < q && h - k*q > 0) {
          int tmp = h - k*q;
          while (tmp%q == 0 || tmp%q > p) { tmp -= p; ++step; }
        }
        int thit = (h - k*q - step*p + q-1) / q;

        REP(j, MAXK) if (dp[i][j][k] != -inf) {
          if (k) {
            int phit = (h + p-1) / p;
            if (j-phit >= 0) {
              chmax(dp[i+1][j-phit][1], dp[i][j][k] + g);
            }
          }

          if (h - k*q <= 0) {
            chmax(dp[i+1][j][0], dp[i][j][k]);
          } else {
            int all_hit = (h - k*q + q-1) / q;
            assert(j + all_hit < MAXK);
            chmax(dp[i+1][j+all_hit][0], dp[i][j][k]);

            int fora = j+thit;
            if (fora-step-1 >= 0) {
              assert(fora-step-1 < MAXK);
              chmax(dp[i+1][fora - step - 1][1], dp[i][j][k] + g);
            }
          }

        }
      }
    }

    int ans = 0; 
    REP(j, MAXK) chmax(ans, dp[n][j][0]);
    REP(j, MAXK) chmax(ans, dp[n][j][1]);
    printf("Case #%d: %d\n", tc+1, ans);
    fflush(stdout);
  }
  return 0;
}
