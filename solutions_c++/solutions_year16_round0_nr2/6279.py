#include <cstdint>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  string s;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    cin >> s;
    int ans = 0;
    char c = s[0];
    for (int j = 1; j < s.length(); j++) {
      if (c != s[j])
        ans++;
      c = s[j];
    }
    ans += (c != '+') ? 1 : 0;
    cout << ans << "\n";
  }

  return 0;
}

