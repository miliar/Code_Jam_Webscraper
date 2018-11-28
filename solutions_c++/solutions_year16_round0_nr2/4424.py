#include <iostream>

using namespace std;

int main() {
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    string s;
    cin >> s;
    bool is_first = s[0] == '-';
    int cnt = 0;
    int pos = 0;
    while (pos < (int) s.length()) {
      if (s[pos] == '+') {
        ++pos;
        continue;
      }
      ++cnt;
      while (pos < (int) s.length() && s[pos] == '-')
        ++pos;
    }
    cout << "Case #" << test << ": " << 2 * cnt - is_first << '\n';
  }
  return 0;
}
