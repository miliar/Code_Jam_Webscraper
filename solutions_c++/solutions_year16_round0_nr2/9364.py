#include <iostream>
#include <string>
using namespace std;

int main() {
  int T, _42=1;
  cin >> T;
  while (T--) {
    string s;
    cin >> s;
    int ans = 0;
    for (int i = 0; i < s.size()-1; i++) {
      if (s[i] != s[i+1]) ans++;
    }
    if (s[s.size()-1] == '-') ans++;
    cout << "Case #" << _42++ << ": " << ans << endl;
  }
  return 0;
}
