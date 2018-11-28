#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

long double solve_slow(int n, int k, std::vector<long double>& probabilities) {

}

long double solve(int n, int k, std::vector<long double>& probabilities) {
  std::vector<std::vector<std::vector<long double>>>
    k_prob(n + 2, std::vector<std::vector<long double>>(n + 2,
          std::vector<long double>(k + 1, 0)));
  k_prob[0][n + 1][0] = 1;
  long double answer = 0;
  for (int i = 0; i <= n; ++i) {
    for (int j = n + 1; j > i; --j) {
      for (int yes = 0; yes <= i + (n + 1 - j) && yes <= k; ++yes) {
        if (i > 0) {
          k_prob[i][j][yes] = 
              k_prob[i - 1][j][yes] * (1 - probabilities[i]) +
              (yes > 0 ? k_prob[i - 1][j][yes - 1] * probabilities[i] : 0);
        } else if (j < n + 1) {
          k_prob[i][j][yes] = 
              k_prob[i][j + 1][yes] * (1 - probabilities[j]) +
              (yes > 0 ? k_prob[i][j + 1][yes - 1] * probabilities[j] : 0);
        }
        if (yes == k / 2 && (i + (n + 1 - j)) == k) {
          answer = std::max(answer, k_prob[i][j][yes]);
        }
      }
    }
  }
  //for (auto& v : k_prob) {
    //for (auto& w : v) {
      //for (auto& c : w) {
        //std::cout << c << ' ';
      //}
      //std::cout << std::endl;
    //}
    //std::cout << "=====" << std::endl;
  //}
  return answer;
}

int main() {
  int number_of_tests = 0;
  std::cin >> number_of_tests;
  std::cout.precision(15);
  for (int test_index = 0; test_index < number_of_tests; ++test_index) {
    int n, k;
    std::cin >> n >> k;
    std::vector<long double> probabilities(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      std::cin >> probabilities[i + 1];
    }
    std::sort(probabilities.begin(), probabilities.end());
    std::cout << "Case #" << test_index + 1 << ": " << std::fixed <<
      solve(n, k, probabilities) << std::endl;
  }
  return 0;
}
