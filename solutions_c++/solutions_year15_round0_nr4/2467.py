#include <iostream>
#include <cstdio>

using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    int x, r, c;
    scanf("%d%d%d", &x, &r, &c);
    int area = r*c;
    if (x == 4 && area == 8 && (r == 2 || c == 2)) {
      printf("Case #%d: RICHARD\n", tt);
      continue;
    }
    if (x > area) {
      printf("Case #%d: RICHARD\n", tt);
    } else if (x == area) {
      if (x <= 2) {
        printf("Case #%d: GABRIEL\n", tt);
      } else {
        printf("Case #%d: RICHARD\n", tt);
      }
    } else {
      if (area % x) {
        printf("Case #%d: RICHARD\n", tt);
      } else {
        int p,l;
        if (x % 2) {
          p = x/2+1;
          l = x/2+1;
        } else {
          p = x/2;
          l = x/2+1;
        }
        if (((r >= p && c >= l) || (r >= l && c >= p)) && (r >= x || c >= x)) {
          printf("Case #%d: GABRIEL\n", tt);
        } else {
          printf("Case #%d: RICHARD\n", tt);
        }
      }
    }
  }
}