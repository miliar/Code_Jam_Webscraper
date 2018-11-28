// Google Code Jam
// Qualification Round 2013
//
// Problem C. Fair and Square
//
// Compiled with C++11 and clang++
// clang++ -std=c++11 -stdlib=libc++ -Wall

#include <cmath>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::max;

bool palindrome(long n) {
  if (n < 10) {
    return true;
  }

  long factor = 10;
  while (n / factor > 0) {
    factor *= 10;
  }
  factor /= 10;

  while (n > 0) {
    long first = n / factor;
    long last = n % 10;
    if (first != last) {
      return false;
    }
    n = (n - first * factor) / 10;
    factor /= 100;
  }
  return true;
}

int main(int argc, char* argv[]) {
  int t;
  cin >> t;
  for (int testCase = 1; testCase <= t; ++testCase) {
    long a, b;
    cin >> a >> b;

    long first = sqrt(a);
    if (first * first < a) {
      ++first;
    }
    long last = sqrt(b);
    long result = 0;
    for (long i = first; i <= last; ++i) {
      if (palindrome(i) && palindrome(i * i)) {
        ++result;
      }
    }
    cout << "Case #" << testCase << ": " << result << endl;
  }
  return 0;
}
