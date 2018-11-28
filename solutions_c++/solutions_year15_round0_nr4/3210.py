#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i =1; i<=t; i++) {
    int x, r, c;
    cin >> x >> r >> c;
    if (x == 1) {
      printf("Case #%d: GABRIEL\n", i);
      continue;
    } else if (x == 2) {
      if (r*c % 2 !=0) {
        printf("Case #%d: RICHARD\n", i);
        continue;
      } else {
        printf("Case #%d: GABRIEL\n", i);
        continue;
      }
    } else if (x==3) {
      if (min(r, c) == 1 || r*c % 3 !=0) {
        printf("Case #%d: RICHARD\n", i);
        continue;
      } else {
        printf("Case #%d: GABRIEL\n", i);
        continue;
      }
    } else {
      if (min(r, c) <= 2 || r*c % 4 !=0 || max(r, c) < 3) {
        printf("Case #%d: RICHARD\n", i);
        continue;
      } else {
        printf("Case #%d: GABRIEL\n", i);
        continue;
      }
    }
  }
}
