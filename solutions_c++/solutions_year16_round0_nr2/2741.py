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
string s;

int main() {
  ios_base::sync_with_stdio(0);

  cin >> z;

  FOR(tc, 1, z) {
    cin >> s;
    while (s.size() && s.back() == '+') s.pop_back();
    s.resize(distance(s.begin(), unique(ALL(s))));
    cout << "Case #" << tc << ": " << s.size() << endl;
  }
}