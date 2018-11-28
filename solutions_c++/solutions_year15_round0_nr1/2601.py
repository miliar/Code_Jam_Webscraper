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

int main() {
  int Tests;
  std::cin >> Tests;
  for (int test = 1; test <= Tests; ++test) {
    int Smax;
    std::string s;
    std::cin >> Smax >> s;
    int ans = 0;
    int sum = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
      auto a = s[i] - '0';
      auto d = std::max(0, i - sum);
      ans += d;
      sum += a + d;
    }
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
