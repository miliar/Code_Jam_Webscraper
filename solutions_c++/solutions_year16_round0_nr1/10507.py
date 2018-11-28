#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <sstream>
#include <functional>

using namespace std;
using namespace std::placeholders;

struct Digits {
  Digits();
  Digits &operator<<(uint64_t n);
  array<size_t, 10> digits;
  bool full() const;
  int16_t unique_digits() const;
};

ostream &operator<<(ostream &o, const Digits &digits) {
  string sep;
  int index = 0;
  for(auto d: digits.digits) {
    o << sep << index++ << "=" << d;
    sep = ", ";
  }
  return o << "]";
}

Digits::Digits() : digits{0}
{
}

Digits& Digits::operator<<(uint64_t n)
{
  stringstream s;
  s << n;
  for(auto digit: s.str())
    digits[digit - '0']++;
  return *this;
}

bool Digits::full() const
{
  return unique_digits() == 10;
}

int16_t Digits::unique_digits() const
{
  int16_t unique_digits;
  for(auto digit: digits)
    if(digit>0)
      unique_digits++;
  return unique_digits;
}



int64_t solve(uint64_t number) {
  Digits digits;
  int i = 0;
  if(number == 0)
    return -1;
  uint64_t new_number;
  while(true) {
    new_number = number * ++i;
    digits << new_number;
//     cerr << "i=" << i << ", number=" << new_number << ", digits=" << digits << endl;
    if(digits.full())
      return new_number;
  }
}

int main(int argc, char **argv) {
  size_t test_cases;
  cin >> test_cases;
  for(size_t i = 0; i< test_cases; i++) {
    uint64_t n;
    cin >> n;
    auto solved = solve(n);
    cout << "Case #" << i+1 << ": ";
    if(solved > -1)
      cout << solved;
    else
      cout << "INSOMNIA";
    cout << endl;
  }
  return 0;
}

