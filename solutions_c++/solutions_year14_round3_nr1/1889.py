#include <cstdio>
#include <cmath>
using namespace std;

long long gcd(long long a, long long b) {
  if (b > a) return gcd(b, a);
  if (a % b == 0) return b;
  return gcd(b, a % b);
}

void solve() {
  long long n, m;
  scanf("%lld/%lld\n", &n, &m);
  int count = 0;
  long long g = gcd(n, m);
  n /= g;
  m /= g;
  
  if (m % 2 != 0) {
    printf("impossible");
    return;
  }

  while (n > 1 && m % 2 == 0) {
    n = n / 2;
    m = m / 2;
  }
  if (n == 1) {
    printf("%d", (int) log2(m));
  } else {
    printf("impossible");
  }
}

int main() {
  int N;
  scanf("%d", &N);
  for (int n = 1; n <= N; n++) {
    printf("Case #%d: ", n);
    solve();
    printf("\n");
  }
}
