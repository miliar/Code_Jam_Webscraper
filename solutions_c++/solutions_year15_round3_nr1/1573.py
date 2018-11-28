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
    int R, C, W;
    std::cin >> R >> C >> W;

    auto rem = C % W;
    auto spc = W - 1 + std::min(1, rem);
    auto ans = spc + C / W;
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
