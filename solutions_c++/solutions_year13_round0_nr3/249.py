#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include <gmpxx.h>

mpz_class MakePalindrome(mpz_class n, int middle) {
  std::ostringstream oss;
  oss << n;
  std::string str = oss.str();
  std::string::size_type len = str.length();
  for (std::string::size_type i = middle; i < len; i++) {
    str += str[len - i - 1];
  }
  return mpz_class(str);
}

bool IsPalindrome(mpz_class n) {
  std::ostringstream oss;
  oss << n;
  std::string str = oss.str();
  std::string::size_type len = str.length();
  for (std::string::size_type i = 0; i < len / 2; i++) {
    if (str[i] != str[len - 1 - i]) {
      return false;
    }
  }
  return true;
}

void CheckFairAndSquareNumbers(mpz_class n, int middle, std::vector<mpz_class>& fsns) {
  mpz_class number = MakePalindrome(n, middle);
  mpz_class fsn = number * number;
  // check?
  fsns.push_back(fsn);
}

void FindFairAndSquareNumbers(
    int numDigits,
    int digit,
    int remaining,
    mpz_class number,
    std::vector<mpz_class>& fsns) {
  int begin = (digit == 1) ? 1 : 0;
  if (digit < numDigits) {
    for (int d = begin; d * d * 2 <= remaining; d++) {
      FindFairAndSquareNumbers(numDigits, digit + 1, remaining - d * d * 2, number * 10 + d, fsns);
    }
  } else {
    for (int d = begin; d * d <= remaining; d++) {
      CheckFairAndSquareNumbers(number * 10 + d, 1, fsns);
      if (d * d * 2 <= remaining) {
        CheckFairAndSquareNumbers(number * 10 + d, 0, fsns);
      }
    }
  }
}

std::vector<mpz_class> ComputeFairAndSquareNumbers(int numQuadDigits) {
  std::vector<mpz_class> fsns;
  for (int n = 1; n <= numQuadDigits; n++) {
    FindFairAndSquareNumbers(n, 1, 9, 0, fsns);
  }
  std::sort(fsns.begin(), fsns.end());
  return fsns;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::vector<mpz_class> fsns = ComputeFairAndSquareNumbers(25);
  int numCases;
  std::cin >> numCases;
  for (int caseNum = 1; caseNum <= numCases; caseNum++) {
    mpz_class left, right;
    std::cin >> left >> right;
    std::vector<mpz_class>::size_type leftIndex = std::lower_bound(fsns.begin(), fsns.end(), left) - fsns.begin();
    std::vector<mpz_class>::size_type rightIndex = std::upper_bound(fsns.begin(), fsns.end(), right) - fsns.begin();
    std::vector<mpz_class>::size_type number = rightIndex - leftIndex;
    std::cout << "Case #" << caseNum << ": " << number << std::endl;
  }
}
