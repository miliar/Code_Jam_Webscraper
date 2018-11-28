#include <bits/stdc++.h>

#define SIEVE_MAX 10000001LL

using namespace std;

bitset<10000001> bs;

vector<long long> primes;

void sieve() {
  bs.set();
  bs[0] = 0;
  bs[1] = 0;
  for (long long i = 2LL; i < SIEVE_MAX; ++i) {
    int prime = i;
    if (!bs[prime]) continue;
    
    primes.push_back(i);
    for (long long j = i * i; j < SIEVE_MAX; j += i) {
      int idx = j;
      bs[idx] = 0;
    }
  }
}

bool isPrime(long long num) { // no number > (SIEVE_MAX - 1)²
  if (num < SIEVE_MAX) {
    int inum = num;
    return bs[inum];
  }
  long long sqroot = sqrt(num);
  for (int i = 0; i < bs.size(); ++i) {
    if (primes[i] > sqroot) return true;
    
    long long divisor = primes[i];
    if (num % divisor == 0) return false;
  }
  return true;
}

int main() {
  int t, n, j;
  cin >> t >> n >> j;
  return 0;
}
