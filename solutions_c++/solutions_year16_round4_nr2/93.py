/* Written by Filip Hlasek 2016 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MAXN 222
int N, K;
double P[MAXN];

long double dp[MAXN][MAXN];

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(testcase, 1, T) {
    scanf("%d%d", &N, &K);
    REP(i, N) scanf("%lf", P + i);

    sort(P, P + N);
    long double ans = 0;
    REP(k, K + 1) {
      vector<long double> p;
      REP(j, k) p.push_back(P[j]);
      REP(j, K - k) p.push_back(P[N - j - 1]);

      REP(i, K + 1) REP(j, K + 1) dp[i][j] = 0;
      dp[0][0] = 1;
      REP(n, K) REP(k, K + 1) {
        dp[n + 1][k + 1] += p[n] * dp[n][k];
        dp[n + 1][k] += (1 - p[n]) * dp[n][k];
      }
      ans = max(ans, dp[K][K/2]);
    }

    printf("Case #%d: %.9Lf\n", testcase, ans);
  }
  return 0;
}
