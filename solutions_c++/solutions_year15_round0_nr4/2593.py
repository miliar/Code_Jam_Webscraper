#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int tn, ti;
  scanf("%d", &tn);
  for (int ti = 0; ti < tn; ti ++) {
    int x, r, c;
    scanf("%d%d%d", &x, &r, &c);
    printf("Case #%d: ", ti + 1);

    bool yes = true;

    if (r * c % x != 0) {
      yes = false;
    }
    if (max(r, c) < x) {
      yes = false;
    }
    if (x == 1) {
    } else if (x == 2) {
    } else if (x == 3) {
      if (min(r, c) < 2) {
        yes = false;
      }
    } else if (x == 4) {
      if (min(r, c) < 2) {
        yes = false;
      }
      if (r * c <= 8) {
        yes = false;
      }
    }
    if (yes) {
      printf("GABRIEL\n");
    } else {
      printf("RICHARD\n");
    }
  }
}
