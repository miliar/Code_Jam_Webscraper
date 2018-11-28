#include <cstdio>

using namespace std;

int N, M, T;
int grid[105][105];

void process(int tc);
bool isSafeRow(int row);
bool isSafeCol(int col);

int main() {
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {
    process(i);
  }

  return 0;
}

void process(int tc) {
  scanf("%d %d", &N, &M);
  for (int row = 0; row < N; row++) {
    for (int col = 0; col < M; col++) {
      scanf("%d", &grid[row][col]);
    }
  }
  for (int row = 0; row < N; row++) {
    for (int col = 0; col < M; col++) {
      if (grid[row][col] == 1) {
        if (!isSafeRow(row) && !isSafeCol(col)) {
          printf("Case #%d: NO\n", tc);
          return;
        }
      }
    }
  }
  printf("Case #%d: YES\n", tc);
}

bool isSafeRow(int row) {
  for (int col = 0; col < M; col++) {
    if (grid[row][col] == 2) {
      return false;
    }
  }
  return true;
}
    
bool isSafeCol(int col) {
  for (int row = 0; row < N; row++) {
    if (grid[row][col] == 2) {
      return false;
    }
  }
  return true;
}
