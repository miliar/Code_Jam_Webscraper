#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int DIM_MAX = 128;
int DIR_X[4] = {1, 0, -1, 0};
int DIR_Y[4] = {0, 1, 0, -1};

int R, C;
int grid[DIM_MAX][DIM_MAX];
//int row_arrow_cts[DIM_MAX];
//int col_arrow_cts[DIM_MAX];

void init() {
  /*
  for (int i = 0; i < DIM_MAX; i++) {
    row_arrow_cts[i] = col_arrow_cts[i] = 0;
  }
  */

  cin >> R >> C;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      char temp; cin >> temp;
      if (temp == '>')
        grid[i][j] = 0;
      else if (temp == 'v')
        grid[i][j] = 1;
      else if (temp == '<')
        grid[i][j] = 2;
      else if (temp == '^')
        grid[i][j] = 3;
      else {
        assert(temp == '.');
        grid[i][j] = -1;
      }

      /*
      if (grid[i][j] != -1) {
        row_arrow_cts[i]++;
        col_arrow_cts[j]++;
      }
      */
    }
  }
}

bool in_bounds(int r, int c) {
  return (r >= 0 && r < R && c >= 0 && c < C);
}

bool needs_change(int r, int c) {
  int cur = grid[r][c];
  assert(cur != -1);
  r += DIR_Y[cur];
  c += DIR_X[cur];

  while (in_bounds(r, c)) {
    if (grid[r][c] != -1)
      return false;
    r += DIR_Y[cur]; c += DIR_X[cur];
  }
  return true;
}

bool can_change(int r, int c) {
  for (int dir = 0; dir < 4; dir++) {
    int cur_r = r + DIR_Y[dir];
    int cur_c = c + DIR_X[dir];
    while (in_bounds(cur_r, cur_c)) {
      if (grid[cur_r][cur_c] != -1)
        return true;
      cur_r += DIR_Y[dir]; cur_c += DIR_X[dir];
    }
  }
  return false;
}

void solve_case(int t) {
  init();

  int changes = 0;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (grid[i][j] == -1)
        continue;

      //cout << "checking " << i << ", " << j << endl;
      if (needs_change(i, j)) {
        //cout << "needs change!\n";
        if (!can_change(i, j)) {
          cout << "Case #" << t << ": IMPOSSIBLE\n";
          return;
        }

        changes++;
      }
    }
  }

  cout << "Case #" << t << ": " << changes << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
