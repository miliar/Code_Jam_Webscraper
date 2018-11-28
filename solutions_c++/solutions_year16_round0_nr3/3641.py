#include <bits/stdc++.h>
using namespace std;

vector<long long> primes;
constexpr size_t kPrimesCount = 30000;

int main() {
  primes.reserve(kPrimesCount);
  for (long long i = 2; primes.size() < kPrimesCount; ++i) {
    bool isPrime = true;
    for (auto j : primes) {
      if (i % j == 0) {
        isPrime = false;
        break;
      }
      if (j * j >= i) break;
    }
    if (isPrime) primes.push_back(i);
  }

  int z;
  scanf("%d", &z);
  for (int zz = 1; zz <= z; ++zz) {
    int n, j;
    scanf("%d %d", &j, &n);

    printf("Case #%d:\n", zz);
    vector<int> u(j, 0);
    u[0] = u[j-1] = 1;
    while (n > 0) {
      array<long long, 10> ds;
      bool ok = true;
      for (int i = 2; ok && i <= 10; ++i) {
        ok = false;
        for (auto p : primes) {
          long long uu = 0;
          long long r = 0;
          for (auto t : u) {
            uu = uu * i + t;
            r = r * i + uu / p;
            uu %= p;
          }
          if (r <= 1) break;
          if (uu == 0) {
            ds[i-1] = p;
            ok = true;
            break;
          }
        }
      }
      if (ok) {
        for (auto x : u) printf("%d", x);
        for (int i = 2; i <= 10; ++i) printf(" %lld", ds[i - 1]);
        printf("\n");
        --n;
      }

      ++u[j-2];
      for (int x = j-2; x >= 0 && u[x] > 1; --x) {
        u[x-1] += u[x] / 2;
        u[x] = u[x] % 2;
      }
    }
  }

  return 0;
}
