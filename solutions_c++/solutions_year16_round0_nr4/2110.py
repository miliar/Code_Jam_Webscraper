#include <bits/stdc++.h>

#define bug(xx) cerr << #xx << " = " << xx << endl;

using namespace std;

#define FOR(a, b, i) for (ll i = a; i < b; ++i)

typedef long long int ll;
typedef vector<ll> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef long double ld;

int main() {
  int t;
  cin >> t;
  FOR(1, t + 1, cas) {
    cout << "Case #" << cas << ":";
    int k, c, s;
    cin >> k >> c >> s;
    FOR(1, k + 1, i) cout << ' ' << i;
    cout << '\n';
  }
}
