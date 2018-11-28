#include <iostream>
#include <string>

const int kMaxN = 105;
const int kMaxM = 105;

int N, M;
int a[kMaxN][kMaxM];
int row_value[kMaxN], column_value[kMaxM];

bool solve() {
  for (int r = 0; r < N; ++r) { row_value[r] = -1; }
  for (int c = 0; c < M; ++c) { column_value[c] = -1; }
  for (int r = 0; r < N; ++r) {
    int max = -1;
    for (int c = 0; c < M; ++c) if (a[r][c] > max) { max = a[r][c]; }
    for (int c = 0; c < M; ++c) {
      if (a[r][c] < max) {
        if (column_value[c] == -1) {
          column_value[c] = a[r][c];
        } else if (column_value[c] != a[r][c]) {
          return false;
        }
      }
    }
  }
  for (int c = 0; c < M; ++c) {
    int max = -1;
    for (int r = 0; r < N; ++r) if (a[r][c] > max) { max = a[r][c]; }
    if (column_value[c] != -1 && column_value[c] < max) { return false; }
    for (int r = 0; r < N; ++r) {
      if (a[r][c] < max) {
        if (row_value[r] == -1) {
          row_value[r] = a[r][c];
        } else if (row_value[r] != a[r][c]) {
          return false;
        }
      }
    }
  }
  return true;
}

int main(int argc, char *argv[]) {
  int t;
  std::cin >> t;
  for (int i = 0; i < t; ++i) {
    std::cin >> N >> M;
    for (int r = 0; r < N; ++r) {
      for (int c = 0; c < M; ++c) {
        std::cin >> a[r][c];
      }
    }
    std::cout << "Case #" << i + 1 << ": "
              << (solve() ? "YES" : "NO")
              << std::endl;
  }
  return 0;
}
