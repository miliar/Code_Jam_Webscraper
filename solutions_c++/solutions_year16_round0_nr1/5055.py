#include <cstdio>

int dig(int n) {

  int r = 0;
  for (; n; n /= 10)
    r |= 1 << (n % 10);
  return r;
}

int main() {

  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);

    int N;
    scanf("%d", &N);

    if (N <= 0) {
      puts("INSOMNIA");
      continue;
    }

    int n = N;
    int d = 0;
    
    for (int k = 0; k <= 100000; k++, n+=N)
      if ((d |= dig(n)) == 0x3ff)
        break;
    if (d == 0x3ff)
      printf("%d\n", n);
    else
      puts("INSOMNIA");
  }
  return 0;
}
