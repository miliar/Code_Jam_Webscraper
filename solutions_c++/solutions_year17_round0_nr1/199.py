#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1000000007LL

#define rep(i, n) for(int i = 0; i < (n); i++)
#define rrep(i, n) for(int i = (n) - 1; i >= 0; i--)
#define trep(i, n) for(int i = 0; i <= (n); i++)
#define rep1(i, n) for(int i = 1; i <= (n); i++)
#define mfor(i, s, t) for(int i = (s); i < (t); i++)
#define tfor(i, s, t) for(int i = (s); i <= (t); i++)

int tmp[1919];

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    string s;
    int k;
    cin >> s >> k;
    rep(i, s.size()) {
      if(s[i] == '+') {
        tmp[i] = 0;
      }
      else {
        tmp[i] = 1;
      }
    }
    int ans = 0;
    trep(i, s.size() - k) {
      if(tmp[i]) {
        ans++;
        rep(j, k) {
          tmp[i + j] ^= 1;
        }
      }
    }
    bool ok = true;
    rep(i, k - 1) {
      if(tmp[s.size() - k + 1 + i]) {
        ok = false;
      }
    }
    if(ok) {
      cout << "Case #" << _ << ": " << ans << endl;
    }
    else {
      cout << "Case #" << _ << ": " << "IMPOSSIBLE" << endl;
    }
  }
}
