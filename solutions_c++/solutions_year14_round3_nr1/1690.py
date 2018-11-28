#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>

#define REP(i, n) for (int i = 0; i < (n); i++)

typedef unsigned long long int ll;

void docase(int tcase) {
  ll p, q; scanf("%llu/%llu", &p, &q);
  for (int n = 0; n <= 40; ++n) {
    if ((p * (1LL << 40)) % q == 0) {
      ll k = (1LL << 40) * p / q - (1LL << (40 - n));
      if (k >= 0 && k <= (1LL << 40) - (1LL << (40 - n))) {
        printf("Case #%d: %d\n", tcase, n);
        return;
      }
    }
  }

  printf("Case #%d: impossible\n", tcase);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; i++) docase(i+1);
}
