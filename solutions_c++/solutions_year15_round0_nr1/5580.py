#include <iostream>
using namespace std;
int main() {
  int T; cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int n; cin >> n;
    string s; cin >> s;
    int cur = 0;
    int ans = 0;
    for (int i = 0; i <= n; ++i) {
      int d = s[i]-'0';
      int dif = max(i-cur, 0);
      cur += d + dif;
      ans += dif;
    }
    cout << "Case #" << cas << ": " << ans << endl;
  }


}
