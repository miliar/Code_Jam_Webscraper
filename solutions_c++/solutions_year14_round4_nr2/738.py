#include <assert.h>
#include <ctype.h>
#include <float.h>
#include <limits.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include <algorithm>
#include <complex>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define CLR(c,n) memset(c, n, sizeof(c))
#define TR(it, c) for(typeof(c.begin()) it = c.begin();it != c.end(); ++it)
#define CONTAIN(it, c) (c.find(it) != c.end())
typedef vector<int> VI;
typedef pair<int, int> PII;
template <class T> void checkmin(T &a, T b) { if (b<a) a=b; }
template <class T> void checkmax(T &a, T b) { if (b>a) a=b; }

#define N 1024
const int INF=0x3F3F3F3F;
int n;
PII a[N];
int dp[N][N];
int status[N][N][N];
void work(int idx) {
  scanf("%d", &n);
  REP(i, n) scanf("%d", &a[i].first), a[i].second = i;
  sort(a, a+n);
  CLR(dp, INF);
  int ans = INF;
  dp[0][0] = n-1-a[0].second;
  dp[0][1] = a[0].second;
  //    REP(i, n) printf("%d %d\n", a[i].first, a[i].second);
  REP(i, n-1) {
    REP(j, n) if (dp[i][j] != INF) {
      //      printf("%d %d %d\n", i, j, dp[i][j]);
      int first = j, last = n - 2 - i + j;
      ans = dp[i][j];
      for (int k = i + 2; k < n; ++k) if (a[k].second > a[i+1].second) ++ans;
      checkmin(dp[i+1][j], ans);
      ans = dp[i][j];
      for (int k = i + 2; k < n; ++k) if (a[k].second < a[i+1].second) ++ans;
      checkmin(dp[i+1][j+1], ans);
    }
  }
  ans = INF;
  REP(i, n) checkmin(ans, dp[n-1][i]);
  printf("Case #%d: %d\n", idx, ans);
  /*
  REP(i, n) dp[n-1][i] = abs(a[n-1].second - i);
  for (int i = n - 1; i > 0; --i) {
    REP(j, n) if (dp[i][j] != INF) {
      int prev = j - 1, next = j + n - i;
      if (prev >= 0) checkmin(dp[i-1][prev], dp[i][j] + abs(a[i-1].second - prev));
      if (next < n) checkmin(dp[i-1][j], dp[i][j] + abs(a[i-1].second - next));
    }
  }
  printf("Case #%d: %d\n", idx, dp[0][0]/2);
  */
}
int main(int argc, char *argv[]) {
  int tc;
  scanf("%d", &tc);
  FOR(i, 1, tc) work(i);
}
