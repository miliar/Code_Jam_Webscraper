#include <iostream>
#include <cstdio>
using namespace std;
int main() {
  FILE *fin = fopen("qd.in", "r");
  FILE *fout = fopen("qd.out", "w");
  int case_num = 0;
  fscanf(fin, "%d", &case_num);
  for (int case_id = 1; case_id <= case_num; ++case_id) {
    int x, r, c;
    fscanf(fin, "%d%d%d", &x, &r, &c);
    int ans = 0;
    if (x == 1) {
      ans = 1;
    }
    if (x == 2) {
      if (r % 2 == 0 || c % 2 == 0) {
        ans = 1;
      }
    }
    if (x == 3) {
      if (r == 3 || c == 3) {
        if (r > 1 && c > 1) {
          ans = 1;
        }
      }
    }
    if (x == 4) {
      if (c * r >= 12) {
        ans = 1;
      }
    }
    if (ans == 1) {
      fprintf(fout, "Case #%d: GABRIEL\n", case_id);
    } else {
      fprintf(fout, "Case #%d: RICHARD\n", case_id);
    }
  }
}