#include <algorithm>
#include <cmath>
#include <complex>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

const int DX[] = {-1, 1, 0, 0};
const int DY[] = {0, 0, -1, 1};

bool FindArrow(int r, int c, const std::vector<std::string>& map, int x, int y, int d) {
  while (true) {
    x += DX[d];
    y += DY[d];
    if (0 <= x && x < r && 0 <= y && y < c) {
      if (map[x][y] != '.') {
        return true;
      }
    } else {
      break;
    }
  }
  return false;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    // Input
    int r, c;
    std::cin >> r >> c;
    std::vector<std::string> map;
    for (int j = 0; j < r; j++) {
      std::string row;
      std::cin >> row;
      map.push_back(row);
    }
    // Solve
    int y = 0;
    bool success = true;
    for (int j = 0; j < r; j++) {
      for (int k = 0; k < c; k++) {
        if (map[j][k] == '.') {
          continue;
        }
        int d = -1;
        switch (map[j][k]) {
        case '^':
          d = 0;
          break;
        case 'v':
          d = 1;
          break;
        case '<':
          d = 2;
          break;
        case '>':
          d = 3;
          break;
        }
        if (FindArrow(r, c, map, j, k, d)) {
          continue;
        }
        bool found = false;
        for (int nd = 0; nd < 4; nd++) {
          if (nd != d && FindArrow(r, c, map, j, k, nd)) {
            found = true;
            break;
          }
        }
        if (!found) {
          success = false;
          break;
        }
        y++;
      }
      if (!success) {
        break;
      }
    }
    // Output
    std::cout << "Case #" << i + 1 << ": ";
    if (success) {
      std::cout << y;
    } else {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
}
