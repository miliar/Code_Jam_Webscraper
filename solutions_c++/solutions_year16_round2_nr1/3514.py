#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

typedef long long LL;

int T, ti;

string dig[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
  "EIGHT", "NINE"};
bool ff;
int cnt[1000];
int ans[10];

bool check(int n, int k) {
  bool r = true;
  for (int i = 0; i < dig[n].length(); ++i) {
    cnt[dig[n][i]] -= k;
    if (cnt[dig[n][i]] < 0)
      r = false;
  }
  if (r == false) {
    for (int i = 0; i < dig[n].length(); ++i)
      cnt[dig[n][i]] += k;
    return false;
  }
  // cout << n << ' ' << k << endl;
  return true;
}

bool f(int l, int n) {
  // cout << ans[3] << endl;
  if (l == 0) {
    ff = true;
    for (int i = 0; i <= 9; ++i)
      for (int j = 0; j < ans[i]; ++j)
        cout << i;
    cout << endl;
    return true;
  }
  if (n > 9)
    return false;
  for (int i = 1; i <= l / dig[n].length(); ++i) {
    if (check(n, i) && !ff) {
      ans[n] += i;
      if (f(l - i*dig[n].length(), n+1))
        return true;
      ans[n] -= i;
      for (int j = 0; j < dig[n].length(); ++j)
        cnt[dig[n][j]] += i;
    } else {
      break;
    }
  }
  if (!ff)
    f(l, n+1);
  return false;
}

int solve() {
  string s;
  ff = false;
  for (char c = 'A'; c <= 'Z'; ++c)
    cnt[c] = 0;
  for (int i = 0; i <= 9; ++i)
    ans[i] = 0;
  cin >> s;
  for (int i = 0; i < s.length(); ++i) {
    cnt[s[i]]++;
  }
  printf("Case #%d: ", ti);
  f(s.length(), 0);

  return 0;
}

int main() {
  cin >> T;
  for (ti = 1; ti <= T; ti++) {
    solve();
  }
  return 0;
}
