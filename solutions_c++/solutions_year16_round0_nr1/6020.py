#include <cstdio>

long long solve(long long N) {
  bool a[10];
  for (int j = 0; j <= 9; j++)
    a[j] = false;
  for (long long i = 1; i <=( (1ll << 63) - 1) / N; i++) {
    for (long long j = i * N; j; j /= 10)
      a[j % 10] = true;
    for (int j = 0; j <= 9; j++)
      if (!a[j])
	goto end;
    return i * N;
  end:;
  }
  return -1;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);
    long long N;
    scanf("%lld", &N);
    if (N == 0 || (N = solve(N)) == -1)
      printf("INSOMNIA\n");
    else
      printf("%lld\n", N);
  }
}
