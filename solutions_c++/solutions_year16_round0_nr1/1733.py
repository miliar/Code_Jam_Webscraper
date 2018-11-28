#include <cstdio>

int main(){
  int T;
  long long N;
  scanf("%d", &T);
  for (int TC = 1; TC <= T; ++TC) {
    printf ("Case #%d: ", TC);
    scanf("%lld", &N);

    if (N == 0) printf("INSOMNIA");
    else {
      long long num = 0;
      int bm = 0;

      while (bm != (1 << 10) - 1)
      {
        num += N;
        long long tmp = num;
        while (tmp) {
          bm |= 1 << (tmp % 10);
          tmp /= 10;
        }
      }

      printf("%lld", num);
    }

    putchar('\n');
  }
}
