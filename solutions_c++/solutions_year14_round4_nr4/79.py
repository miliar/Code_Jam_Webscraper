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
#define MAXL 111
int N, M, s[MAXN];
char S[MAXN][MAXL];

int count(int mask) {
  int ans = 1;
  REP(i, M) if (mask & (1 << i)) {
    int len = 0;
    REP(j, i) if (mask & (1 << j)) {
      int common = 0;
      while (common < s[i] && common < s[j] && S[i][common] == S[j][common]) common++;
      len = max(len, common);
    }
    ans += s[i] - len;
  }
  return ans;
}

pair<int, int> solve(int n, int mask) {
  if (n == N) {
    if (mask != (1 << M) - 1) return make_pair(-1000000000, 0);
    return make_pair(0, 1);
  }
  int best = -1, ways = 0;
  REP(submask, 1 << M) if (submask && (mask & submask) == 0) {
    pair<int, int> ans = solve(n + 1, mask | submask);
    int val = ans.first + count(submask);
    if (val > best) { best = val; ways = 0; }
    if (val == best) ways += ans.second;
  }
  return make_pair(best, ways);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  REP(t, T) {
    scanf("%d%d", &M, &N);
    REP(i, M) scanf("%s", S[i]);
    REP(i, M) s[i] = strlen(S[i]);
    pair<int, int> ans = solve(0, 0);
    printf("Case #%d: %d %d\n", t + 1, ans.first, ans.second);
  }

  return 0;
}
