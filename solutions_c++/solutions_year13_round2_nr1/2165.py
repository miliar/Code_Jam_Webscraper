#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <complex>
#include <algorithm>
using namespace std;

const int BUFFER_SIZE = 1 * 1024;
const double EPS      = 10e-6;
const int MAX         = 105;
const int MAX2        = 1000005;
const int INF         = 1 << 30;

int dp[MAX][MAX2];
int M[110], N;

int solve(int i, int a)
{
  if (i == N)
    return 0;

  int &ans = dp[i][a];

  if (ans != -1)
    return ans;

  if (a > M[i]) {
    ans = solve(i + 1, a + M[i]);
  } else {
    if (a > 1)
      ans = min(solve(i, a + a - 1), solve(i + 1, a)) + 1;
    else
      ans = solve(i + 1, a) + 1;
  }

  return ans;
}

int main(int argc, char *argv[])
{
  int T, tc, i, A; 

  scanf("%d", &T);
  for (tc = 1; tc <= T; tc++) {
    scanf("%d %d", &A, &N);
    for (i = 0; i < N; i++)
      scanf("%d", &M[i]);
    sort(M, M + N);


    memset(dp, -1, sizeof dp);
    printf("Case #%d: %d\n", tc, solve(0, A));
  }

  return EXIT_SUCCESS;
}

