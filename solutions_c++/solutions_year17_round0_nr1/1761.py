/* Copyright 2017 Yusuf Hussein
 */
#include <iostream>
#include <string>
#include <queue>
int solve(std::string s, int k) {
  std::queue<int> q;
  int len = s.size();
  int ret = 0;
  for (int i = 0; i < len; ++i) {
    if (!q.empty() && q.front() == i) {
      q.pop();
    }
    if (q.size() & 1) {
      s[i] = s[i] == '-' ? '+' : '-';
    }
    if (i + k <= len && s[i] == '-') {
      s[i] = '+';
      ++ret;
      q.push(i + k);
    }
    if (s[i] == '-') {
      return -1;
    }
  }
  return ret;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    std::string s;
    int k;
    std::cin >> s >> k;
    int ans = solve(s, k);
    std::cout << "Case #" << t << ": ";
    if (ans == -1) {
      std::cout << "IMPOSSIBLE\n";
    } else {
      std::cout << ans << '\n';
    }
  }
}
