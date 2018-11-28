#include <iostream>
using namespace std;

int main() {
  int T; cin >> T;
  for (int ncase = 1; ncase <= T; ++ ncase) {
    string s; cin >> s;
    char last = s[0];
    int ans = 0;
    for (char c : s) {
      ans += c != last;
      last = c;
    }
    cout << "Case #" << ncase << ": " << ans + (last=='-') << endl;
  }
}
