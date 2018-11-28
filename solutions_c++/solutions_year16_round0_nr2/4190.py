#include <cstdio>
#include <cstring>
using namespace std;

char str[200];
int dp[200][200][2];

int main() {
  int T;
  scanf("%d", &T);
  for (int I = 1; I <= T; ++I) {
    scanf("%s", str);
    memset(dp, sizeof(dp), 0);
    int len = strlen(str);
    for (int i = 0; i < len; ++i) {
      if (str[i] == '+') {
        dp[i][i][0] = 0;
        dp[i][i][1] = 1;
      } else {
        dp[i][i][0] = 1;
        dp[i][i][1] = 0;
      }
    }
    
    for (int l = 1; l < len; ++l) {
      for (int i = 0; i + l < len; ++i) {
        dp[i][i + l][1] = -1;
        if (dp[i][i][1] == 0 && dp[i + 1][i + l][1] == 0) dp[i][i + l][1] = 0;
        for (int j = i; j < i + l; ++j) {
          int tmp = dp[i][j][0] + dp[j + 1][i + l][1] + 1;
          if (dp[i][i + l][1] == -1 || tmp < dp[i][i + l][1])
            dp[i][i + l][1] = tmp;
        }
        
        dp[i][i + l][0] = dp[i][i + l][1] + 1;
        if (dp[i][i][0] == 0 && dp[i + 1][i + l][0] == 0) dp[i][i + l][0] = 0;
        for (int j = i; j < i + l; ++j) {
          int tmp = dp[i][j][1] + dp[j + 1][i + l][0] + 1;
          if (tmp < dp[i][i + l][0])
            dp[i][i + l][0] = tmp;
        }
      }
    }

    
    // for (int i = 0; i < len; ++i) {
    //   for (int j = i; j < len; ++j) {
    //     printf(" (%d, %d)", dp[i][j][0], dp[i][j][1]);
    //   }
    //   printf("\n");
    // }
    printf("Case #%d: %d\n", I, dp[0][len - 1][0]);
  }
}
