#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <cmath>

int INF = 2147483647;
double INFD = 2147483647;

double PI = 3.14159265359;

using namespace std;

void Sieve(unsigned long long n, set<unsigned long long>& primes) {
  vector<bool> is_prime(ceil(sqrt(n)), true);
  is_prime[0] = is_prime[1] = false;
  unsigned long long i = 2;
  while (i < is_prime.size()) {
    if (is_prime[i]) {
      primes.insert(i);
      unsigned long long j = i + i;
      while (j < is_prime.size()) {
        is_prime[j] = false;
        j += i;
      }
    }
    i++;
  }
}

unsigned long long FirstFactor(unsigned long long n,
                               set<unsigned long long>& primes) {
  set<unsigned long long>::iterator prime = primes.begin();
  while (prime != primes.end()) {
    if (!(n % *prime)) {
      return *prime;
    }
    ++prime;
  }
  return n;
}

unsigned long long Debasefy(unsigned bits, unsigned long long base) {
  unsigned long long power = 1;
  unsigned long long total = 0;
  while (bits) {
    if (bits & 1) {
      total += power;
    }
    bits >>= 1;
    power *= base;
  }
  return total;
}

string Stringfy(unsigned bits) {
  string ret_val;
  while (bits) {
    ret_val += '0' + (bits & 1);
    bits >>= 1;
  }
  reverse(ret_val.begin(), ret_val.end());
  return ret_val;
}

void Solve(unsigned length, unsigned target, set<unsigned long long>& primes) {
  unsigned total = (1 << (length)) - 1;
  unsigned bits = (1 << (length-1)) + 1;
  while (bits < total && target) {
    unsigned long long base = 2;
    vector<unsigned long long> factors;
    while (base <= 10) {
      unsigned long long n = Debasefy(bits, base);
      unsigned long long factor = FirstFactor(n, primes);
      if (factor == n) {
        break;
      }
      factors.push_back(factor);
      base++;
    }
    if (factors.size() == 9) {
      cout << Stringfy(bits);
      int i = 0;
      while (i < factors.size()) {
        cout << " " << factors[i];
        i++;
      }
      cout << endl;
      target--;
    }
    bits += 2;
  }
}

int main() {
  unsigned long long n = 100000000;
  n *= n;
  set<unsigned long long> primes;
  Sieve(n, primes);
  int t = 0;
  cin >> t;
  unsigned N = 0, J = 0;
  cin >> N >> J;
  Solve(N, J, primes);

  return 0;
}
