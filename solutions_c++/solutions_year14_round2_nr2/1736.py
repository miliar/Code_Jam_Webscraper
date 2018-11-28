#include <cstdio>

int main () {

  int T;
  scanf ("%d", &T);
  
  for (int t = 1; t <= T; ++t) {
    int A, B, K;
    scanf ("%d%d%d", &A, &B, &K);
    int count = 0;
    for (int a = 0; a < A; ++a)
      for (int b = 0; b < B; ++b)
	if ((a & b) < K)
	  ++count;
    printf ("Case #%d: %d\n", t, count);
  }

  return 0;
}
