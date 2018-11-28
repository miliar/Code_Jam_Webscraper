#include <cstdio>
#include <algorithm>

using namespace std;

inline bool solve () {
  int x,r,c;
  scanf ("%d %d %d", &x, &r, &c);

  if ((r*c)%x != 0 or x >= 7) {
    return false;
  } else if (x == 1 or x == 2) {
    return true;
  } else if (x == 3) {
    return not (r < 2 or c < 2);
  } else if (x == 4) {
    return not (r < 3 or c < 3);
  } else if (x == 5) {
    return not (r < 4 or c < 4);
  } else if (x == 6) {
    return not (r < 5 or c < 5);
  }
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: %s\n", i, solve () == false ? "RICHARD" : "GABRIEL");
  }
}
