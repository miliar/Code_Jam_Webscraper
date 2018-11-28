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
#include <array>
static const int INF = std::numeric_limits<int>::max();

std::array<int, 4> dx{{1, 0, -1, 0}};
std::array<int, 4> dy{{0, 1, 0, -1}};

int X;
std::array<bool, 1 << 16> memo;

bool visited(int state, int x, int y, int R, int C) {
  return state & (1 << (x * C + y));
}
int visit(int state, int x, int y, int R, int C) {
  return state | (1 << (x * C + y));
}

void print(int state, int R, int C) {
  std::cout << ":state:" << state << std::endl;
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (visited(state, i, j, R, C)) {
        std::cout << "*";
      } else {
        std::cout << ".";
      }
    }
    std::cout << std::endl;
  }
}

bool dfs(int state, int R, int C);

bool go(int state, int bstate, int left, int R, int C) {
  if (left == 0) {
    //    print(state, R, C);
    return dfs(state, R, C);
  }
  for (int x = 0; x < R; ++x) {
    for (int y = 0; y < C; ++y) {
      if (!visited(bstate, x, y, R, C)) {
        continue;
      }
      for (int i = 0; i < 4; ++i) {
        auto nx = x + dx[i];
        auto ny = y + dy[i];
        if (nx < 0 || nx >= R || ny < 0 || ny >= C ||
            visited(state, nx, ny, R, C)) {
          continue;
        }
        auto nstate = visit(state, nx, ny, R, C);
        auto nbstate = visit(bstate, nx, ny, R, C);
        //    std::cout << "visit " << nx << "," << ny << std::endl;
        if (go(nstate, nbstate, left - 1, R, C)) {
          return true;
        }
      }
    }
  }
  return false;
}

bool dfs(int state, int R, int C) {
  // std::cout << "dfs" << std::endl;
  // print(state, R, C);
  if (state == (1 << R * C) - 1) {
    return true;
  }
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      if (visited(state, i, j, R, C)) {
        continue;
      }
      return go(visit(state, i, j, R, C), visit(0, i, j, R, C), X - 1, R, C);
    }
  }
  assert(0);
}

auto p = std::vector<std::vector<std::vector<std::string>>>{
    {{"*"}},
    {
     {"**"},
    },
    {
     {"***"}, {"**.", "*.."},
    },
    {{"****"}, {"***", "*.."}, {"***", ".*."}, {"**.", ".**"}, {"**", "**"}}};

int setstate(const std::vector<std::string> &a, int x, int y, int R, int C) {
  if (x + a.size() > R) {
    return 0;
  }
  if (y + a[0].size() > C) {
    return 0;
  }
  int state = 0;
  for (int i = 0; i < (int)a.size(); ++i) {
    for (int j = 0; j < (int)a[0].size(); ++j) {
      if (a[i][j] == '.') {
        continue;
      }
      state = visit(state, i + x, j + y, R, C);
    }
  }
  return state;
}

bool put(const std::vector<std::string> &a, int R, int C) {
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      auto state = setstate(a, i, j, R, C);
      if (state == 0) {
        continue;
      }
      if (dfs(state, R, C)) {
        return true;
      }
    }
  }
  return false;
}

bool check(int R, int C) {
  auto &q = p[X - 1];
  for (auto &a : q) {
    if (!put(a, R, C) && !put(a, C, R)) {
      // for (auto &s : a) {
      //   std::cout << s << std::endl;
      // }
      return false;
    }
  }
  return true;
}

int main() {
  int Tests;
  std::cin >> Tests;
  for (int test = 1; test <= Tests; ++test) {
    int R, C;
    std::cin >> X >> R >> C;
    auto ans = "RICHARD";

    std::fill(std::begin(memo), std::end(memo), 0);
    if (check(R, C)) {
      ans = "GABRIEL";
    }

    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
