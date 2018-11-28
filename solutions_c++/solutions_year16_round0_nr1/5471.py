#include <string>
#include <vector>
#include <iostream>
#include <map>

using std::cin;
using std::cout;
using std::endl;
using std::map;

void initialize_map(map<int, int> &digits) {
  for (int i = 0; i < 10; ++i)
  {
    digits[i] = i;
  }
}

void digits_for_number(const int &n, map<int, int> &digits) {
  int aux = n;
  int digit;

  while (aux > 0) {

    int digit = aux % 10;

    map<int, int>::iterator iter = digits.find(digit);
    if (iter != digits.end())
    {
      digits.erase(iter);
    }

    aux /= 10;
  }
}

int count_sheep(int &n) {
  int last_number = -1;
  map<int, int> digits;
  initialize_map(digits);

  if (n > 0) {
    int i = 1;
    while (!digits.empty())
    {
      last_number = i++ * n;
      digits_for_number(last_number, digits);

    }
  }

  return (digits.empty()) ? last_number : -1;
}

int main() {
  int T = 0, n = 0, result = 0;
  cin >> T;

  for (int i = 0; i < T; ++i)
  {
    cin >> n;
    result = count_sheep(n);
    if (result != -1)
    {
      cout <<  "Case #" << i + 1 << ": " << result << endl;
    } else {
      cout <<  "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
    }

  }


  return 0;
}
