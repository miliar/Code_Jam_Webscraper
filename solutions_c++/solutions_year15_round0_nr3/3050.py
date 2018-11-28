/* Written by Filip Hlasek 2015 */
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

#define MAXN 1111111
char input[MAXN];
int N;

bool dp[MAXN][3][8];

const int table[4][4] = {
  {0, 2, 4, 6},
  {2, 1, 6, 5},
  {4, 7, 1, 2},
  {6, 4, 3, 1}
};

bool solve() {
  REP(i, N + 1) REP(j, 3) REP(k, 8) dp[i][j][k] = false;
  dp[0][0][0] = true;
  REP(i, N) REP(j, 3) REP(k, 8) if (dp[i][j][k]) {
    int l = 2 * (input[i] - 'i' + 1);
    int rem = (k % 2 + l % 2) % 2;
    int m = table[k / 2][l / 2];
    rem = (rem + m % 2) % 2;
    m = (m / 2) * 2 + rem;
    dp[i + 1][j][m] = true;
    if ((j == 0 && m == 2) || (j == 1 && m == 4)) dp[i + 1][j + 1][0] = true;
  }
  return dp[N][2][6];
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    int L, X;
    scanf("%d%d", &L, &X);
    scanf("%s", input);
    REP(i, X) REP(j, L) input[(i + 1) * L + j] = input[j];
    N = L * X;
    printf("Case #%d: ", t);
    if (solve()) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
