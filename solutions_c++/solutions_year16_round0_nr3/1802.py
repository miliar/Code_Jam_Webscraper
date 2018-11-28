#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <cstdarg>
#include <sys/time.h>
#include <random>

#ifdef _OPENMP
#include <omp.h>
#endif

#include <gmpxx.h>
typedef mpz_class bigint;

using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

typedef long long ll;


/*
ll rho(ll n) {
 for (;;) {
  ll d = 1, x, y;
  x = y = (rand() * (ll)rand()) % n;
  for (int i = 1; d == 1; i++) {
    x = (mult_mod(x, x, n) + n - 1) % n;
    d = gcd(n, ::llabs(x - y));
    if (d != 1) break;
    if ((i & (i - 1)) == 0) y = x;
  }
  if (d != n) return d;
 }
}
*/

bigint gcd(const bigint &a, const bigint &b) {
  return b == 0 ? a : gcd(b, a % b);
}

int main(int argc, char **argv) {
  puts("Case #1:");
  int N = atoi(argv[1]);
  int J = atoi(argv[2]);

  set<string> used;

#pragma omp parallel for
  rep (j, J) {
    mt19937 mt(j);
    uniform_int_distribution<> und(0, 1);

    auto random_str = [&]() {
      string s(N, '0');
      rep (i, N) s[i] = '0' + (i == 0 || i == N - 1 ? 1 : und(mt));
      return s;
    };


    for (;;) {
      string s = random_str();
#pragma omp critical
      {
        if (used.count(s)) continue;
      }

      vector<bigint> ans;

      for (int base = 2; base <= 10; ++base) {
        bigint n(s, base);
        int p = mpz_probab_prime_p(n.get_mpz_t(), 50);
        // cerr << n << " " << p << " ... " << endl;
        if (p != 0) goto retry;

        // Rho
        for (;;) {
          bigint d = 1, x, y;
          x = y = bigint(random_str(), base) % n;
          for (ll i = 1; d == 1; i++) {
            x = (x * x % n + n - 1) % n;
            d = gcd(n, abs(x - y));
            if (d != 1) break;
            if ((i & (i - 1)) == 0) y = x;
          }
          if (d != n) {
            ans.pb(d);
            break;
          }
        }
      }

      #pragma omp critical
      {
        if (used.count(s)) continue;
        used.insert(s);
        cerr << used.size() << endl;

        cout << s;
        for (const auto &d : ans) cout << " " << d;
        cout << endl;
      }

      break;
   retry:
      continue;
    }
  }
}
