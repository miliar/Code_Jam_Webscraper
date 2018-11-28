#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#if DEBUG
void print(std::vector<int64_t> array) {
  for (auto element : array) {
    std::cout << element << "\t";
  }
  std::cout << std::endl;
}
#endif

std::vector<int64_t> getSelectedRow(void) {
  int64_t A;
  std::cin >> A;
  auto cards = std::vector<std::vector<int64_t> >(4, std::vector<int64_t>(4));
  for (int64_t i = 0; i < 4; ++i) {
    for (int64_t j = 0; j < 4; ++j) {
      std::cin >> cards[i][j];
    }
  }
  return cards[A - 1];
}

int main(void) {
  int64_t T;
  std::cin >> T;
  for (int64_t t = 0; t < T; ++t) {
    auto first = getSelectedRow();
    auto second = getSelectedRow();
    std::sort(first.begin(), first.end());
    std::sort(second.begin(), second.end());

    auto intersection = std::vector<int64_t>(4);
    auto iterator = std::set_intersection(
        first.begin(), first.end(), second.begin(), second.end(), intersection.begin());

    auto size = iterator - intersection.begin();

#if DEBUG
    std::cout << "first: "; print(first);
    std::cout << "second: "; print(second);
    intersection.resize(size);
    std::cout << "intersection: "; print(intersection);
#endif

    std::cout << "Case #" << t + 1 << ": ";
    switch (size) {
    case 0:
      std::cout << "Volunteer cheated!" << std::endl;
      break;
    case 1:
      std::cout << *(intersection.begin()) << std::endl;
      break;
    default:
      std::cout << "Bad magician!" << std::endl;
      break;
    }
  }
  return EXIT_SUCCESS;
}

