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
static const int INF = std::numeric_limits<int>::max();

int dx[] = {
  0, 1, 0, -1, 1, 1, -1, -1
};
int dy[] = {
  1, 0, -1, 0, 1, -1, 1, -1
};

int ans_r, ans_c;

bool check(std::vector<int> v, int R, int C, int M)
{
  for(int r = 0; r < R; ++r) {
    for(int c = 0; c < C; ++c) {
      if(v[r * C + c] != 0) {
        continue;
      }
      int f = 0;
      for(int i = 0; i < 8; ++i) {
        auto nr = r + dx[i], nc = c + dy[i];

        if(nr < 0 || nr >= R || nc < 0 || nc >= C) {
          continue;
        }

        auto k = nr * C + nc;
        if(v[k] == 1) {
          f = 2;
        }
      }
      v[r * C + c] = f;
    }
  }

  for(int r = 0; r < R; ++r) {
    for(int c = 0; c < C; ++c) {
      auto k = r * C + c;

      if(v[k] == 1) {
        continue;
      }

      std::vector<int> visited(R * C);
      std::queue<std::pair<int, int>> q;
      q.emplace(r, c);
      visited[r * C + c] = 1;

      while(!q.empty()) {
        auto top = q.front();
        q.pop();

        auto x = top.first;
        auto y = top.second;

        if(v[x * C + y] != 0) {
          continue;
        }

        for(int i = 0; i < 8; ++i) {
          auto nx = x + dx[i], ny = y + dy[i];
          if(nx < 0 || nx >= R || ny < 0 || ny >= C) {
            continue;
          }
          auto k = nx * C + ny;
          if(v[k] == 1 || visited[k] != 0) {
            continue;
          }
          visited[k] = 1;
          q.emplace(nx, ny);
        }
      }

      if(std::count(std::begin(visited), std::end(visited), 1) == R * C - M) {
        ans_r = r;
        ans_c = c;
        return true;
      } else {
        return false;
      }
    }
  }
  return false;
}

int main()
{
  int T;

  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int R, C, M;
    std::cin >> R >> C >> M;

    std::vector<int> v(R*C, 1);

    std::fill(std::begin(v), std::begin(v) + R * C - M, 0);

    bool success = false;
    do {
      if(check(v, R, C, M)) {
        success = true;
        break;
      }
    } while(std::next_permutation(std::begin(v), std::end(v)));
    std::cout << "Case #" << test << ":\n";
    if(success) {
      for(int i = 0; i < R; ++i) {
        for(int j = 0; j < C; ++j) {
          auto k = i * C + j;
          if(v[k] != 1) {
            if(i == ans_r && j == ans_c) {
              std::cout << "c";
            } else {
              std::cout << ".";
            }
          } else {
            std::cout << "*";
          }
        }
        std::cout << std::endl;
      }
    } else {
      std::cout << "Impossible" << std::endl;
    }
  }
}
