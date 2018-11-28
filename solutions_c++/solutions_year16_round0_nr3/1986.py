#include <bits/stdc++.h>

#define bug(xx) cerr << #xx << " = " << xx << endl;

using namespace std;

#define FOR(a, b, i) for (ll i = a; i < b; ++i)

typedef long long int ll;
typedef vector<ll> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef long double ld;

string conv(int dins, int n) {
  n = (n - 4) / 2;
  string s (n, '0');
  FOR(0, n, pos) {
    if (dins % 2 == 1) ++s[pos];
    dins /= 2;
  }
  return "1" + s + "11" + s + "1";
}

ll diwv(ll b, ll n) {
  n /= 2;
  ll r = 1;
  FOR(0, n, i) r *= b;
  return r + 1;
}

int main() {
  int t;
  cin >> t;
  cout << "Case #1:\n";
  int n, j;
  cin >> n >> j;
  FOR(0, j, dins) {
    cout << conv(dins, n);
    FOR(2, 11, b) cout << ' ' << diwv(b, n);
    cout << '\n';
  }
}
