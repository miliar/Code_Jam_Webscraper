#include <bits/stdc++.h>
using namespace std;

int ch[2234];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  int tc = 1;
  while (t--) {
    string s;
    cin >> s;
    int i, j;
    i = j = 1001;
    ch[i] = s[0];
    for (int k = 1; k < s.length(); ++k) {
      if (s[k] >= ch[i]) {
        --i;
        ch[i] = s[k];
      }
      else {
        ++j;
        ch[j] = s[k];
      }
    }
    cout << "Case #" << tc++ << ": ";
    for (int k = i; k <= j; ++k)
      cout << (char)ch[k];
    cout << "\n";
  } 

  return 0;
}