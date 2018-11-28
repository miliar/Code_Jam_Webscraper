#include <algorithm>
#include <cmath>
#include <cstdint>
#include <complex>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

int64_t WordId(const std::string& word) {
  int64_t id = 0;
  for (char ch : word) {
    id *= 26;
    id += ch - 'a';
  }
  return id;
}

int n;
std::vector<std::unordered_set<std::string>> S;
int y;

template <class C1, class C2>
int Intersect(const C1& a, const C2& b) {
  int c = 0;
  for (const auto& x : a) {
    if (b.count(x)) {
      c++;
    }
  }
  return c;
}

template <class C1, class C2, class C3>
int Intersect2(const C3& s, const C1& a, const C2& b) {
  int c = 0;
  for (const auto& x : s) {
    if (!a.count(x) && b.count(x)) {
      c++;
    }
  }
  return c;
}

void Search(int k, int c, const std::unordered_set<std::string>& a, const std::unordered_set<std::string>& b) {
  if (c >= y) {
    return;
  }
  if (k == n) {
    y = c;
    return;
  }
  int c2 = Intersect2(S[k], a, b);
  if (c + c2 < y) {
    std::unordered_set<std::string> a2(a);
    a2.insert(S[k].begin(), S[k].end());
    Search(k + 1, c + c2, a2, b);
  }
  c2 = Intersect2(S[k], b, a);
  if (c + c2 < y) {
    std::unordered_set<std::string> b2(b);
    b2.insert(S[k].begin(), S[k].end());
    Search(k + 1, c + c2, a, b2);
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    // Input
    std::cin >> n >> std::ws;
    S.clear();
    std::string line;
    for (int j = 0; j < n; j++) {
      std::getline(std::cin, line);
      std::istringstream sen(line);
      std::string word;
      S.emplace_back();
      while (sen >> word) {
        S.back().insert(word);
      }
    }
    // Solve
    std::unordered_set<std::string> english(S[0].begin(), S[0].end());
    std::unordered_set<std::string> french(S[1].begin(), S[1].end());
    int c = Intersect(english, french);
    y = std::numeric_limits<int>::max();
    Search(2, c, english, french);
    // Output
    std::cout << "Case #" << i + 1 << ": " << y << std::endl;
  }
}
