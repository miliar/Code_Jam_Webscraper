#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

int dp[1002][1002];

void doTest() {
  int n;
  scanf("%d", &n);
  vector<int> v(n, 0);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &v[i]);
  }
  vector<int> left(n, 0), right(n, 0);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < i; ++j) {
      if (v[j] > v[i]) ++left[i];
    }
    for (int j = i + 1; j < n; ++j) {
      if (v[j] > v[i]) ++right[i];
    }
  }
  vector<int> s = v;
  sort(s.begin(), s.end());
  vector<int> wh(n, -1);
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      if (s[i] == v[j])
        wh[i] = j;

  for (int i = 0; i <= n; ++i)
    for (int j = 0; j <= n; ++j)
      dp[i][j] = n * n + n;
  dp[0][0] = 0;
  for (int i = 0; i < n; ++i) {
    for (int l = 0; l < n; ++l) {
      if (dp[i][l] > n * n) continue;
      int pos = wh[i];
      dp[i + 1][l] = min(dp[i + 1][l], dp[i][l] + right[pos]);
      dp[i + 1][l + 1] = min(dp[i + 1][l + 1], dp[i][l] + left[pos]);
    }
  }
  int ans = n * n + n;
  for (int i = 0; i <= n; ++i) {
    ans = min(ans, dp[n][i]);
  }
  printf("%d\n", ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    doTest();
  }
  return 0;
}