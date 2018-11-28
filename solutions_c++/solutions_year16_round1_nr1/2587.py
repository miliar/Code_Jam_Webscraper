#include <iostream>
#include <string>

void solve()
{
  std::string s;
  std::cin >> s;
  std::string res;
  res += s[0];
  for (int i = 1; i < s.size(); i++) {
    if (s[i] >= res.front()) {
      res.insert(res.begin(), s[i]);
    } else {
      res.push_back(s[i]);
    }
  }
  std::cout << res;
}

int main()
{
  int t;
  std::cin >> t;
  for (int i = 1; i <= t; i++) {
    std::cout << "Case #" << i << ": ";
    solve();
    std::cout << '\n';
  }
}
