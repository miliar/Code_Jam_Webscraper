#include <cstdio>
#include <algorithm>

using namespace std;

int t,x,r,c;

bool solve() {
  if (x == 1)
    return true;
  if (r * c % x)
    return false;
  if (x <= 2)
    return true;
  if (x == 4)
    return (r * c >= 12 ? true : false);
  // then x == 3
  if (min(r,c) == 1)
    return false;
  return true;
}

int main() {
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {
    scanf("%d%d%d", &x, &r, &c);
    if ( solve() )
      printf ("Case #%d: GABRIEL\n", ti);
    else
      printf ("Case #%d: RICHARD\n", ti);
  }
  return 0;
}
