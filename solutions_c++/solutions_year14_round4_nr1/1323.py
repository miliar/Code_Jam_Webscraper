#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int t;
  std::cin >> t;
  for (int x = 1; x <= t; x++) {
    int n, c;
    std::cin >> n >> c;
    std::vector<int> s(n);
    for (int i = 0; i < n; i++) {
      std::cin >> s[i];
    }
    int y = 0;
    std::sort(s.begin(), s.end());
    while (!s.empty()) {
      ++y;
      int r = c - s.back();
      s.pop_back();
      auto it = std::upper_bound(s.begin(), s.end(), r);
      if (it == s.begin()) {
        continue;
      }
      s.erase(--it);
    }
    std::cout << "Case #" << x << ": " << y << std::endl;
  }
}
