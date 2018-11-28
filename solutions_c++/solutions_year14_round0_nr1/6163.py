#include "iostream"
#include "vector"
#include "algorithm"

int main() {
  int T;
  std::cin >> T;
  for (int t = 1, r; t <= T; ++t) {
    std::vector<int> first, second, intersect;
    std::cin >> r;
    for (int i = 0, x; i < 16; ++i) {
      std::cin >> x;
      if ((r-1)*4 <= i && i < r*4) {
	first.push_back(x);
      }
    }
    std::cin >> r;
    for (int i = 0, x; i < 16; ++i) {
      std::cin >> x;
      if ((r-1)*4 <= i && i < r*4) {
	second.push_back(x);
      }
    }
    std::sort(first.begin(), first.end());
    std::sort(second.begin(), second.end());
    std::set_intersection(first.begin(), first.end(), 
		  second.begin(), second.end(),
		  std::back_inserter(intersect));
    
    std::cout << "Case #" << t << ": ";
    if (intersect.size() == 0) {
      std::cout << "Volunteer cheated!" << std::endl;
    } else if (intersect.size() == 1) {
      std::cout << intersect.front()  << std::endl;
    } else {
      std::cout << "Bad magician!" << std::endl;
    }
  }
  return 0;
}
