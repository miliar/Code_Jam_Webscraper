#include <bits/stdc++.h>
using namespace std;

int main() {
  int T; cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    int Smax;
    string s;
    cin >> Smax >> s;
    int res = 0;
    for(int i = 0, k = 0; i < s.size(); ++i) {
      if(s[i] == '0') continue;
      if(k < i) {
        res += i - k;
        k = i;
      }
      k += s[i] - '0';
    }
    cout << res << endl;
  }
  return 0;
}

