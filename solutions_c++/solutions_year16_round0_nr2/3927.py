#include <iostream>
#include <string>

using namespace std;

const int MAXN = 128;

int N;
string pancakes;

int dp[MAXN][2];

int main() {
   dp[1][0] = 1;
   dp[1][1] = 0;
   for(int i = 2 ; i < MAXN ; i++) {
      dp[i][0] = dp[i - 1][1] + 1;
      dp[i][1] = dp[i - 1][0] + 1;
      if (i & 1) {
         dp[i][0] = min(dp[i][0], dp[i][1] + 1);
         dp[i][1] = min(dp[i][1], dp[i][0] + 1);
         dp[i][0] = min(dp[i][0], dp[i][1] + 1);
      }
   }

   cin >> N;
   for(int t = 1 ; t <= N ; t++) {
      cin >> pancakes;
      int p = (pancakes[0] == '+' ? 1 : 0);
      int tot = 1;
      for (int j = 1 ; j < (int)pancakes.size() ; j++) {
         if (pancakes[j] != pancakes[j - 1]) {
            tot += 1;
         }
      }
      printf("Case #%d: %d\n", t, dp[tot][p]);
   }

   return 0;
}
