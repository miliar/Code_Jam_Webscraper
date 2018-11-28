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

enum {
  ONE = 1,
  I,
  J,
  K,
};

int ch(char c) {
  switch (c) {
  case 'i':
    return I;
  case 'j':
    return J;
  case 'k':
    return K;
  default:
    assert(0);
  }
}

int op(int x, int y) {
  auto sign = x * y > 0 ? 1 : -1;
  x = abs(x);
  y = abs(y);
  if (x == ONE) {
    return sign * y;
  }
  if (y == ONE) {
    return sign * x;
  }
  switch(x) {
  case I:
    switch (y) {
    case I:
      return -ONE * sign;
    case J:
      return K * sign;
    case K:
      return -J * sign;
    default:
      assert(0);
    }
  case J:
    switch (y) {
    case I:
      return -K * sign;
    case J:
      return -ONE * sign;
    case K:
      return I * sign;
    default:
      assert(0);
    }
  case K:
    switch (y) {
    case I:
      return J * sign;
    case J:
      return -I * sign;
    case K:
      return -ONE * sign;
    default:
      assert(0);
    }
  default:
    assert(0);
  }
}

int main() {
  int Tests;
  std::cin >> Tests;
  for (int test = 1; test <= Tests; ++test) {
    int L, X;
    std::string S;
    std::cin >> L >> X >> S;
    std::string s;
    for (int i = 0; i < X; ++i) {
      s += S;
    }
    int a = ONE;
    for (auto b : s) {
      a = op(a, ch(b));
    }
    std::string ans = "NO";
    if (a == -1) {
      int x = ONE;
      int z = ONE;
      std::vector<int> xi;
      for (int i = 0; i < (int)s.size() - 2; ++i) {
        x = op(x, ch(s[i]));
        if (x == I) {
          xi.push_back(i + 1);
        }
      }
      std::vector<int> zi;
      for (int i = (int)s.size() - 1; i >= 2; --i) {
        z = op(ch(s[i]), z);
        if (z == K) {
          zi.push_back(i);
        }
      }
      for (auto first : xi) {
        for (auto last : zi) {
          int y = ONE;
          for (int i = first; i < last; ++i) {
            y = op(y, ch(s[i]));
          }
          if (y == J) {
            ans = "YES";
            goto done;
          }
        }
      }
    }
  done:
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
