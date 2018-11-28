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
  string S;
  cin >> S;
  string ans = "";
  ans += S[0];
  for (int i = 1; i < S.size(); ++i) {
    if (S[i] >= ans[0]) {
      ans = S[i] + ans;
    } else {
      ans = ans + S[i];
    }
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
