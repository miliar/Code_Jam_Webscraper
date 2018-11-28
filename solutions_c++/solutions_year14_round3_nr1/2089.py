#include <cstdio>

int main() {
  int t, p, q;
  scanf("%d", &t);
  for (int cn = 1; cn <= t; cn++) {
    printf("Case #%d: ", cn);
    scanf(" %d/%d", &p, &q);
    for (int i = p; i > 1; i--) {
      if (i > p) {
        i = p;
      }
      if (p % i == 0 && q % i == 0) {
        p /= i;
        q /= i;
      }
    }
    int temp = q;
    while (temp % 2 == 0) {
      temp /= 2;
    }
    if (temp != 1) {
      printf("impossible\n");
      continue;
    }
    int g = 0;
    while (p < q) {
      p *= 2;
      g++;
    }
    printf("%d\n", g);
  }
  return 0;
}
