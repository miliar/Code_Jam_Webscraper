#include <iostream>
#include <string>

using namespace std;

int solve(string s) {
  int cnt = 0;
  char start = s[0];
  for (int i = 1; i < s.size(); ++i) {
    if (s[i] != start) {
      ++cnt;
      start = start == '-' ? '+' : '-';
    }
  }
  if (start == '-') ++cnt;
  return cnt;
}

int main() {
  int T;
  string s;

  cin >> T;

  for (int t = 0; t < T; ++t) {
    cin >> s;
    cout << "Case #" << t + 1 << ": " << solve(s) << "\n";
  }
}