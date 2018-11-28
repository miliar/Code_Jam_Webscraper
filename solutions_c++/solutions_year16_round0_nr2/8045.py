#include <iostream>
using namespace std;

int calc(string s) {
  int a = 0;
  char c = s[s.length() - 1];
  if (c == '-') {
    a++;
  }
  for (int i = s.length() - 1; i >= 0; --i) {
    if (s[i] != c) {
      a++;
    }
    c = s[i];
  }
  return a;
}

int main() {
  int T;
  string s;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> s;
    cout << "Case #" << i + 1 << ": " << calc(s) << endl;
  }
}
