#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef map<int, int> mii;
typedef set<int> si;
typedef map<string, int> msi;

string solve(int n, int p, int r, int s) {
  if (p < 0 or r < 0 or s < 0) return "IMPOSSIBLE";
  if (n == 0) {
    if (p == 1) return "P";
    if (r == 1) return "R";
    if (s == 1) return "S";
  }
  if (n == 1) {
    if (p == 1 and r == 1) return "PR";
    if (p == 1 and s == 1) return "PS";
    if (r == 1 and s == 1) return "RS";
    return "IMPOSSIBLE";
  }
  int g = (1 << (n - 2));
  string c = solve(n - 2, p - g, r - g, s - g);
  if (c == "IMPOSSIBLE") return c;
  string a = "";
  for (int i = 0; i < c.size(); ++i) {
    if (c[i] == 'P') a += "PRPS";
    if (c[i] == 'R') a += "PRRS";
    if (c[i] == 'S') a += "PSRS";
  }
  return a;
}

int main() {
  ios_base::sync_with_stdio(false);
  cout.setf(ios::fixed);
  cout.precision(10);
  int tt;
  cin >> tt;
  for (int ttt = 1; ttt <= tt; ++ttt) {
    cout << "Case #" << ttt << ": ";
    int n, p, r, s;
    cin >> n >> r >> p >> s;
    cout << solve(n, p, r, s) << endl;
  }
  
}