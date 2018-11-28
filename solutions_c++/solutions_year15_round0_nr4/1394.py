#include "stdc++.h"
using namespace std;

#define DEBUG 0

int X, R, C;
bool win;

int main() {
  int tc, cn;
  scanf("%d", &tc);
  for(cn = 1; cn <= tc; cn++) {
    scanf("%d%d%d", &X, &R, &C);
    if(R > C)
      swap(R, C);
    win = false;
    if(R * C % X != 0)
      win = true;
    if(X == 3 && R == 1)
      win = true;
    if(X == 4 && (R == 1 || R == 2))
      win = true;
    printf("Case #%d: %s\n", cn, win ? "RICHARD" : "GABRIEL");
  }
  return 0;
}
