#include <iostream>

using namespace std;

char filp(char c) {
  return c == '+' ? '-' : '+';
}

long long count_flips(string& s, int pos, char tchar) {
  if (pos < 0) return 0;

  bool need_change = s[pos] != tchar;
  return (need_change ? 1 : 0) + count_flips(s, pos - 1, need_change ? filp(tchar) : tchar);
}

long long doit() {
  string S;
  cin >> S;
  return count_flips(S, S.size()-1, '+');
}

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t<<": " << doit() << endl;
  }
}
