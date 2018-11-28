#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
#include <map>
static const int INF = std::numeric_limits<int>::max();

int K, L, S;
std::string KEYS, TARGET;
int max;
double ans;
double P;

int count(const std::string &s) {
  int res = 0;
  for (size_t i = 0; i + TARGET.size() <= s.size(); ++i) {
    if (std::equal(std::begin(TARGET), std::end(TARGET), std::begin(s) + i)) {
      ++res;
    }
  }
  return res;
}

void recur(const std::string &s, double p) {
  if (s.size() == S) {
    auto cnt = count(s);
    max = std::max(max, cnt);
    ans += p * cnt;
    return;
  }
  for (auto c : KEYS) {
    recur(s + c, p * P);
  }
}

int main() {
  int Tests;
  std::cin >> Tests;
  for (int test = 1; test <= Tests; ++test) {
    std::cin >> K >> L >> S >> KEYS >> TARGET;
    ans = 0;
    max = 0;
    P = 1.0 / KEYS.size();

    recur("", 1);

    std::cout << "Case #" << test << ": " << std::fixed << std::setprecision(9)
              << max - ans << std::endl;
  }
}
