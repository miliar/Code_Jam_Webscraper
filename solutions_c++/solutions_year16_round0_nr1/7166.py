#include <bits/stdc++.h>
using namespace std;

bool chk[10];


bool ok(long long x) {
  while (x) {
    chk[x % 10] = true;
    x /= 10;
  }
  for (int i = 0; i <= 9; ++i) if (!chk[i]) return false;
  return true;
}
int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; ++tc) {
    memset(chk, 0, sizeof(chk));
    int n;
    cin >> n;
    if (n == 0) {
      cout << "Case #" << tc << ": INSOMNIA" << '\n';
      continue;
    }
    long long cur = n;
    while (!ok(cur)) {
      cur += n;
    }
    cout << "Case #" << tc << ": " << cur << '\n';
    cerr << "Case #" << tc << ": " << cur << endl;
  }
}
