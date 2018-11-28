#include <stdio.h>
#include <iostream>
#include <string>
#include <queue>

using namespace std;
#define MAX_I 1005
int P[MAX_I];
int dp[MAX_I][MAX_I];
int main()
{
  int T;
  scanf("%d", &T);

  for (int i = 2; i < MAX_I; i++) {
    for (int j = 1; j < i; j++) {
      //      int value = (j == 1) ? MAX_I : dp[i][j-1];
            int value = MAX_I;
      for (int t = 1; t <= (i>>1); t++) {
        value = min(value, 1 + dp[i-t][j] + dp[t][j]);
      }
      dp[i][j] = value;
    }
    for (int j = i; j < MAX_I; j++) {
      dp[i][j] = 0;
    }
  }
  //  for (int i = 1; i < 10; i++) {
  //    for (int j = 1; j < 10; j++) {
  //      printf("dp[%d][%d] = %d%c", i, j, dp[i][j], (j==10) ? '\n' : ',');
  //    }
  //  }

  for (int i = 0; i < T; i++) {
    int D;
    scanf("%d", &D);
    int max_d = 0;
    for (int j = 0; j < D; j++) {
      scanf("%d", &P[j]);
      max_d = max(max_d, P[j]);
    }

    int ans = MAX_I;
    for (int j = 1; j <= max_d; j++) {
      int v = j;
      for (int k = 0; k < D; k++) {
        v += dp[P[k]][j];
      }
      ans = min(ans, v);
    }
    printf("Case #%d: %d\n", (i+1), ans);
  }
}
