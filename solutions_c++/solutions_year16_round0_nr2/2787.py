#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int T;
  string s;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";

    cin >> s;
    
    int ans = 0;
    for (int i = 0; i < s.size() - 1; ++i) {
      if (s[i] != s[i + 1]) {
        if (s[i] == '+') {
          ans += 2;
        }
      }
    }

    if (s[0] == '-') {
      ++ans;
    }

    cout << ans << endl;
  }
}
