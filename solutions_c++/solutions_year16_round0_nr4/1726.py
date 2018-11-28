#include <cstdio>

int main() {
  int T, K, C, S;
  scanf("%d", &T);
  for (int TC = 1; TC <= T; ++TC) {
    scanf("%d %d %d", &K, &C, &S);
    printf("Case #%d:", TC);
    if (K == 1) printf(" 1");
    else if (C == 1 && S == K)
      for (int i = 1; i <= K; ++i)
        printf(" %d", i);
    else if (C > 1 && S + 1 >= K)
      for (int i = 2; i <= K; ++i)
        printf(" %d", i);
    else printf(" IMPOSSIBLE");
    putchar('\n');
  }
}
