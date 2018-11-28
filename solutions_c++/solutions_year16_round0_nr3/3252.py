#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <memory.h>

#define MAXN 40

using namespace std;

// > 0 means it's not a prime, and = 0 is a prime
long long isPrime(const long long& n) {
  for (long long i = 2; i <= (long long) sqrt(n); ++i) {
    if (n % i == 0) {
       return i;
    }
  }

  return 0;
}


bool isJamCoin(const int a[], const int& n) {
  for (int base = 2; base <= 10; ++base) {
    long long val = 0;

    for (int i = 0; i < n; ++i) {
      val = (val * base) + a[i];
    }

    long long res = isPrime(val);

    // cout << val << " " << base << " " << res << endl;

    if (res == 0) {
      return false;
    }
  }

  return true;
}

int main () {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int test, c = 0;

  cin >> test;

  while (test > 0) {
    c++;
    test--;
    int n, j;
 
    cin >> n >> j;

    int a[MAXN];

    memset(a, 0, sizeof(a));

    a[0] = 1;
    a[n-1] = 1;

    int count = 0;
    int value = 0;

    // cout << "Case #" << c << ":" << endl;

    while (count < j) {
      if (isJamCoin(a, n)) {
        count++;

        for (int i = 0; i < n; ++i) {
          cout << a[i];
        }
        cout << endl;
      }

      value++;

      int m = value;
      int k = n - 2;
      while (m != 0) {
        a[k] = m % 2;
        m /= 2;
        k--;
      }

    }
  }

  return 0;
}
