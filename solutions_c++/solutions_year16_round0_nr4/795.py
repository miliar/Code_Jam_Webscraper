#include <cstdio>

#include <iostream>
#include <vector>

using std::vector;

const int MAX_DIGITS = 1000 + 5;

long long toBase10(const vector<int>& digits, int base) {
  long long result = 0LL;
  for (int digit : digits) {
    result *= base;
    result += digit;
  }
  return result;
}

vector<long long> solve(int K, int C, int S) {
  int necessaryTiles = K / C;
  if (K % C != 0) {
    ++necessaryTiles;
  }
  if (necessaryTiles > S) {
    return {};
  }
  vector<int> digits(MAX_DIGITS);
  for (int i = 0; i < K; ++i) {
    digits[i] = i;
  }
  for (int i = K; i < digits.size(); ++i) {
    digits[i] = K - 1;
  }
  int currentStart = 0;
  vector<long long> result;
  for (int i = 0; i < necessaryTiles; ++i, currentStart += C) {
    vector<int> currentDigits(digits.begin() + currentStart, digits.begin() + currentStart + C);
    result.push_back(toBase10(currentDigits, K) + 1);
  }
  return result;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int K;
    int C;
    int S;
    scanf("%d %d %d", &K, &C, &S);
    auto res = solve(K, C, S);
    std::cout << "Case #" << t << ":";
    if (res.empty()) {
      std::cout << " IMPOSSIBLE\n";
    } else {
      for (long long tile : res) {
        std::cout << " " << tile;
      }
      std::cout << "\n";
    }
  }
}
