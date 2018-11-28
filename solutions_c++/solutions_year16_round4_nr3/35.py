#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int DIM_MAX = 120;
int R, C;
int N;
int pairs[4 * DIM_MAX];
char grid[DIM_MAX][DIM_MAX];
bool impossible;
const int DIR_R[4] = {0, -1, 0, 1};
const int DIR_C[4] = {1, 0, -1, 0};

void print_grid() {
  for (int i = 1; i <= R; i++) {
    for (int j = 1; j <= C; j++) {
      cout << grid[i][j];
    }
    cout << "\n";
  }
}

void get_pos(int x, int *r, int *c) {
  assert(0 <= x && x < N);
  if (x < C) {
    *r = 0; *c = x + 1;
  } else if (x < R + C) {
    *r = x - C + 1; *c = C + 1;
  } else if (x < 2*C + R) {
    *r = R + 1; *c = (2*C + R) - x;
  } else {
    *r = (2*C + 2*R) - x; *c = 0;
  }
}

int get_occupant(int r, int c) {
  if (r == 0 && 0 < c && c <= C) {
    return c - 1;
  } else if (c == C + 1 && 0 < r && r <= R) {
    return C + r - 1;
  } else if (r == R + 1 && 0 < c && c <= C) {
    return R + C + (C - c);
  } else if (c == 0 && 0 < r && r <= R) {
    return 2*C + R + (R - r);
  }
  return -1;
}

void hug_left(int looking_for, int r, int c, int dir) {
  /*
  cout << "----------\n";
  cout << "hugging " << r << ", " << c << ", dir: " << dir << endl;
  print_grid();
  cout << "----------\n";
  */

  int next_r = r + DIR_R[dir];
  int next_c = c + DIR_C[dir];

  int occupant = get_occupant(next_r, next_c);
  if (occupant != -1) {
    if (occupant != looking_for)
      impossible = true;
    return;
  }

  char cell = grid[next_r][next_c];
  if (cell == '.') {
    //cout << "filling!" << endl;
    if (dir % 2 == 0) { // left or right
      grid[next_r][next_c] = '/';
    } else {
      grid[next_r][next_c] = '\\';
    }
    hug_left(looking_for, next_r, next_c, (dir + 1) % 4);
  } else if (cell == '/') {
    if (dir % 2 == 0) {
      hug_left(looking_for, next_r, next_c, (dir + 1) % 4);
    } else {
      hug_left(looking_for, next_r, next_c, (dir + 3) % 4);
    }
  } else if (cell == '\\') {
    if (dir % 2 == 1) {
      hug_left(looking_for, next_r, next_c, (dir + 1) % 4);
    } else {
      hug_left(looking_for, next_r, next_c, (dir + 3) % 4);
    }
  } else {
    assert (false);
  }
}

void grow(int x) {
  // cout << "growing " << x << endl;
  int mate = pairs[x];

  int inner = x + 1;
  while (inner != mate) {
    if (pairs[inner] > mate) {
      impossible = true;
      return;
    }
    grow(inner);
    if (impossible)
      return;
    inner = pairs[inner] + 1;
  }

  int r, c;
  get_pos(x, &r, &c);
  int dir;
  if (x < C)
    dir = 3;
  else if (x < R + C)
    dir = 2;
  else if (x < 2 * C + R)
    dir = 1;
  else
    dir = 0;
  hug_left(mate, r, c, dir);
}

void init() {
  impossible = false;
  cin >> R >> C;
  N = 2 * (R + C);
  for (int i = 0; i < R + C; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    pairs[x] = y; pairs[y] = x;
  }

  for (int i = 0; i < DIM_MAX; i++) {
    for (int j = 0; j < DIM_MAX; j++) {
      grid[i][j] = '.';
    }
  }
}

void solve_case(int t) {
  init();
  int cur = 0;
  while (cur < N) {
    grow(cur);
    if (impossible) break;
    cur = pairs[cur] + 1;
  }

  cout << "Case #" << t << ":\n";
  if (impossible) {
    cout << "IMPOSSIBLE\n";
  } else {
    for (int i = 1; i <= R; i++) {
      for (int j = 1; j <= C; j++) {
        if (grid[i][j] == '.')
          grid[i][j] = '/';
      }
    }
    print_grid();
  }
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
