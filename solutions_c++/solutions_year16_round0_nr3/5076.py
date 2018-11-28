#include <iostream>
#include <bitset>
#include <cmath>
#include <vector>

using namespace std;

vector<unsigned long long> divisors;
unsigned long long width;

bool isPrime(unsigned long long n) {
  if (n <= 1) return false;
  if (n == 2) return true;
  if (n % 2 == 0) {
    divisors.push_back(2);
    return false;
  }
  for (unsigned long long i = 3; i <= sqrt(n); i+=2) {
    if (n % i == 0) {
      divisors.push_back(i);
      return false;
    }
  }
  return true;
}

unsigned long long base(unsigned long long b, unsigned long long n) {
  unsigned long long total = 0;
  unsigned long long scale = 1;
  while (n != 0) {
    total += scale * (n & 1);
    n = n >> 1;
    scale *= b;
  }
  return total;
}

bool noPrimes(unsigned long long n) {
  for (unsigned long long i = 2; i <= 10; i++) {
    if (isPrime(base(i, n))) return false;
  }
  return true;
}

int q = 0;

void defend(unsigned long long n) {
  bitset<35> k(n);
  for (int i = width - 1; i >= 0; i -= 1) {
    cout << k[i];
  }
  // cout << " : " << n;
  for (unsigned long long i : divisors) {
    cout << " " << i;
  }
  cout << endl;
}


int main() {
  ios::sync_with_stdio(false);

  unsigned long long k;
  cin >> k;
  unsigned long long m = k;

  while (k--) {
    cin >> width;
    unsigned long long j;
    cin >> j;
    cout << "Case #" << m - k << ":\n";
    for (unsigned long long i = 0; i < (unsigned long long)floor(pow((double)2,(double)(width-2))) && j > 0; i++) {
      unsigned long long x = (((i << 1) | 1) | (unsigned long long)floor(pow((double)2,(double)width-1)));
      divisors.clear();
      if (noPrimes(x)) {
        defend(x);
        j--;
      }
    }
  }

}
