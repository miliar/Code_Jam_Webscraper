#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

double solveDp(const vector<double> &p) {
  const int n = int(p.size());
  vector<vector<double>> dp = vector<vector<double>>(n + 1, vector<double>(n + 1, 0.0));
  dp[0][0] = 1.0;
  for (int i = 1; i <= n; ++i) {
    dp[i][0] = (1.0 - p[i - 1]) * dp[i - 1][0];
    dp[i][i] = p[i - 1] * dp[i - 1][i - 1];
    for (int j = 1; j < i; ++j)
      dp[i][j] = (1.0 - p[i - 1]) * dp[i - 1][j] + p[i - 1] * dp[i - 1][j - 1];
  }
  return dp[n][n / 2];
}

inline int getBit(const int mask, const int bit) {
  return (mask >> bit) & 1;
}

int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int testCount;
  in >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int N, K;
    in >> N >> K;
    vector<double> P = vector<double>(N);
    for (int i = 0; i < N; ++i)
      in >> P[i];
    double maxP = 0.0;
    for (int mask = 0; mask < (1 << N); ++mask) {
      vector<double> currentP;
      for (int i = 0; i < N; ++i)
        if (getBit(mask, i) == 1)
          currentP.push_back(P[i]);
      if (int(currentP.size()) == K)
        maxP = max(maxP, solveDp(currentP));
    }
    out << "Case #" << test << ": " << fixed << setprecision(9) << maxP << "\n";
  }
  in.close();
  out.close();
  return 0;
}
