#include<cstdio>
#include<deque>
#include<queue>
#include<stack>
#include<vector>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<bitset>
#include<list>
#include<set>
#include<map>

using namespace std;

const int N = 110;

char s[N];

int dp[N][2];

int main() {
  freopen("Blarge.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int test;
  scanf("%d", &test);
  for(int t = 1; t <= test; t++) {
    scanf("%s", s);
    int len = strlen(s);
    for(int i = 0; i < len; i++) {
      if(i == 0) {
        if(s[i] == '-') {
          dp[i][0] = 0;
          dp[i][1] = 1;
        } else {
          dp[i][0] = 1;
          dp[i][1] = 0;
        }
      } else {
        if(s[i] == '+') {
          dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1]);
          dp[i][0] = dp[i - 1][1] + 1;
        } else {
          dp[i][1] = dp[i - 1][0] + 1;
          dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + 1);
        }
      }
    }
    int ans = min(dp[len - 1][1], dp[len - 1][0] + 1);
    printf("Case #%d: %d\n", t, ans);
  }
}

