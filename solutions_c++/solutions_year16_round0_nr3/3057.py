#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;
typedef unsigned int uint;

int is_prime(ll x) {
  assert(x < 4e+18);
  cerr << "x = " << x << endl;
  for (ll d = 2; d * d <= x; d++) {
    if (x % d == 0) {
      return d;
    }
  }
  return -1;
}

void testCase()
{
  int n, J;
  scanf("%d%d", &n, &J);

  for (uint m = (1 << (n - 1)) + 1; m < 1 << n; m += 2) {
    cerr << m << endl;

    bool coin = true;
    vector<int> divisors;
    for (int base = 2; base <= 10; base++) {
      ll value = 0;
      for (int i = n - 1; i >= 0; i--) {
        value = base * value + ((m >> i) & 1);
      }
      int d = is_prime(value);
      divisors.push_back(d);
      if (d < 0) {
        coin = false;
      }
    }

    if (coin) {
      for (int i = n - 1; i >= 0; i--) {
        printf("%d", (m >> i) & 1);
      }
      for (int d : divisors) {
        printf(" %d", d);
      }
      printf("\n");
      if (--J == 0) {
        break;
      }
    }
  }
  assert(J == 0);
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T;
//  cin >> T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
//    cout << "Case #" << t << ": ";
    printf("Case #%d:\n", t);
    testCase();
  }
  return 0;
}
