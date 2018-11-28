#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <map>
#include <unordered_map>
#include <cstdint>
std::string global_max;
void combinations(std::string a, std::string b) {
 if (b.length() == 0) {
  if (a > global_max) {
      global_max = a;
    }
    return;
  }
  std::string x = a;

  a.insert(0, 1, b[0]);
  combinations(a, b.substr(1));

  x.push_back(b[0]);
  combinations(x, b.substr(1));
}

int main() {
  int N;
  std::cin >> N;
  for (int i = 1; i <= N; i++) {
    std::string str;
    std::cin >> str;
    global_max = str;
    combinations(std::string(1, str[0]), str.substr(1));
    std::cout << "Case #" << i << ": " << global_max << std::endl;
  }

  return 0;
}
