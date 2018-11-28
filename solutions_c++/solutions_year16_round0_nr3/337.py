#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int) (a).size())

ll f(ll x) {
  assert(x >= 2);
  for (int i = 2; 1LL * i * i <= x; i++) {
    if (x % i == 0) {
      return i;
    }
  }
  return x;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  vector<vector<ll>> ans;
  for (int i = 32769; i < 65536; i += 2) {
    bool ok = true;
    vector<ll> cur {i};
    for (int j = 2; j <= 10; j++) {
      ll val = 0;
      ll mult = 1;
      int x = i;
      while (x > 0) {
        val += mult * (x & 1);
        mult *= j;
        x /= 2;
      }
      ll fv = f(val);
      if (fv == val) {
        ok = false;
        break;
      } else {
        cur.push_back(fv);
      }
    }
    if (ok) {
      ans.push_back(cur);
    }
    if (SZ(ans) >= 50) {
      break;
    }
  }
  assert(SZ(ans) == 50);
  cout << "Case #1:" << endl;
  for (auto &it : ans) {
    string s = "";
    int j = it[0];
    while (j > 0) {
      s += (char)('0' + (j & 1));
      j /= 2;
    }
    reverse(ALL(s));
    cout << s;
    for (int i = 1; i < SZ(it); i++) {
      cout << ' ' << it[i];
    }
    cout << '\n';
  }
  return 0;
}

