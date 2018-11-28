#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

unsigned long long interpret(unsigned long long v, unsigned long long base, unsigned long long n) {
  unsigned long long result = 0;
  unsigned long long mask = 1 << (n-1);
  while (mask) {
    result = ((v & mask) ? 1 : 0) + result * base;
    mask >>= 1;
  }

  return result;
}

int main(int argc, char* argv[]) {
  if (argc < 2) return 1;

  ifstream ifs(argv[1]);

  int t, n, j;
  ifs >> t;
  ifs >> n;
  ifs >> j;

  // primes
  unsigned long long upper = 1024*1024*1;
  vector<unsigned long long> primes(upper+1, 1);

  # pragma omp parallel for
  for (unsigned long long i = 2; i <= upper/2; ++i) {
    if (primes[i] != 1) continue;
    for (unsigned long long ii = i+i; ii <= upper; ii += i) {
      primes[ii] = i;
    }
  }

  cout << "Case #1:" << endl;

  unsigned long long limit = (1 << (n-2));
  int count = 0;
  for (unsigned long long v = (1 << (n-1)) + 1, i = 0; i < limit && count < j; ++i, v += 2) {
    int base = 2;
    vector<unsigned long long> divisors(10+1, 1);

    for (; base <= 10; ++base) {
      unsigned long long val = interpret(v, base, n);
      if (val < upper) {
        if (primes[val] == 1) break; // prime
        divisors[base] = primes[val];
      } else {
        if (val % 2 == 0) {
          divisors[base] = 2;
        } else {
          for (unsigned long long i = 3; i < sqrt(val)+1 && i < upper; i += 2) {
            if (primes[i] != 1) continue;
            if (val % i == 0) {
              divisors[base] = i;
              break;
            }
          }
        }
        if (divisors[base] == 1) break; // prime
      }
      assert ((val % divisors[base]) == 0);
    }

    if (base <= 10) continue;
    count += 1;
    unsigned long long mask = 1 << (n-1);
    while (mask) {
      cout << ((mask & v) ? 1 : 0);
      mask >>= 1;
    }
    for (int ii = 2; ii <= 10; ++ii) {
      //cout << " " << divisors[ii] << "(" << interpret(v, ii, n) << ")";
      cout << " " << divisors[ii];
    }
    cout << endl;
  }

  return 0;
}
