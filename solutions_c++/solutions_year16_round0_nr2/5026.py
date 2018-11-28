#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

#define FOR(i,n) for(int i=0; i<n; i++)

typedef long long LL;

using namespace std;

string s;

void solve() {
  cin >> s;
  int idx = 0;
  int cnt = 0;
  int cur = s[0];

  FOR(idx, (int)s.length() - 1) {
    if (s[idx+1] != s[idx]) {
      cnt++;
    }
  }

  if (s[s.length() - 1] == '-') cnt++;

  cout << cnt << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  FOR(t,tt) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
