#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL)
#define endl '\n'

using namespace std;

typedef long long ll;

string toStr(ll n) {
  stringstream ss;
  ss << n;
  return ss.str();
}

ll solve(ll n) {
  ll it = 1;
  set<int> digits;
  while (digits.size() != 10) {
    ll tmp = it * n;
    string d = toStr(tmp);
    for (int i = 0; i < d.size(); i++) {
      digits.insert(d[i] - '0');
    }
    it++;
  }
  return (it - 1) * n;
}

int main() {
  fast;
  int t, nc = 0;
  ll n;
  cin >> t;

  while (t--) {
    nc++;
    cin >> n;
    cout << "Case #" << nc << ": ";

    if (n == 0) cout << "INSOMNIA" << endl;
    else {
      cout << solve(n) << endl;
    }
  }

  return 0;
}
