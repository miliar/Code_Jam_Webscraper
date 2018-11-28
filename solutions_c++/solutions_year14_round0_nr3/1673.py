#include <iostream>
#include <cstdio>

using namespace std;

int dx[] = {1, 1, 0, -1, -1, -1, 0, 1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};

int cntMine(char map[50][50], int row, int col, int R, int C) {
  if (row < 0 || col < 0 || row >= R || col >= C)
    return 0;
  if (map[row][col] == '*')
    return 1;
  else
    return 0;
}

void reveal(char map[50][50], int row, int col, int R, int C) {
  if (row < 0 || col < 0 || row >= R || col >= C)
    return;
  if (map[row][col] != '.')
    return;
  map[row][col] = 'c';
  int cnt = 0;
  for (int d = 0; d < 8; ++d) {
    cnt += cntMine(map, row + dx[d], col + dy[d], R, C);
  }
  if (cnt == 0) {
    for (int d = 0; d < 8; ++d) {
      reveal(map, row + dx[d], col + dy[d], R, C);
    }
  }
}

bool click(char map[50][50], int row, int col, int R, int C) {
  if (map[row][col] != '.')
    return false;
  char nmap[50][50];
  for (int i = 0; i < R; ++i)
    for (int j = 0; j < C; ++j)
      nmap[i][j] = map[i][j];
  reveal(nmap, row, col, R, C);
  for (int i = 0; i < R; ++i)
    for (int j = 0; j < C; ++j)
      if (nmap[i][j] == '.')
	return false;
  map[row][col] = 'c';
  return true;
}

bool bfs(char map[50][50], int row, int col, int R, int C, int M, int N) {
  if (col == C)
    return bfs(map, row + 1, 0, R, C, M, N);
  if (row == R) {
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j)
	if (click(map, i, j, R, C))
	  return true;
    return false;
  }
  if (M > 0) {
    map[row][col] = '*';
    if (bfs(map, row, col + 1, R, C, M - 1, N))
      return true;
  }
  if (N > 0) {
    map[row][col] = '.';
    if (bfs(map, row, col + 1, R, C, M, N - 1))
      return true;
  }
  return false;
}

int main(int argc, char* argv[]) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": " << endl;
    int R, C, M;
    cin >> R >> C >> M;
    char map[50][50];
    bool found = bfs(map, 0, 0, R, C, M, R * C - M);
    if (found) {
      for (int i = 0; i < R; ++i) {
	for (int j = 0; j < C; ++j) {
	  cout << map[i][j];
	}
	cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
  }
}
