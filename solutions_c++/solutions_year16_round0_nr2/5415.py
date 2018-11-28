#include <bits/stdc++.h>


const int maxl = 100;

std::string s = "";

int f (const std::string& s) {
  if (s.size() == 0) return 0;
  int i = 0;
  int ans = 0;
  while (i < s.size()) {
    char ch = s[i];
    i += 1;
    while (i < s.size() && s[i] == ch) {
      i += 1;
    }
    if (ch == '-' || (ch == '+' && i < s.size())) ans += 1;
  }
  return ans;
}

void solution () {
  std::getline(std::cin, s);
  // std::cout << s << std::endl;
  std::cout << f(s) << std::endl;
}

int main () {
  // std::ios_base::sync_with_stdio(false);

  // std::freopen("x.in", "r", stdin);
  // std::freopen("B-small-attempt0.in", "r", stdin);
  std::freopen("B-large.in", "r", stdin);

  std::freopen("B.out", "w", stdout);

  int T = 0;
  std::cin >> T;
  std::cin.ignore(10000, '\n');
  for (int i = 1 ; i <= T ; i += 1) {
    std::cout << "Case #" << i << ": ";
    solution();
  }

  return 0;
}
