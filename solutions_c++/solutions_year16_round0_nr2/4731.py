#include <cstdio>
#include <iostream>
#include <utility>
#include <cstring>

#define maxn 105
using namespace std;

char str[maxn];
pair<int, int> dp[maxn];
int main() {
  freopen("B-small-attempt.out", "w", stdout);
  int T, cas = 1;
  scanf("%d", &T);
  while(T--) {
    scanf("%s", str);
    dp[0].first = (str[0] == '+');
    dp[0].second = (str[0] == '-');
    int n = strlen(str);
    for(int i = 1; i < n; i++) {
      if (str[i] == '-') {
        dp[i].first = min(dp[i - 1].first, dp[i - 1].second + 1);
        dp[i].second = min(dp[i - 1].second + 2, dp[i - 1].first + 1);
      } else {
        dp[i].second = min(dp[i - 1].second, dp[i - 1].first + 1);
        dp[i].first = min(dp[i - 1].second + 1, dp[i - 1].first + 2);
      }
    }
    cout << "Case #" << cas++ << ": " << dp[n - 1].second << endl;
  }
  return 0;
}