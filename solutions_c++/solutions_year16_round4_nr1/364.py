#include <bits/stdc++.h>
using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using ll = long long;
using VL = vector<ll>;
using VVL = vector<VL>;
using P = pair<int, int>;
using VP = vector<P>;
using VVP = vector<VP>;

string sorted(const string &r) {
  vector<string> v;
  for (char c : r) v.push_back(string(1, c));
  int size = v.size();
  while (size > 1) {
    vector<string> w;
    for (int i = 0; i < size; i += 2) {
      w.push_back(min(v[i], v[i + 1]) + max(v[i], v[i + 1]));
    }
    size /= 2;
    swap(v, w);
  }
  return v[0];
}

void solve(int cas) {
  int n;
  cin >> n;

  VI l{2};
  for (int i = 0; i < n; ++i) {
    VI nl;
    for (int c : l) {
      nl.push_back(c);
      nl.push_back((c + 1) % 3);
    }
    swap(l, nl);
  }

  VI v(3);
  for (int c : l) ++v[c];

  VI w(3);
  for (int i = 0; i < 3; ++i) cin >> w[i];

  cout << "Case #" << cas << ": ";
  char P[3] = {'R', 'P', 'S'};
  for (int r = 0; r < 3; ++r) {
    bool ok = true;
    for (int i = 0; i < 3; ++i) {
      if (v[i] != w[(i + r) % 3]) {
        ok = false;
        break;
      }
    }
    if (ok) {
      string res{""};
      for (int c : l) res += P[(c + r) % 3];
      cout << sorted(res) << endl;
      return;
    }
  }
  cout << "IMPOSSIBLE" << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  for (int z = 1; z <= t; ++z) solve(z);
}
