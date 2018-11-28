#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int T, ti;
int n, sum, ans;
string s;


int solve() {
  cin >> n >> s;
  sum = 0, ans = 0;
  for (int i = 0; i <= n; ++i) {
    int t = s[i] - '0';
    if (sum < i)
      ans += (i - sum), sum = i;
    sum += t;
  }

  printf("Case #%d: %d\n", ti, ans);
  return 0;
}

int main() {
    cin >> T;
    for (ti = 1; ti <= T; ti++) {
        solve();
    }
    return 0;
}
