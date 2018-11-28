#include <cstdio>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

void uniq(std::vector<char> &pancakes) {
  auto i = std::adjacent_find(pancakes.begin(), pancakes.end());
  while (i != pancakes.end()) {
    pancakes.erase(i);
    i = std::adjacent_find(pancakes.begin(), pancakes.end());
  }
}

int main() {
  uint32_t T;

  scanf("%u", &T);

  for (size_t t = 0; t < T; ++t) {
    std::string S;
    std::cin >> S;
    std::vector<char> pancakes;
    pancakes.reserve(S.length());
    for (const auto &it : S) {
      pancakes.push_back(it);
    }
    uniq(pancakes);

    printf("Case #%d: ", (t + 1));
    if (pancakes[pancakes.size() - 1] == '+') {
      printf("%d\n", pancakes.size() - 1);
    }
    else {
      printf("%d\n", pancakes.size());
    }
  }
  return 0;
}
