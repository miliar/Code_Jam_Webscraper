// I feel like knowing this requires more knowledge of numbers than I have. Come
// back to it later.

#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

void mark_digits(int number, vector<bool>& digits) {
  while (number > 9) {
    digits[number % 10] = true;
    number = floor(number / 10);
  }
  digits[number] = true;
}

bool seen_all(vector<bool>& digits) {
  for (auto digit : digits) {
    if (!digit) return false;
  }

  return true;
}

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;

    cout << "Case #" << t << ": ";
    if (N == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      int multiplier = 1;
      vector<bool> digits(10, false);
      mark_digits(N, digits);
      while (!seen_all(digits)) {
        multiplier++;
        mark_digits(N*multiplier, digits);
      }
      cout << N*multiplier << endl;
    }
  }

  return 0;
}