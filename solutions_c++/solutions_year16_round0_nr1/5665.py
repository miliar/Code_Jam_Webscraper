#include <iostream>
#include <cstring>

using namespace std;

static int counting_sheep(int N);

int main() {
  int test_cases;
  cin >> test_cases;

  for (int i = 1; i <= test_cases; ++i) {
    int N;
    cin >> N;
    int last_number = counting_sheep(N);
    if (last_number >= 0) {
      cout << "Case #" << i << ": " << last_number << endl;
    } else {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
  }
  
  return 0;
}

int counting_sheep(int N) {
  if (N == 0) return -1;

  static char digits[8];
  static bool numbers[10];

  *digits = '\0';
  for (bool& number : numbers) number = false;

  bool done = false;
  int result = 0;
  int multiplier = 1;
  while (!done) {
    result = N * multiplier++;
    //cout << result << ": ";
    sprintf(digits, "%d", result);
    for (char& digit : digits) {
      int digit_value = digit - 48;
      if (digit_value >= 0 && digit_value <= 9) {
        //cout << "   " << digit_value;
        numbers[digit_value] = true;
      } else {
        break;
      }
    }
    //cout << endl;
    bool all_numbers = true;
    for (bool number : numbers) {
      if (!number) {
        all_numbers = false;
        break;
      }
    }
    if (all_numbers) done = true;
  }
  return result;
}