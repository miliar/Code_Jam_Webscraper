#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve() {
  string s;
  cin >> s;
  int n = s.size();
  int ans = 0;
  for (int i = 0; i < n - 1; ++i) {
    if (s[i] != s[i + 1]) {
      ans++;
    }
  }
  if ((ans % 2 == 1 && s[0] == '+') || (ans % 2 == 0 && s[0] == '-')) {
    ans++;
  }
  cout << ans << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    printf("Case #%d: ", i + 1);
    solve();  
  }
  return 0;
}
