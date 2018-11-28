#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <memory.h>
#include <map>

using namespace std;

long long _gcd (long long a, long long b) {
    if (b == 0)
        return a;

    return _gcd(b, a % b);
}
int main () {
  freopen ("input.txt", "rt", stdin);
  freopen ("out.txt", "wt", stdout);

  int t ;
  scanf ("%d", &t);
  for (int tt = 0 ; tt < t ; tt++) {
    cout << "Case #" << tt+1 << ": ";

    long long a, b;
    scanf ("%lld/%lld", &a, &b);
    long long gcd = _gcd (a,b) ;
    long long nb = b/gcd;

    if (__builtin_popcount(nb) != 1) {
        cout << "impossible" << endl;
        continue;
    }
    double f = (a*1.)/b;
    //cout << a << " " << b <<  " " << f << endl;
    int ans = 0;
    while (f < 1) {
        ans ++ ;
        f *= 2;
    }

    cout << ans << endl;
  }
  return 0;
}
