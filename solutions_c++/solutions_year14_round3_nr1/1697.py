#include <cstdio>

bool checkDen (int n) {
  while (n > 1) {
    if (n % 2 == 0)
      n = n/2;
    else
      return false;
  }
  return true;
}

int main () {

  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; ++t) {
    int P, Q;
    scanf ("%d/%d", &P, &Q);

    int steps = 0;
    if (!checkDen (Q)) {
      printf ("Case #%d: impossible\n", t);
      continue;
    }
    
    int num = Q;
    while (num > 0) {
      if (P >= num)
	break;
      else {
	++steps;
	num = num/2;
      }
    }
    if (num == 0)
      printf ("Case #%d: impossible\n", t);
    else
      printf ("Case #%d: %d\n", t, steps);

  }

  return 0;
}
