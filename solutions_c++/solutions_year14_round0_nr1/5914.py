#include <iostream>
#include <set>
#include <vector>
#include <iterator>

const int N = 4;

int main() {
  std::ios_base::sync_with_stdio(false);
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    int first, second;
    int fc[N][N];
    int sc[N][N];
    std::cin >> first;
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        std::cin >> fc[j][k];
      }
    }
    std::cin >> second;
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        std::cin >> sc[j][k];
      }
    }
    first--;
    second--;
    std::set<int> fs(fc[first], fc[first] + N);
    std::set<int> ss(sc[second], sc[second] + N);
    std::vector<int> common;
    std::set_intersection(fs.begin(), fs.end(), ss.begin(), ss.end(), std::back_inserter(common));
    std::cout << "Case #" << i + 1 << ": ";
    if (common.size() == 0) {
      std::cout << "Volunteer cheated!";
    } else if (common.size() == 1) {
      std::cout << common[0];
    } else {
      std::cout << "Bad magician!";
    }
    std::cout << std::endl;
  }
}
