#include <bits/stdc++.h>

using namespace std;

int main() {
  int tc, x, r, c, t;
  scanf("%d",&tc);
  for (t = 1; t <= tc; t++) {
    scanf("%d%d%d",&x,&r,&c);
    if (c > r) {
      c = c+r;
      r = c-r;
      c = c-r;
    }
    if ((r >= x) and (c >= (x - 1))) {
      if (((r - x) * c) % x == 0)
        printf("Case #%d: GABRIEL\n", t);
      else
        printf("Case #%d: RICHARD\n", t);
    } else
			printf("Case #%d: RICHARD\n", t);
	}
  return 0;
}