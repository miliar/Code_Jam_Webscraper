#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

typedef long long ll;
const int MAXN = 210;

double dp[MAXN][MAXN];
int T, N, K;
double A[MAXN];

int main() {
  scanf("%d", &T);
  REP(t,T) {
    REP(k, MAXN) REP(i, MAXN) {
      dp[k][i] = 0;
    }
    scanf("%d%d", &N, &K);
    REP(i,N) scanf("%lf", A+i);
    double best = 0;
    REP(mask, 1<<N) {
      dp[0][0] = 1;
      FOR(i,1,MAXN-1) dp[0][i] = 0;
      int k = 1;
      REP(n,N) if (mask & (1 << n)) {
        dp[k][0] = (1 - A[n]) * dp[k-1][0];
        FOR(i, 1, MAXN-1) {
          dp[k][i] = A[n] * dp[k-1][i-1] + (1-A[n]) * dp[k-1][i];
        }
        ++k;
      }
      if (k != K+1) continue;
      best = max(best, dp[K][K/2]);
    }
    printf("Case #%d: %lf\n", t+1, best);
  }
  return 0;
}
