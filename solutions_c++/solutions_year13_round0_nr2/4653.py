#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int n_tests;
  scanf("%d", &n_tests);
  for (int test = 1; test <= n_tests; ++test) {
    int R, C;
    scanf("%d %d", &R, &C);
    int T[R][C];
    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        scanf("%d", &T[r][c]);
      }
    }
    int vr[R];
    int nr = R;
    for (int r = 0; r < R; ++r) {
      vr[r] = r;
    }
    int vc[C];
    int nc = C;
    for (int c = 0; c < C; ++c) {
      vc[c] = c;
    }
    bool fail = false;
    while (nr > 0 && nc > 0 && !fail) {
      // find min. entry
      int r_min = 0, c_min = 0;
      for (int r = 0; r < nr; ++r) {
        for (int c = 0; c < nc; ++c) {
          if (T[vr[r]][vc[c]] < T[vr[r_min]][vc[c_min]]) {
            r_min = r;
            c_min = c;
          }
        }
      }
      // try removing column
      bool can_remove_column = true;
      for (int r = 0; r < nr && can_remove_column; ++r) {
        can_remove_column = (T[vr[r]][vc[c_min]] == T[vr[r_min]][vc[c_min]]);
      }
      if (can_remove_column) {
        swap(vc[nc - 1], vc[c_min]);
        --nc;
      } else {
        // try removing row
        bool can_remove_row = true;
        for (int c = 0; c < nc && can_remove_row; ++c) {
          can_remove_row = (T[vr[r_min]][vc[c]] == T[vr[r_min]][vc[c_min]]);
        }
        if (can_remove_row) {
          swap(vr[nr - 1], vr[r_min]);
          --nr;
        } else {
          fail = true;
        }
      }
    }
    if (fail) {
      printf("Case #%d: NO\n", test);
    } else {
      printf("Case #%d: YES\n", test);
    }
  }
  return 0;
}
