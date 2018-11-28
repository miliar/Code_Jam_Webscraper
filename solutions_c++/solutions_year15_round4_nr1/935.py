
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int test = 1; test <= T; test++) {
    int R, C;
    cin >> R >> C;

    cin.ignore();

    std::vector<std::vector<std::pair<int, int>>> grid;
    for (int r = 0; r < R; r++) {
      grid.emplace_back();

      for (int c = 0; c < C; c++) {
        char v;
        cin >> v;

        std::pair<int, int> cell{0, 0};

        if (v == '>') {
          cell.second = 1;
        } else if (v == '<') {
          cell.second = -1;
        } else if (v == '^') {
          cell.first = -1;
        } else if (v == 'v') {
          cell.first = 1;
        }

        grid.back().push_back(cell);
      }

      cin.ignore();
    }

    bool impossible = false;
    for (int r = 0; r < R; r++) {
      int cnt = 0;
      int last = 0;
      for (int c = 0; c < C; c++) {
        if (grid[r][c] != std::pair<int, int>{0, 0}) {
          cnt++;
          last = c;
        }
      }

      if (cnt == 1) {
        cnt = 0;
        for (int rr = 0; rr < R; rr++) {
          if (grid[rr][last] != std::pair<int, int>{0, 0}) cnt++;
        }

        if (cnt == 1) {
          impossible = true;
        }
      }
    }

    if (impossible) {
      printf("Case #%d: %s\n", test, "IMPOSSIBLE");
      continue;
    }

    int changes = 0;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (grid[r][c] == std::pair<int, int>{0, 0}) continue;

        int rr = r;
        int cc = c;

        do {
          rr += grid[r][c].first;
          cc += grid[r][c].second;
        } while (0 <= rr && rr < R && 0 <= cc && cc < C &&
                 grid[rr][cc] == std::pair<int, int>{0, 0});

        if (!(0 <= rr && rr < R && 0 <= cc && cc < C)) {
          changes++;
        }
      }
    }

    printf("Case #%d: %d\n", test, changes);
  }
}
