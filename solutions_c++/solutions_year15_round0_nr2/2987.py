#include <bits/stdc++.h>

const int N = 1010;

using namespace std;

int a[N];
int n, nTest;

int main() {
  ios::sync_with_stdio(0); cin.tie(0);
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  cin >> nTest;
  for (int test = 1; test <= nTest; ++test) {
    cin >> n;
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    int ans = 1e9;
    for (int limit = *max_element(a, a + n); limit; --limit) {
      int now = limit;
      for (int i = 0; i < n; ++i)
        if (a[i] % limit)
          now += a[i] / limit;
        else
          now += a[i] / limit - 1;
      ans = min(ans, now);
    }
    cout << "Case #" << test << ": " << ans << endl;
  }
  return 0;
}
