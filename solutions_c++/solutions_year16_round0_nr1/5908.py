#include <cstdio>
#include <string.h>

typedef long long ll;

ll count(ll n) {
  int c = 10;
  while (n>0) c *= 10, n /= 10;
  return c;
}

int main() {
  int t, c = 0;

  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);

    printf("Case #%d: ", ++c);

    ll d[10], cnt = 10, lim = count(n);
    memset(d, 0, sizeof d);

    bool found = false;
    for (ll i = 1, j = n; !found && cnt > 0 && i <= lim; ++i, j = i*n) {
      do {
        if (d[j % 10] == 0)
          d[j % 10] = 1, --cnt;
        if (cnt == 0) printf("%lld\n", i*n), found = true;
        j /= 10;
      } while (!found && j > 0);
    }

    if (!found) puts("INSOMNIA");
  }

  return 0;
}
