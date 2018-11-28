#include <algorithm>
#include <iostream>
#include <string>

std::string dp[1111][2];

int main() {
  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    std::string S;
    std::cin >> S;

    dp[0][0] = dp[0][1] = "";

    for (size_t i = 0; S[i]; ++i) {
      dp[i + 1][0] = std::max(dp[i][0], dp[i][1]) + S[i];
      dp[i + 1][1] = S[i] + std::max(dp[i][0], dp[i][1]);    
    }

    std::cout << "Case #" << t << ": " << std::max(dp[S.length()][0], dp[S.length()][1]) << "\n";
  }
  return 0;
}
