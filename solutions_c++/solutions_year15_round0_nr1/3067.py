#include <iostream>
#include <string>

using namespace std;

int toi(char c) {
  return c - '0';
}

int main(void) {
  int T;

  cin >> T;
  for (int t = 1; t <= T; t++) {
    int ans = 0;
    int s_max;
    cin >> s_max;
    string s; cin >> s;
    int standing = toi(s[0]);
    for (int i = 1; i <= s_max; i++) {
      int n = toi(s[i]);
      if (standing < i) {
        ans += i - standing;
        standing += i - standing;
      }
      standing += n;
    }
    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}