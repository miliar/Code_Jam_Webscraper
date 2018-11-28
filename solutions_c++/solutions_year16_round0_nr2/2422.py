#include <bits/stdc++.h>

#define bug(xx) cerr << #xx << " = " << xx << endl;

using namespace std;

#define FOR(a, b, i) for (ll i = a; i < b; ++i)

typedef long long int ll;
typedef vector<ll> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef long double ld;

string rev(string a, int i) {
  string r = a;
  FOR(0, i, j) {
    if (a[j] == '-') r[i - j - 1] = '+';
    else r[i - j - 1] = '-';
  }
  return r;
}

int main() {
  int t;
  cin >> t;
  FOR(1, t + 1, cas) {
    cout << "Case #" << cas << ": ";
    string s;
    cin >> s;
    map<string, int> cost;
    int n = s.size();
    cost[string(n, '+')] = 0;
    queue<string> Q;
    Q.push(string(n, '+'));
    while (not Q.empty()) {
      string u = Q.front();
      Q.pop();
      FOR(1, n + 1, i) {
	string v = rev(u, i);
	if (not cost.count(v)) {
	  cost[v] = cost[u] + 1;
	  Q.push(v);
	}
      }
    }
    cout << cost[s] << '\n';
  }
}
