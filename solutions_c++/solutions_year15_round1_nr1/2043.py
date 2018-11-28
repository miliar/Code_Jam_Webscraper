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

int solve1(const std::vector<int> &v) {
  int res = 0;
  for (int i = 0; i < (int)v.size() - 1; ++i) {
    auto d = v[i] - v[i + 1];
    if (d > 0) {
      res += d;
    }
  }
  return res;
}

int solve2(const std::vector<int> &v) {
  int res = INF;
  int left = -1, right = 10001;
  while(right - left > 1) {
    auto b = (right + left) / 2;
    int ans = 0;
    for (int i = 0; i < (int)v.size() - 1; ++i) {
      auto d = v[i] - v[i + 1];
      if (d >= 0 && b < d) {
        ans = -1;
        break;
      }
      ans += std::min(v[i], b);
    }
    if (ans != -1) {
      right = b;
      res = std::min(res, ans);
    } else {
      left = b;
    }
  }
  return res;
}

int main() {
  int Tests;
  std::cin >> Tests;
  for (int test = 1; test <= Tests; ++test) {
    int N;
    std::cin >> N;
    auto v = std::vector<int>(N);
    for (int i = 0; i < N; ++i) {
      std::cin >> v[i];
    }
    auto ans1 = solve1(v);
    auto ans2 = solve2(v);
    std::cout << "Case #" << test << ": " << ans1 << " " << ans2 << std::endl;
  }
}
