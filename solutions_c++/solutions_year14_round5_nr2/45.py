#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

int n, p, q, h[100], g[100];

int dp[101][1500];

int main() {
  int Z;
  cin >> Z;
  for (int z=1;z<=Z;++z) {
    cin >> p >> q >> n;
    for (int i=0; i<n; ++i)
      cin >> h[i] >> g[i];
    for (int i=0; i<1500; ++i)
      dp[0][i] = -1e9;
    dp[0][1] = 0;
    for (int m=1;m<=n;++m) {
      int he_has_to = (h[m-1] + q - 1) / q - 1;
      int i_have_to = (h[m-1] - q * he_has_to + p - 1) / p;
      int off1 = he_has_to - i_have_to;
      int off2 = he_has_to + 1;
      for (int i=0; i<1500; ++i)
        dp[m][i] = -1e9;
      for (int i=0; i<1500; ++i) {
        if (i+off1 >= 0 && i+off1 < 1500)
          dp[m][i+off1] = max(dp[m][i+off1], dp[m-1][i] + g[m-1]);
        if (i+off2 >=0 && i+off2 < 1500)
          dp[m][i+off2] = max(dp[m][i+off2], dp[m-1][i]);
      }
      for (int i=1100;i<1500;++i)
        assert(dp[m][i] < 0);
    }
        
    int best=-1e9;
    for (int i=0; i<1500; ++i) best=max(best, dp[n][i]);
    assert(best >= 0);
    cout << "Case #" << z << ": " << best << endl;
  }
}
