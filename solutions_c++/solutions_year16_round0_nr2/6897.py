#include <bits/stdc++.h>

using namespace std;

void solveTest() {
  string s;
  cin >> s;
  std::reverse(s.begin(), s.end());
  char prev = '+';
  int ans = 0;
  for (char c : s) {
    if (c != prev) {
      ans++;
    }
    prev = c;
  }
  cout << ans << "\n";
}

int main() {
  int tn;
  cin >> tn;
  for (int tc = 0; tc < tn; tc++) {
    cout << "Case #" << (tc + 1) << ": ";
    solveTest();
  }
  return 0;
}
