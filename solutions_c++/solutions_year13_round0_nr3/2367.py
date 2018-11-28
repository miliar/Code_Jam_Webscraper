#include <cstdio>
#include <cmath>

long long reverse(long long n) {
  long long ret = 0;
  while (n) {
    ret *= 10;
    ret += n % 10;
    n /= 10;
  }
  return ret;
}

int main() {
  const long long MAX = 10000000;
  int t, i;
  long long a, b, j, sqa, sqb, *ans;

  ans = new long long[MAX + 1]();
  for (j = 1; j * j <= MAX * MAX; ++j) {
    if (j == reverse(j) && j * j == reverse(j * j)) {
      ++ans[j];
    }
    ans[j] += ans[j - 1];
  }

  scanf("%d", &t);
  for (i = 1; i <= t; ++i) {
    scanf("%lld%lld", &a, &b);
    sqa = sqrt(a);
    sqb = sqrt(b);
    if (sqa * sqa < a) {
      ++sqa;
    }
    printf("Case #%d: %lld\n", i, ans[sqb] - ans[sqa - 1]);
  }
  return 0;
}
