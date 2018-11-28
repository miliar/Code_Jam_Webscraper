#include <iostream>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int K, C, S;
    cin >> K >> C >> S;
    std::cout << "Case #" << i << ":";
    if (S < K) {
      std::cout << "IMPOSSIBLE" << std::endl;
    } else {
      for (int j = 1; j <= K; ++j) {
        std::cout << " " << j;
      }
      std::cout << std::endl;
    }
  }
}
