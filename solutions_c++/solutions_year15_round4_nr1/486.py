#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int R, C;
char table[100][100];

enum {
  NONE,
  UP,
  DOWN,
  LEFT,
  RIGHT,
};

char Convert(char c) {
  switch(c) {
  case '.': return NONE;
  case '^': return UP;
  case 'v': return DOWN;
  case '<': return LEFT;
  case '>': return RIGHT;
  }
  return -1;
}

int CheckEdge(int i, int j) {
  switch (table[i][j]) {
  case NONE: return 0;
  case UP: i-=1; break;
  case DOWN: i+=1; break;
  case LEFT: j-=1; break;
  case RIGHT: j+=1; break;
  }
  if (i < 0 || R <= i || j < 0 || C <= j) return 1;
  return 0;
}

bool CheckDir(int i, int j, int di, int dj) {
  i += di; j += dj;
  while (0 <= i && i < R && 0 <= j && j < C) {
    if (table[i][j] != NONE) return true;
    i += di; j += dj;
  }
  return false;
}

int Check(int i, int j) {
  if (table[i][j] == NONE) return 0;
  int di = 0, dj = 0;
  switch (table[i][j]) {
  case UP: di = -1; break;
  case DOWN: di = 1; break;
  case LEFT: dj = -1; break;
  case RIGHT: dj = 1; break;
  }
  if (CheckDir(i, j, di, dj)) return 0;
  if (CheckDir(i, j, 0, -1) ||
      CheckDir(i, j, 0, 1) ||
      CheckDir(i, j, -1, 0) ||
      CheckDir(i, j, 1, 0)) return 1;
  return -1;
}

int Solve() {
  int cnt = 0;
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      int r = Check(i, j);
      if (r < 0) return -1;
      cnt += r;
    }
  }
  return cnt;
}

int main() {
  int nnn;
  cin >> nnn;
  for (int iii = 0; iii < nnn; ++iii) {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) {
      string line;
      cin >> line;
      for (int j = 0; j < C; ++j) {
	table[i][j] = Convert(line[j]);
      }
    }
    int ans = Solve();
    if (ans < 0)
      cout << "Case #" << iii+1 << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << iii+1 << ": " << ans << endl;
  }
}
