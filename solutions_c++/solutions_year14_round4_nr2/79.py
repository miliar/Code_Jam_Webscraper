/* Written by Filip Hlasek 2014 */
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

#define MAXN 1111
int A[MAXN], N, rank[MAXN];
vector<pair<int, int> > v;

int dp[MAXN][MAXN];
int solve(int left, int right) {
  if (left + right == N) return 0;
  if (dp[left][right] != -1) return dp[left][right];
  int n = left + right;
  dp[left][right] = min(solve(left + 1, right) + rank[v[n].second],
                        solve(left, right + 1) + (N - (left + right) - 1) - rank[v[n].second]);
  // printf("left: %d right: %d ans: %d pos: %d rank: %d\n", left, right, dp[left][right], v[n].second, rank[v[n].second]);
  return dp[left][right];
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  REP(t, T) {
    scanf("%d", &N);
    REP(i, N) scanf("%d", A + i);
    REP(i, N) {
      rank[i] = 0;
      REP(j, i) rank[i] += A[j] > A[i];
    }
    v.clear();
    REP(i, N) v.push_back(make_pair(A[i], i));
    sort(v.begin(), v.end());
    REP(i, N) REP(j, N) dp[i][j] = -1;
    printf("Case #%d: %d\n", t + 1, solve(0, 0));
  }
  return 0;
}
