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

typedef long long ll;
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

set<int> s;

void check(int x) {
  while (x) {
    s.insert(x % 10);
    x /= 10;
  }
}

int main() {
  ios_base::sync_with_stdio(0);

  cin >> z;

  FOR(tc, 1, z) {
    cin >> n;
    s.clear();

    cout << "Case #" << tc << ": ";

    if (n == 0)
      cout << "INSOMNIA" << endl;
    else {
      long long i = 0;
      long long x;
      while (s.size() < 10) {
        i++;
        x = i * n;
        check(x);
      }
      cout << i* n << endl;
    }
  }
}