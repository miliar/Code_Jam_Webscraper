#include<cstdio>
#include<algorithm>
using namespace std;

int T, N, p, q, r, s;
int a[1000005];
long long sum[1000005];

bool check(long long x) {
  int p = upper_bound(sum, sum + N, x) - sum - 1;
  if (p < 0) return false;
  int q = upper_bound(sum, sum + N, x + sum[p]) - sum - 1;
  long long t = sum[q];
  return sum[N - 1] - sum[q] <= x;
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A.out", "w", stdout);
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);
    for (int i = 0; i < N; ++i) {
      a[i] = ((long long)(i) * p + q) % r + s;
      sum[i] = (i == 0) ? a[i] : sum[i - 1] + a[i];
    }
    long long S = sum[N - 1];
    long long l = 0, r = S;
    while (l + 1 < r) {
      long long m = (l + r) >> 1;
      if (check(m)) {
        r = m;
      } else {
        l = m;
      }
    }
    printf("Case #%d: %.10f\n", test, (double)(S - r) / S);
  }
  return 0;
}

