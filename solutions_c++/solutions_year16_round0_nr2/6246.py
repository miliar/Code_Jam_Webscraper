#include <iostream>
#include <cstdio>
#include <cstring>
#include <unordered_map>
using namespace std;
const int MAXN = 123;

int mp[12345];
char str[MAXN];

int reverse(int x, int len) {
  int y = 0;
  for (int i = 0; i < len; ++i) {
    if (!((x >> i) & 1)) {
      y |= (1 << (len - i - 1));
    }
  }
  return y;
}

int cutAndReverse(int x, int pos, int len) {
  int first = x >> (len - 1 - pos);
  int second = x - (first << (len - 1 - pos));
  first = reverse(first, pos + 1);
  return (first << (len - 1 - pos)) + second;
}

void dfs(int currentState, int currentStep, int len, int mp[]) {
  if (mp[currentState] != -1 && currentStep >= mp[currentState]) {
    return;
  }
  mp[currentState] = currentStep;
  for (int i = 0; i < len; ++i) {
    dfs(cutAndReverse(currentState, i, len), currentStep + 1, len, mp);
  }
}

int dp[MAXN][2];

int main() {
  int cases = 0;
  scanf("%d", &cases);
  gets(str);
  for (int T = 1; T <= cases; ++T) {
    gets(str);
    int len = strlen(str);
    int initialState = 0;
    for (int i = 0; i < len; ++i) {
      if (str[i] == '+') {
        initialState |= 1 << (len - 1 -i);
      }
    }
    dp[0][0] = str[0] == '-' ? 0 : 1;
    dp[0][1] = str[0] == '-' ? 1 : 0;
    for (int i = 1; i < len; ++i) {
      if (str[i] == '-') {
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + 1);
        dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1] + 2);
      } else {
        dp[i][0] = min(dp[i - 1][1] + 1, dp[i - 1][0] + 2);
        dp[i][1] = min(dp[i - 1][1], dp[i - 1][0] + 1);
      }
    }
    memset(mp, -1, sizeof(mp));
    // dfs(initialState, 0, len, mp);
    // printf("Case #%d: %d %d\n", T, mp[(1 << len) - 1], dp[len - 1][1]);
    printf("Case #%d: %d\n", T, dp[len - 1][1]);
  }
}
