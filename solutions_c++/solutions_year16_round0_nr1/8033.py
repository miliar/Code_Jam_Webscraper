#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    long long N;
    cin >> N;
    if (N == 0) {
      std::cout << "Case #" << i << ": INSOMNIA" << std::endl;
      continue;
    }

    long long currValue = N;
    bool digitsSeen[10] = {false};
    while (true) {
      long long currN = currValue;
      while (currN) {
        digitsSeen[currN % 10] = true;
        currN /= 10;
      }

      bool digitsFound = true;
      for (int j = 0; j < 10; ++j) {
        if (digitsSeen[j] == false) {
          digitsFound = false;
          break;
        }
      }
      if (digitsFound) {
        std::cout << "Case #" << i << ": " << currValue << std::endl;
        break;
      }

      currValue += N;
    }
  }
}
