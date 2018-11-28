/*
 * Fair-and-Square.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: admin
 */

#include <cstdio>
#include <cmath>

typedef unsigned long long ll;

bool isPalindrome(ll n) {
  ll p = 0;
  ll m = n;
  while (n > 0) {
    p = 10 * p + n % 10;
    n /= 10;
  }
  return (p == m);
}

int main() {
  int numTest;
  scanf("%d", &numTest);

  for (int t = 1; t <= numTest; ++t) {
    printf("Case #%d: ", t);
    ll A, B;
    scanf("%lld%lld", &A, &B);
    ll count = 0;
    for (ll n = (ll) ceil(sqrt(A)); n <= sqrt(B); ++n) {
      if (isPalindrome(n) && isPalindrome(n * n)) {
        count++;
      }
    }
    printf("%lld\n", count);
  }
  return 0;
}

