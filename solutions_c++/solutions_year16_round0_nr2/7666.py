#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("OUTPUT.txt", "w", stdout);
  int t;
  string s;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> s;
    cout << "Case #" << i + 1  << ": ";
    if (s.size() == 1) {
        if (s[0] == '+'){cout << 0;} else {cout << 1;}
    } else if (s.size() == 2) {
      if (s[0] == s[1] && s[1] == '+') {
        cout << 0;
      } else if (s[0] == s[1]) {cout << 1;}
      else {
        if (s[0] == '+') {cout << 2;}
        else{cout << 1;}
      }
    } else {
      int ind = 0;
      int k = 0;
      int Plus = 0;
      while(ind < s.size()) {
        if (s[ind] == '-') {ind++;continue;}
        while(ind < s.size() && s[ind] == '+') {Plus++;ind++;}
         k++;
      }
      if (k == 1) {
            if (Plus == s.size()) {cout << 0;} else if (Plus == s.size() - 1 && s[0] == '-') {cout << 1;} else if (s[s.size() - 1] == '+') {cout << 1;}
        else if (s[0] == '+') {cout << 2;} else {
            cout << 3;
        }
      } else {
        int ans = (k - 1) * 2;
        if (s[0] == '-') {ans++;}
        if (s[s.size() - 1] == '-') {ans += 2;}
         cout << ans;
      }
    }
    cout << endl;
  }

  return 0;
}
