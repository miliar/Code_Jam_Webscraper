#include <iostream>
#include <cstdio>
using namespace std;

int solve(const string& s) {
  int c = 1;
  char ch = s[0];
  for (int i = 0; i < s.length(); i++) {
    if (s[i] != ch) {
      c++;
      ch = s[i];
    }
  }
  ch = s[0];
  if (s[s.length() - 1] == '+') c--;
  return c;
}

int main() {
  ios_base::sync_with_stdio(false);
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    string s; cin >> s;
    printf("Case #%d: %d\n", i, solve(s));
  }
  return 0;
}
