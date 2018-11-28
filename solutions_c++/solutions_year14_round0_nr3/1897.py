#define NDEBUG
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

#define ZERO(v) memset((v), 0, sizeof (v))

const int MAX = 50;

int R, C, M;
char board[MAX][MAX+1];

vector<pair<int, int>> cells;

int nums[MAX][MAX+1];

bool dfs_bio[MAX][MAX];
int reveal(int y, int x) {
  if (y < 0 || y >= R || x < 0 || x >= C ||
      dfs_bio[y][x] || board[y][x] == '*') {
    return 0;
  }
  dfs_bio[y][x] = 1;

  int ans = 1;
  if (nums[y][x] == 0) {
    for (int dy=-1; dy<=1; ++dy) {
      for (int dx=-1; dx<=1; ++dx) {
        ans += reveal(y+dy, x+dx);
      }
    }
  }
  return ans;
}

bool provjeri() {
  pair<int, int> click(-1, -1);
  for (int y=0; y<R; ++y) {
    for (int x=0; x<C; ++x) {
      nums[y][x] = 0;
      if (board[y][x] == '.') {
        for (int dy=-1; dy<=1; ++dy) {
          for (int dx=-1; dx<=1; ++dx) {
            if (dy == 0 && dx == 0) {
              continue;
            }
            int ny = y+dy, nx = x+dx;
            if (ny < 0 || ny >= R || nx < 0 || nx >= C) {
              continue;
            }
            nums[y][x] += board[ny][nx] == '*';
          }
        }

        if (nums[y][x] == 0 || click.first == -1) {
          click = make_pair(y, x);
        }
      }
    }
  }

  if (click.first == -1) {
    return false;
  }

  ZERO(dfs_bio);
  if (reveal(click.first, click.second) == R*C - M) {
    board[click.first][click.second] = 'c';
    return true;
  }
  return false;
}

void rek(int pos, int mines_left) {
  if (R*C - pos < mines_left) {
    return;
  }

  if (mines_left == 0) {
    if (provjeri()) {
      throw 1;
    }
    return;
  }

  assert(pos < R*C);

  for (int i=pos; i<R*C; ++i) {
    board[cells[i].first][cells[i].second] = '*';
    rek(i+1, mines_left-1);
    board[cells[i].first][cells[i].second] = '.';
  }
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d:\n", tt);
    cin >> R >> C >> M;

    for (int i=0; i<R; ++i) {
      memset(board[i], '.', C);
      board[i][C] = '\0';
    }

    cells.clear();
    for (int y=0; y<R; ++y) {
      for (int x=0; x<C; ++x) {
        cells.push_back(make_pair(y, x));
      }
    }
    try {
      rek(0, M);
      puts("Impossible");
    } catch (int x) {
      for (int i=0; i<R; ++i) {
        puts(board[i]);
      }
    }
  }

  return 0;
}
