#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MAXN = 1000100;
int ar[MAXN];
ll sums[MAXN];

int T;
int N, p, q, r, s;
ll best;

void check(int a, int b) {
  ll x = sums[a], y = sums[b] - sums[a], z = sums[N] - sums[b];
  ll amar = x + y + z - max(x, max(y, z));
  if (amar > best) best = amar;
}
int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    scanf("%d %d %d %d %d", &N, &p, &q, &r, &s);
    for(int i = 0; i < N; ++i) {
      ar[i] = ((ll(i) * p + q) % r + s);
      sums[i + 1] = sums[i] + ar[i];
    }

    best = 0;
    int sec = 0;
    while (sec + 1 <= N && sums[sec + 1] <= sums[N] - sums[sec + 1]) ++sec;
    for(int x = 0; x <= N; ++x) {
      check(x, sec);
      while (sec + 1 <= N && sums[sec + 1] - sums[x] <= sums[N] - sums[sec + 1]) {
        ++sec;
        check(x, sec);
      }
      if (sec + 1 <= N)
        check(x, sec + 1);
    }

    long double ans = (long double)(best) / sums[N];
    printf("Case #%d: %.10Lf\n", t, ans);
  }
  return 0;
}
