#include <iostream>
#include <vector>
#include <string>
using namespace std;
char op(char c) {
  return c == '+' ? '-' : '+';
}
void reverse(string &s, int idx) {
  if (idx % 2 == 0) {
    s[idx / 2] = op(s[idx / 2]);
  }
  for (int i = 0; i < (idx + 1) / 2; i++) {
    char tmp = s[i];
    s[i] = op(s[idx - i]);
    s[idx - i] = op(tmp);
  }
}
int main() {
  int tk, tk1 = 0;
  cin >> tk;
  while (tk--) {
    tk1++;
    string s;
    cin >> s;
    int cnt = 0;
    while (true) {
      if (s[0] == '-') {
        int idx = s.length() - 1;
        while (idx >= 0 && s[idx] == '+') {
          idx--;
        }
        reverse(s, idx);
      }
      else {
        int idx = 0;
        while (idx < s.length() && s[idx] == '+') {
          idx++;
        }
        if (idx == s.length()) {
          break;
        }
        else {
          reverse(s, idx - 1);
        }
      }
      cnt++;
      //cout << "cnt, s = " << cnt << ", " << s << endl;
    }
    cout << "Case #" << tk1 << ": " << cnt << endl;
  }
}
