#include <iostream>
using namespace std;

char op(char c) {
  if (c == '+') {
    return '-';
  }
  return '+';
}

int fun(string s, int k) {
  int res = 0;
  int n = s.size();
  for (int i = 0; i + k <= n; ++i) {
    if (s[i] == '-') {
      ++res;
      for (int j = 0; j < k; ++j) {
        s[i + j] = op(s[i + j]);
      }
    }
  }
  for (int i = n - k + 1; i < n; ++i) {
    if (s[i] == '-') {
      return -1;
    }
  }
  return res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    string s;
    int k;
    cin >> s >> k;
    int res = fun(s, k);
    cout << "Case #" << cas << ": ";
    if (res == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << res << endl;
    }
  }
}
