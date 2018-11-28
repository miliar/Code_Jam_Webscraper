#include <cstdio>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

typedef std::pair<int, int> cell;

int R, C, M;
char **cells;

void print_cells(char **_cells, bool debug);
void read_example();
void count_mines(int x, int y, char **_cells);
bool valid(char **_cells);
void solve_case();

int main()
{
#if 1
  int count;
  scanf("%d", &count);
  for (int p = 1; p <= count; p++) {
      scanf("%d %d %d\n", &R, &C, &M);
      printf("Case #%d:\n", p);
      solve_case();
  }
#endif

/*
  read_example();
  print_cells(cells, true);
  if (valid(cells)) {
    printf("valid\n");
  } else {
    printf("invalid\n");
  }
*/
}

void init_cells(int x, int y, char **_cells) {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      _cells[i][j] = '.';
    }
  }
  _cells[x][y] = 'c';
}
int next_comb(int comb[], int k, int n) {
    int i = k - 1;
    ++comb[i];
    while ((i >= 0) && (comb[i] >= n - k + 1 + i)) {
        --i;
        ++comb[i];
    }

    if (comb[0] > n - k)
        return 0;

    for (i = i + 1; i < k; ++i)
        comb[i] = comb[i - 1] + 1;

    return 1;
}

void solve_case()
{
    int *comb = new int[M];
    cells = new char*[R];
    for (int i = 0; i < R; i++) {
      cells[i] = new char[C];
    }
    std::vector<cell> v;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++){
        v.push_back(cell(i, j));
      }
    }

    int size = v.size();
    for (int i = 0; i < M; i++) {
        comb[i] = i;
    }

    while (next_comb(comb, M, size)) {
      for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
          init_cells(i, j, cells);
          // set mines
          for (int c = 0; c < M; c++) {
            //        printf("%d(%d, %d), ", i, v[comb[i]].first, v[comb[i]].second);
            cells[v[comb[c]].first][v[comb[c]].second] = '*';
          }
          if (cells[i][j] != '*') {
            cells[i][j] = 'c';
            if (valid(cells)) {
              print_cells(cells, false);
              return;
            }
//            print_cells(cells, true);
          }
        }
      }
    }
    printf("Impossible\n");
}


bool valid(char **_cells) {
  int init_x, init_y;

  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (cells[i][j] == 'c') {
        init_x = i;
        init_y = j;
      }
    }
  }
  count_mines(init_x, init_y, cells);
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      //      printf("cells[%d][%d]=%c\n", i, j, cells[i][j]);
      if (cells[i][j] == '.') {
        return false;
      }
    }
  }
  return true;
}

void count_mines(int x, int y, char **_cells)
{
  int num = 0;
  for (int dx = -1; dx <= 1; dx++) {
    for (int dy = -1; dy <= 1; dy++) {
      int nx = x + dx, ny = y + dy;
      if (0 <= nx && nx < R &&
          0 <= ny && ny < C && _cells[nx][ny] == '*') {
        num++;
      }
    }
  }
  if (_cells[x][y] != 'c') {
    _cells[x][y] = num + '0';
  }
  if (num != 0) {
    return;
  }
  for (int dx = -1; dx <= 1; dx++) {
    for (int dy = -1; dy <= 1; dy++) {
      int nx = x + dx, ny = y + dy;
      if (0 <= nx && nx < R &&
          0 <= ny && ny < C && _cells[nx][ny] == '.') {
        count_mines(nx, ny, _cells);
      }
    }
  }
}


void print_cells(char **_cells, bool debug)
{
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (!debug &&
           cells[i][j] >= '0' && cells[i][j] <= '8') {
          printf(".");
      } else {
        printf("%c", cells[i][j]);
      }
    }
    printf("\n");
  }
}

void read_example()
{
  char new_line;
  scanf("%d %d", &R, &C);
  printf("%d %d\n", R, C);
  new_line = getchar();
  assert(new_line == '\n');
  cells = new char*[R];
  for (int i = 0; i < R; i++) {
    cells[i] = new char[C];
    for (int j = 0; j < C; j++) {
      cells[i][j] = getchar();
    }
    new_line = getchar();
    assert(new_line == '\n');
  }
}
