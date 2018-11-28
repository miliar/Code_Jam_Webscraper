#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

string s;
int k;

void solve(int tc) {
  cin >> s >> k;
  int ans = 0;
  FOR(i, s.length() - k + 1) {
    if (s[i] == '-') {
      ans++;
      FOR(j, k) {
        if (s[i+j] == '-') s[i+j] = '+'; else s[i+j] = '-';
      }
    }
  }
  cout << "Case #" << tc << ": ";
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '-') {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << ans << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  FOR(i, tt) {
    solve(i+1);
  }
  return 0;
}


