#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long LL;

//*******************
const int INF = 2e9;
int dp[1001][1001];
int delays[1001][1001];

int solve() {
   int d;
   cin >> d;
   vector<int> h(d);
   for(int &hx : h)
      cin >> hx;
   sort(h.begin(), h.end());
   for(int i = 1; i <= d; ++i) {
      dp[i][0] = INF;
      for(int j = 1; j <= h[i-1]; ++j) {
         int local_res = j-1 + (h[i-1]+j-1) / j;
         delays[i][j] = j-1;
         int mink = 1;
         if(i == 1) 
            dp[i][j] = local_res;
         else {
            dp[i][j] = INF;
            for(int k = 1; dp[i-1][k] != INF; ++k) {
               int res = max(j-1 + dp[i-1][k], delays[i-1][k] + local_res);
               if(res < dp[i][j]) {
                  mink = k;
                  dp[i][j] = res;
                  delays[i][j] = j-1 + delays[i-1][k];
               }
            }
         }
         // cout << mink << " -> [" << i << ", " << j <<"] = " << dp[i][j] << endl;
         if(dp[i][j] >= dp[i][j-1]) {
            dp[i][j] = INF;
            break;
         }
      }
   }
   int result = INF;
   for(int j = 1; dp[d][j] != INF; ++j)
      result = min(result, dp[d][j]);
   return result;
}
//*******************

int main() {
   ios::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int i = 1; i <= T; ++i)
      cout << "Case #" << i << ": " << solve() << endl;
   return 0;
}