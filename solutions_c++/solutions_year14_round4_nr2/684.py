#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

int T, n;
int a[1005], b[1005], pos[1005], dp[1005];

int main() {
  scanf("%d", &T);
  for (int it = 1; it <= T; it++) {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
      b[i] = a[i];
    }
    sort(b, b + n);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) if (b[i] == a[j]) pos[i] = j;

  /* for (int i = 0; i < n; i++)
    for (int j = i; j < n; j++) dp[i][j] = 1 << 28;
  for (int i = 0; i < n; i++) dp[i][i] = abs(pos[n - 1] - i);
  for (int w = 2; w <= n; w++)
    for (int x = 0; x + w <= n; x++) {
      int y = x + w - 1, cnt = n - w;
      // two ways to calc dp[x][y]
      dp[x][y] = min(dp[x + 1][y] + abs(pos[cnt] - x), dp[x][y - 1] + abs(pos[cnt] - y));
      // cout << x << ' ' << y << ' ' << dp[x][y] << endl;
    }*/

    dp[n - 1] = 0;
    for (int i = n - 2; i >= 0; i--) {
    	dp[i] = dp[i + 1];
	int lcnt = 0, rcnt = 0;
	for (int j = i + 1; j < n; j++)
	  if (pos[i] < pos[j]) lcnt++; else rcnt++;
	dp[i] += min(lcnt, rcnt);
    }

    printf("Case #%d: %d\n", it, dp[0]);
  }
}
