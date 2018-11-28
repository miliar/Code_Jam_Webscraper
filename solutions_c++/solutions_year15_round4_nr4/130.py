#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

#define MOD 1000000007

int R, C;

int A[10][10];
int dr[] = {-1, 0, 1, 0};
int dc[] = {0, -1, 0, 1};

int check() {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (A[i][j] == -1) continue;
      int lo = 0;
      int hi = 0;
      for (int k = 0; k < 4; k++) {
        int r = i + dr[k];
        int c = (j + dc[k] + C) % C;
        if (r < 0 || r >= R || c < 0 || c >= C) continue;
        if (A[r][c] == -1) {
          hi++;
        } else if (A[r][c] == A[i][j]) {
          lo++;
          hi++;
        }
      }
      if (A[i][j] < lo || hi < A[i][j]) {
        return 0;
      }
    }
  }
  for (int cyc = 1; cyc <= C; cyc++) {
    if (C % cyc != 0) continue;

    bool ok = true;
    for (int i = 0; i < R && ok; i++) {
      for (int j = 0; j < C && ok; j++) {
        if (A[i][(j + cyc) % C] != A[i][j]) {
          ok = false;
        }
      }
    }
    if (ok) {
      return C / cyc;
    }
  }
  return 0;
}

int solve(int r, int c) {
  int v = check();
  if (v == 0) return 0;
  if (r == R) {
/*
    cout << v << endl;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        cout << A[i][j] << ' ';
      }
      cout << endl;
    }
*/
    return v;
  }
  if (c == C) return solve(r + 1, 0);

  int ret = 0;
  for (int i = 1; i < 4; i++) {
    A[r][c] = i;
    ret += solve(r, c + 1);
    A[r][c] = -1;
  }
  return ret;
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> R >> C;
    memset(A, -1, sizeof(A));
    cout << "Case #" << t << ": " << solve(0, 0) / C << endl;
  }
}
