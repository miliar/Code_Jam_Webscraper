#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char IN_FILE[] = "input.txt";
const char OUT_FILE[] = "output.txt";
const int oo = 0x3f3f3f3f;

int solveDp(const vector<int> &values) {
  int n = int(values.size());
  auto dp = vector<vector<vector<int>>>(n, vector<vector<int>>(n, vector<int>(2, oo)));
  for (int i = 0; i < n; ++i) {
    dp[i][i][values[i]] = 0;
    dp[i][i][values[i] ^ 1] = 1;
  }
  for (int l = 2; l <= n; ++l) {
    for (int i = 0, j = l - 1; j < n; ++i, ++j) {
      int count[2] = {0, 0};
      for (int k = i; k <= j; ++k)
        ++count[values[k]];
      if (count[0] == 0) {
        dp[i][j][0] = dp[j][i][0] = 1;
        dp[i][j][1] = dp[j][i][1] = 0;
        continue;
      } else if (count[1] == 0) {
        dp[i][j][0] = dp[j][i][0] = 0;
        dp[i][j][1] = dp[j][i][1] = 1;
        continue;
      }
      for (int v = 0; v <= 1; ++v) {
        if (values[j] == v)
          dp[i][j][v] = min(dp[i][j][v], dp[i][j - 1][v]);
        if (values[i] == v)
          dp[j][i][v] = min(dp[j][i][v], dp[j][i + 1][v]);
        for (int k = i; k < j; ++k) {
          dp[i][j][v] = min(dp[i][j][v], dp[i][k][v ^ 1] + 1 + dp[j][k + 1][v ^ 1]);
          dp[j][i][v] = min(dp[j][i][v], dp[j][k + 1][v ^ 1] + 1 + dp[i][k][v ^ 1]);
        }
      }
    }
  }
  return dp[0][n - 1][0];
}

int main() {
  ifstream cin(IN_FILE);
  ofstream cout(OUT_FILE);

  int testCount;
  cin >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    string S;
    cin >> S;
    vector<int> values = vector<int>(int(S.length()));
    for (int i = 0; i < int(S.length()); ++i) {
      if (S[i] == '+')
        values[i] = 0;
      else
        values[i] = 1;
    }
    cout << "Case #" << test << ": " << solveDp(values) << "\n";
  }

  cin.close();
  cout.close();
  return 0;
}
