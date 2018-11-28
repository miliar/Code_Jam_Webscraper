#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define RICHARD 123
#define GABRIEL 456

int who(int X, int R, int C) {
  if (R > C) swap(R, C);

  if (R*C % X) return RICHARD;
  if (X >= 7) return RICHARD;

  if (X == 1) return GABRIEL;
  if (X == 2) return GABRIEL;
  if (X == 3) {
    if (R == 1 && C == 3) return RICHARD;
    return GABRIEL;
  }
  if (X == 4) {
    if (R == 1 || C == 1 || R == 2 || C == 2) return RICHARD;
    return GABRIEL;
  }
  return RICHARD;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int X, R, C;
    scanf("%d%d%d", &X, &R, &C);

    printf("Case #%d: %s\n", tc, who(X, R, C) == RICHARD ? "RICHARD" : "GABRIEL");
  }
}
