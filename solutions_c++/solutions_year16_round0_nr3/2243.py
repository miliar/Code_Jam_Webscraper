/// HEADERS

#include <bits/stdc++.h>

#define ALL(v) v.begin(), v.end()
#define REP(i, a, b) for (int i = a; i < b; i++)
#define REPD(i, a, b) for (int i = a; i > b; i--)
#define REPLL(i, a, b) for (ll i = a; i < b; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FORD(i, a, b) for (int i = a; i >= b; i--)
#define FORLL(i, a, b) for (ll i = a; i <= b; i++)
#define inf 1000000001

using namespace std;

typedef __int128_t ll;
typedef long double ld;

typedef vector<int>::iterator vit;
typedef set<int>::iterator sit;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef pair<ld, ld> pld;

#define remax(a, b) a = max(a, b)
#define remin(a, b) a = min(a, b)

#define popcount __builtin_popcount
#define pb push_back
#define mp make_pair
#define st first
#define nd second

#define eps 1e-9
#define pi acos(-1.0)

const int N = 1000123;

int z, n;

ll num(ll x, int base) {
  ll b = 1;
  ll res = 0;
  while (x) {
    if (x % 2) res += b;
    b *= base;
    x >>= 1;
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin >> z;

  cout << "Case #1:" << endl;

  FOR(tc, 1, z) {
    int j;
    cin >> n >> j;
    REPLL(i, (1LL << (n - 1)), (1LL << n)) {
      if (i % 2 == 0) continue;
      ll x = i;
      string s;
      while (x) {
        if (x % 2)
          s = "1" + s;
        else
          s = "0" + s;
        x /= 2;
      }
      vector<int> wits;
      FOR(base, 2, 10) {
        ll x = num(i, base);
        assert(x > 0);
        // cerr << i << " base: " << x << " " << n << endl;
        int sq = 50;
        FOR(i, 2, sq) {
          if (x % i == 0) {
            wits.pb(i);
            break;
          }
        }
      }
      if (wits.size() == 9) {
        // cerr << i << " ";
        cout << s << " ";
        for (int w : wits) cout << w << " ";
        cout << endl;
        if (--j <= 0) break;
      }
    }
  }
}