#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
using namespace std;

#define rep(i, s, t) for (int i = (s); i < (t); i ++)
#define repd(i, s, t) for (int i = (s); i > (t); i --)
#define ll long long

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t, s_max;
  string s;
  int cnt, ans;

  cin >> t;
  for (static int cas = 1; cas <= t; cas ++) {
    cin >> s_max >> s;
    cnt = 0, ans = 0;

    rep(i, 0, s_max+1) {
      ans = max(ans, max(i - cnt, 0));
      cnt += s[i] - '0';
    }
    cout << "Case #" << cas << ": " << ans << endl;
  }
}
