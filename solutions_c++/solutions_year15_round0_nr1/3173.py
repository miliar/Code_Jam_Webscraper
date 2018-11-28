#include <bits/stdc++.h>

using namespace std;

int n;
char a;

int main() {
  ios_base::sync_with_stdio(0);
  freopen("inp.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t;
  cin >> t;
  for (int test = 1; test <= t; test++) {
    cin >> n;
    int res = 0, cur = 0;
    for (int i = 0; i <= n; i++) {
      cin >> a;
      if (a != '0') {
        if (cur >= i) {
          cur += a - '0';
        } else {
          res += i - cur;
          cur = i + a - '0';
        }
      }
    }
    cout << "Case #" << test << ": " << res << endl;
  }
  return 0;
}
