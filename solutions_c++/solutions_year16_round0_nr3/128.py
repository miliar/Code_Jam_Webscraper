#include <bits/stdc++.h>

using namespace std;

const int MAX = 1 << 25;

bool prime[MAX];
int np, p[MAX];
int a[777], dv[777];

int main() {
  for (int i = 2; i < MAX; i++) {
    prime[i] = true;
  }
  np = 0;
  for (int i = 2; i < MAX; i++) {
    if (prime[i]) {
      p[np++] = i;
      for (long long j = i * 1LL * i; j < MAX; j += i) {
        prime[j] = false;
      }
    }
  }
  cerr << "sieve done! " << np << " primes detected" << endl;
  srand(8753);
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d:\n", qq);
    int n, J;
    scanf("%d %d", &n, &J);
    int real_n = n;
    if (n == 32) {
      n >>= 1;
    }
    set <long long> jams;
    while (J > 0) {
      long long u = 0;
      for (int i = 0; i < n; i++) {
        if (i == 0 || i == n - 1) {
          a[i] = 1;
        } else {
          a[i] = rand() % 2;
        }
        u = u * 2 + a[i];
      }
      if (jams.find(u) != jams.end()) {
        continue;
      }
      bool err = false;
      for (int base = 2; base <= 10; base++) {
        long long x = 0;
        for (int i = 0; i < n; i++) {
          x = x * base + a[i];
        }
        dv[base] = -1;
        for (int i = 0; i < np && p[i] * 1LL * p[i] <= x; i++) {
          if (x % p[i] == 0) {
            dv[base] = p[i];
            break;
          }
        }
        if (dv[base] == -1) {
          err = true;
          break;
        }
      }
      if (!err) {
        cerr << "found! J = " << J << endl;
        jams.insert(u);
        for (int i = 0; i < real_n; i++) {
          putchar(a[i % n] + '0');
        }
        for (int base = 2; base <= 10; base++) {
          printf(" %d", dv[base]);
        }
        printf("\n");
        J--;
      }
    }
    cerr << "jams.size() = " << jams.size() << endl;
  }
  return 0;
}
