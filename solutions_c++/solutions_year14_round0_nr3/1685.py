#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 50;
int R, C, M;

void print(char grid[MAX][MAX])
{
  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      cout << grid[r][c];
    }
    cout << endl;
  }
}

void fill(char grid[MAX][MAX], int h, int w)
{
  for (int r = 0; r < h; r++) {
    for (int c = 0; c < w; c++) {
      grid[r][c] = '.';
    }
  }
  grid[0][0] = 'c';
}

bool inside(int r, int c)
{
  return 0 <= r && r < R && 0 <= c && c < C;
}

void mark(char grid[MAX][MAX], int mines[MAX][MAX], int r, int c)
{
  grid[r][c] = 'X';
  if (mines[r][c]) return;

  for (int r2 = r-1; r2 <= r+1; r2++) {
    for (int c2 = c-1; c2 <= c+1; c2++) {
      if (inside(r2, c2) && grid[r2][c2] == '.') {
	mark(grid, mines, r2, c2);
      }
    }
  }

}

bool click(char grid[MAX][MAX], int mines[MAX][MAX], int r, int c)
{
  char newgrid[MAX][MAX];
  for (int i = 0; i < R; i++) {
    copy(grid[i], grid[i]+C, newgrid[i]);
  }

  mark(newgrid, mines, r, c);
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (newgrid[i][j] == '.') return false;
    }
  }
  return true;
}

bool check(char grid[MAX][MAX])
{
  int mines[MAX][MAX] = {{0}};   // could be optimize and not recompute each time

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      for (int r2 = r-1; r2 <= r+1; r2++) {
	for (int c2 = c-1; c2 <= c+1; c2++) {
	  if (inside(r2, c2) && grid[r2][c2] == '*') {
	    mines[r][c]++;
	  }
	}
      }
    }
  }

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      if (grid[r][c] == '*') continue;
      if (click(grid, mines, r, c)) {
	grid[r][c] = 'c';
	return true;
      }
    }
  }
  return false;
}

bool choose(char grid[MAX][MAX], int r, int c, int empty)
{
  int left = R*C-r*C-c;
  if (empty > left) return false;
  if (empty == 0) {
    return check(grid);
  }

  int r2 = r, c2 = c+1;
  if (c2 == C) {
    c2 = 0;
    r2++;
  }

  grid[r][c] = '.';
  if (choose(grid, r2, c2, empty-1)) {
    return true;
  }
  grid[r][c] = '*';
  if (choose(grid, r2, c2, empty)) {
    return true;
  }
  return false;
}

void solve()
{
  cin >> R >> C >> M;

  int empty = R*C-M;
  char grid[MAX][MAX];

  for (int r = 0; r < R; r++) {
    for (int c = 0; c < C; c++) {
      grid[r][c] = '*';
    }
  }

  if (empty == 1) {
    fill(grid, 1, 1);
    goto done;
  }

  for (int h = 2; h <= R; h++) {
    if (empty % h != 0) continue;
    int w = empty / h;
    if (w > C || w == 1) continue;
    fill(grid, h, w);
    goto done;
  }

  if (choose(grid, 0, 0, empty)) {
    goto done;
  }

  cout << "Impossible" << endl;
  return;


 done:
  print(grid);

}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ":" << endl;
    solve();
  }

  return 0;
}
