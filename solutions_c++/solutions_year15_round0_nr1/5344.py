#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int S_max;
    string S;
    cin >> S_max >> S;

    vector<int> dp(S_max + 1, 0);
    for (unsigned int i = 0; i < S.size(); ++i) {
      dp[i] = (S[i] - '0');
    }

    int ans = 0;
    for (unsigned int i = 1; i < S.size(); ++i) {
      if (i > dp[i-1] + ans) {
        int inv = i - (dp[i-1] + ans);
        ans += inv;
      }
      dp[i] += dp[i-1];
    }

    cout << "Case #" << testcase << ": " << ans << endl;
  }
}
