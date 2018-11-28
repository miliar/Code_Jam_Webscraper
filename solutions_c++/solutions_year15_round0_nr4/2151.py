#include <cstdio>

bool omino(int X, int R, int C) {
  if (C < R) {
    return omino(X, C, R);
  }
  if ((R * C) % X != 0) {
    return false;
  }
  if (X <= 2) {
    return true;
  }
  if (X == 3) {
    return R > 1;
  }
  if (C == 2 && R == 2) {
    return false;
  }
  return R == 3 || R == 4;
}

int main() {
  int T, X, R, C;

  scanf("%i", &T);

  for (int t = 1; t <= T; ++t) {
    printf("Case #%i: ", t);
    scanf("%i %i %i", &X, &R, &C);
    if (omino(X, R, C)) {
      printf("GABRIEL\n");
    }
    else {
      printf("RICHARD\n");
    }
  }

  return 0;
}
