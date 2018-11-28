#include <cstdio>

typedef long long ll;

ll mpow(ll x, ll p) {
  if (x == 0)
    return 0;
  ll res = 1;
  while (p) {
    if (p & 1)
      res *= x;
    x *= x;
    p >>= 1;
  }
  return res;
}

ll pos(int k, int K, int C) {

  if (k == 0 || C == 0)
    return 0;

  return pos(k - 1, K, C - 1) * K + k;
}

int main() {

  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {

    int K, C, S;
    scanf("%d%d%d", &K, &C, &S);

    printf("Case #%d: ", t);

    if (S != K) {
      puts("DON'T KNOW");
      continue;
    }

    for (int k = 0; k < K; k++)
      printf("%lld ", pos(k, K, C) + 1);
    putchar('\n');
  }

  return 0;
}
