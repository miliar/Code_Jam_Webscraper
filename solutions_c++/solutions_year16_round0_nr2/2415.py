#include <bits/stdc++.h>

using namespace std;

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cout << "Case #" << t << ": ";
    string s;
    cin >> s;
    char c = '+';
    int a = 0;
    for (int i = int(s.size()) - 1; i >= 0; --i) {
      if (c != s[i]) ++a;
      c = s[i];
    }
    cout << a << endl;
  }
}