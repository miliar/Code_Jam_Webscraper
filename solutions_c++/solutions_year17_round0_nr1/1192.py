
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    string s;
    int k;
    cin >> s >> k;
    int ans = 0, top = (int)(s.size()-k);
    for (int i=0; i<=top; i++) {
      if (s[i] == '-') {
        ans++;
        for (int j=0; j<k; j++) {
          s[i+j] = (s[i+j]=='-') ? '+' : '-';
        }
      }
    }
    bool possible = true;
    for (unsigned int i=top+1; i<s.size(); i++) {
      possible = possible && s[i]=='+';
    }
    cout << "Case #" << tc << ": ";
    if (!possible) {
      cout << "Impossible" << endl;
    } else {
      cout << ans << endl;
    }
  }
}
