#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>


namespace {
  using namespace std;
  int T;
  int X, R, C;

  void input() {
    cin >> X >> R >> C;
  }

  void solve(int case_num) {
    if (R > C) swap(R, C);
    if (X == 1) {
      printf("Case #%d: GABRIEL\n", case_num);
    } else if (X == 2) {
      if (R * C % 2 == 0) {
        printf("Case #%d: GABRIEL\n", case_num);
      } else {
        printf("Case #%d: RICHARD\n", case_num);
      }
    } else if (X == 3) {
      if (R * C % 3 == 0 && R > 1 && C > 1) {
        printf("Case #%d: GABRIEL\n", case_num);
      } else {
        printf("Case #%d: RICHARD\n", case_num);
      }
    } else if (X == 4) {
      if (C == 4 && (R == 3 || R == 4)) {
        printf("Case #%d: GABRIEL\n", case_num);
      } else {
        printf("Case #%d: RICHARD\n", case_num);
      }
    }
  }
}

int main() {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    input();
    solve(t + 1);
  }
  return 0;
}
