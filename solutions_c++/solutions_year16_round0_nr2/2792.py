#include <bits/stdc++.h>
using namespace std;

string rev(const string & s, int cnt) {
  string res = s;
  reverse(res.begin(), res.begin() + cnt);
  for (int i = 0; i < cnt; ++i)
    res[i] = (res[i] == '+') ? '-' : '+';

  return res;
}

bool isGood(const string & s) {
  for  (int i = 0; i < s.size(); ++i) {
    if (s[i] == '-')
      return false;
  }
  return true;
}

void solve() {
  string s;
  cin >> s;

  if (isGood(s)) {
    cout << 0 << endl;
    return;
  }

  map<string, int> dist;
  dist[s] = 0;

  queue<string> t;
  t.push(s);

  while (t.size()) {
    string l = t.front();
    int cd = dist[l];
    t.pop();

    for (int i = 1; i <= s.size(); ++i) {
      string tmp = rev(l, i);
      // cerr << l << " " << i << " " << tmp << endl;
      if (!dist.count(tmp) || dist[tmp] > (cd + 1)) {
        dist[tmp] = cd + 1;
        t.push(tmp);
      }

      if (isGood(tmp)) {
        cout << dist[tmp] << endl;
        return;
      }
    }
  }
}

int main() {
  int t;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cerr << i << " of " << t << endl;
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
