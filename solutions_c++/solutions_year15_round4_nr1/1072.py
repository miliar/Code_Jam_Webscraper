#include <memory.h>
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <deque>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef int64_t i64;
template <size_t size>
using ai = array<int, size>;
template <size_t height, size_t width>
using aai = array<ai<width>, height>;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);

  array<array<int, 2>, 4> directions;
  directions[0] = { -1, 0 };
  directions[1] = { 0, 1 };
  directions[2] = { 1, 0 };
  directions[3] = { 0, -1 };

  int T = 0;
  cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    int R = 0;
    int C = 0;
    cin >> R >> C;

    vs data(R);
    vector<ii> arrows;
    arrows.reserve(R * C);
    for (int i = 0; i < R; ++i) {
      cin >> data[i];
      for (int j = 0; j < data[i].size(); ++j) {
        if (data[i][j] != '.') {
          arrows.push_back(make_pair(i, j));
        }
      }
    }

    bool impossible = false;
    int answer = 0;
    for (const auto& arr : arrows) {
      int direction = 0;
      switch (data[arr.first][arr.second]) {
        case '^':
          direction = 0;
          break;
        case '>':
          direction = 1;
          break;
        case 'v':
          direction = 2;
          break;
        case '<':
          direction = 3;
          break;
      }

      bool points = false;
      {
        const array<int, 2>& dir = directions[direction];
        int cy = arr.first;
        int cx = arr.second;
        while (true) {
          cy += dir[0];
          cx += dir[1];
          if (cy < 0 || cy >= R || cx < 0 || cx >= C) {
            break;
          }
          if (data[cy][cx] != '.') {
            points = true;
            break;
          }
        }
      }
      if (!points) {
        bool found = false;
        for (const auto& dir : directions) {
          int cy = arr.first;
          int cx = arr.second;
          while (true) {
            cy += dir[0];
            cx += dir[1];
            if (cy < 0 || cy >= R || cx < 0 || cx >= C) {
              break;
            }
            if (data[cy][cx] != '.') {
              found = true;
              break;
            }
          }
          if (found) {
            break;
          }
        }
        if (!found) {
          impossible = true;
          break;
        }
        ++answer;
      }
    }

    if (impossible) {
      cout << "Case #" << tt << ": " << "IMPOSSIBLE" << "\n";
    } else {
      cout << "Case #" << tt << ": " << answer << "\n";
    }
  }

  return 0;
}
