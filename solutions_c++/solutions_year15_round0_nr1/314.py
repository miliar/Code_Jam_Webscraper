// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    string s;
    cin >> n >> s;
    n++;
    int ans = 0;
    int cnt = s[0] - '0';
    for (int i = 1; i < n; i++) {
      if (cnt < i) {
        ans += i - cnt;
        cnt = i + s[i] - '0';
      } else {
        cnt += s[i] - '0';
      }
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}

