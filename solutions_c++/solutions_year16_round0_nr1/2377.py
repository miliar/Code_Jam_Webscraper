#include <bits/stdc++.h>

#define bug(xx) cerr << #xx << " = " << xx << endl;

using namespace std;

#define FOR(a, b, i) for (ll i = a; i < b; ++i)

typedef long long int ll;
typedef vector<ll> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef long double ld;

void act(set<int>& s, ll n) {
  while (n > 0) {
    s.insert(n % 10);
    n /= 10;
  }
}

int main() {
  int t;
  cin >> t;
  FOR(1, t + 1, cas) {
    cout << "Case #" << cas << ": ";
    ll n, cur = 0;
    cin >> n;
    if (n == 0) cout << "INSOMNIA\n";
    else {
      set<int> s;
      int cnt = 0;
      while (++cnt) {
	cur += n;
	act(s, cur);
	if (s.size() == 10) {
	  cout << cur << '\n';
	  break;
	}
      }
    }
  }
}
