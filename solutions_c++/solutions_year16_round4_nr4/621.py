#include <iostream>
#include <vector>

using namespace std;

int n;

bool check(string& mask, int work, int mach) {
  if (work == ((1 << n) - 1))
    return true;
  for (int i = 0; i < n; ++i) {
    if (((work >> i) & 1) == 0) {
      int cnt = 0;
      bool good = true;
      for (int j = 0; j < n; ++j) {
        if (((mach >> j) & 1) == 0) {
          if (mask[i * n + j] == '1') {
            ++cnt;
            good &= check(mask, work | (1 << i), mach | (1 << j));
          }
        }
      }
      if (cnt == 0 || (cnt > 0 && good == false))
        return false;
    }
  }
  return true;
}

int main() {
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    cin >> n;
    string res = "";
    vector<string> m(n);
    for (int i = 0; i < n; ++i) {
      cin >> m[i];
      res += m[i];
    }
    int ans = n * n;
    for (int mask = 0; mask < (1 << (n * n)); ++mask) {
      string t = res;
      int cnt = 0;
      for (int i = 0; i < n * n; ++i)
        if ((mask >> i) & 1)
          if (t[i] == '0') {
            t[i] = '1';
            ++cnt;
          }
      if (check(t, 0, 0))
        ans = min(ans, cnt);
    }
    cout << "Case #" << test << ": " << ans << '\n';
  }
  return 0;
}
