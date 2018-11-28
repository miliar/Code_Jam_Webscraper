#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

string flip(string x, int P) {
  string p = x.substr(0, P);
  string s = x.substr(P);
  reverse(all(p));
  for (char& c : p) {
    if (c == '+')
      c = '-';
    else
      c = '+';
  }
  return p + s;
}

int smart(string s) {
  vector<bool> tokens;
  for (int i = 0; i < s.size(); i++) {
    if (i + 1 == s.size() || s[i] != s[i + 1])
      tokens.pb(s[i] == '+');
  }
  int res = 0;
  for (bool token : tokens)
    if (!token)
      ++res;
  for (int i = 0; i < tokens.size(); i++) {
    if (i + 1 < tokens.size() && tokens[i] && !tokens[i + 1])
      ++res;
  }
  return res;
}

void solve() {
  string s;
  cin >> s;
  int n = s.size();
  /*string ideal(n, '+');
  map<string, int> ways;
  queue<string> q;
  ways[s] = 0;
  q.push(s);
  while (!ways.count(ideal)) {
    assert(!q.empty());
    string c = q.front(); q.pop();
    for (int p = 1; p <= n; p++) {
      string nc = flip(c, p);
      if (!ways.count(nc)) {
        ways[nc] = ways[c] + 1;
        q.push(nc);
      }
    }
  }
  cout << ways[ideal] << endl;
  assert(smart(s) == ways[ideal]);
  cerr << ways.size() << endl;*/
  cout << smart(s) << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;

  for (int t = 1; t <= tests; t++) {
    cout << "Case #" << t << ": ";
    solve();
  }
  
  return 0;
}
