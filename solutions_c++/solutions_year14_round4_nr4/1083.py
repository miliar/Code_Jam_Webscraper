// Only for the small case
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

int m;
int n;
std::vector<std::string> s;
int x;
int y;

void Search(int depth, std::vector<std::unordered_set<std::string>> generated) {
  if (depth == m) {
    int x2 = 0;
    for (int i = 0; i < n; i++) {
      x2 += generated[i].size();
    }
    if (x2 > x) {
      x = x2;
      y = 1;
    } else if (x2 == x) {
      ++y;
    }
    return;
  }
  for (int i = 0; i < n; i++) {
    std::vector<std::unordered_set<std::string>> v = generated;
    for (int j = 0; j <= s[depth].length(); j++) {
      v[i].insert(s[depth].substr(0, j));
    }
    Search(depth + 1, v);
  }
}

int main() {
  int t;
  std::cin >> t;
  for (int i = 1; i <= t; i++) {
    std::clog << i << std::endl;
    std::cin >> m >> n;
    s.resize(m);
    for (int k = 0; k < m; k++) {
      std::cin >> s[k];
    }
    x = -1;
    y = 0;
    std::vector<std::unordered_set<std::string>> v(n);
    Search(0, v);
    std::cout << "Case #" << i << ": " << x << " " << y << std::endl;
  }
}
