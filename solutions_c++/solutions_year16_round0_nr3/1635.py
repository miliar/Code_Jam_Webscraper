#include <bits/stdc++.h>
using namespace std;

long convert_base(int mask, int base, int N) {
  long ans = 0;
  for (int len = N - 1; len >= 0; --len) {
    ans *= base;
    ans += ((mask & (1 << len)) != 0);
  }
  return ans;
}

int main() {
  const int MAX = 100000010;
  vector<int> A(MAX, -1);
  vector<long> primes;
  for (int i = 2; i < MAX; ++i) if (A[i] == -1) {
    for (long j = long(i) * i; j < MAX; j += i) {
      A[j] = i;
    }
    primes.push_back(i);
  }
  
  auto is_prime = [&] (long value) {
    for (long x : primes) {
      if (x * x > value) {
        return -1L;
      }
      if (value % x == 0) {
        return x;
      }
    }
    assert(0);
  };
  
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; ++caso) {
    printf("Case #%d:\n", caso);
    int N, J;
    cin >> N >> J;
    
    int coins = 0;
    for (int mask = 0; mask < (1 << N); ++mask) {
      if (coins == J) break;
      
      if ((mask & 1) == 0) continue;
      if ((mask & (1 << (N - 1))) == 0) continue;
      
      vector<int> divs;
      for (int base = 2; base <= 10; ++base) {
        long x = convert_base(mask, base, N);
        if (x < MAX) {
          divs.push_back(A[x]);
        } else {
          divs.push_back(is_prime(x));
        }
      }
      
      bool can = find(divs.begin(), divs.end(), -1) == divs.end();
      
      if (can) {
        printf("%ld", convert_base(mask, 10, N));
        for (int x : divs) printf(" %d", x);
        printf("\n");
        ++coins;
      }
    }
  }
  return 0;
}