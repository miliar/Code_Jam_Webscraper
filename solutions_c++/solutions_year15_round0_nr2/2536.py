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

int ans;
std::set<std::pair<std::vector<int>, int>> cache;
void check(const std::vector<int> &v, int t, int to) {
  if (t > to) {
    return;
  }

  // special time
  auto max = *std::max_element(std::begin(v), std::end(v));
  ans = std::min(ans, t + max);
  if (max == 1) {
    return;
  }
  for (int i = 0; i < (int)v.size(); ++i) {
    if (v[i] != max) {
      continue;
    }
    for (int n = 2; n <= v[i] / 2; ++n) {
      auto m = v[i] - n;
      auto nv = v;
      nv[i] = n;
      nv.push_back(m);
      check(nv, t + 1, to);
    }
  }
}

int main() {
  int Tests;
  std::cin >> Tests;
  for (int test = 1; test <= Tests; ++test) {
    int D;
    std::cin >> D;
    auto v = std::vector<int>(D);
    for (int i = 0; i < D; ++i) {
      std::cin >> v[i];
    }
    auto to = *std::max_element(std::begin(v), std::end(v));
    ans = INF;
    check(v, 0, to);
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
