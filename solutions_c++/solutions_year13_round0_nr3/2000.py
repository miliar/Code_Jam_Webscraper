#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

unsigned int digits(unsigned __int64 number) {
  int count = 0;
  while (number > 0) {
    number /= 10;
    count++;
  }
  return count;
}

unsigned int digit(unsigned __int64 number, int index) {
  // shift digits
  for (int i = 0;i<index;i++)
    number /= 10;

  return int(number - __int64(number / 10) * 10);
}

bool isPalindrome(unsigned __int64 number) {
  int noDigits = digits(number);
  for (unsigned int i = 0;i<floor(noDigits/2.0);i++) {
    if (digit(number, i) != digit(number, noDigits - i - 1))
      return false;
  }
  return true;
}

// returns the sqrt of an __int64 rounded up
__int64 findSQRT(__int64 number) {
  __int64 s = __int64(sqrt(double(number)));

  // move down
  while (s*s > number) s--;

  // move up
  while (s*s < number) s++;

  return s;
}

int main (int argc, const char **argv) {
  unsigned __int64 noCases;
    
  if (argc != 2) {
    std::cout << "syntax: exe file" << std::endl;
    return 1;
  }

  std::ifstream input;
  input.open(argv[1]);
  if (!input.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::string line;
  getline(input, line);
  std::stringstream ss(line);

  ss >> noCases;

  if (noCases > 100) {
    std::cout << "T exceeds 100" << std::endl;
  }

  std::ofstream output;
  output.open("result.txt");

  for (unsigned int i = 1;i<=noCases;i++) {
    int count = 0;
    output << "Case #" << i << ": ";
    std::cout << "Case #" << i << ": ";

    __int64 lower, upper;
    __int64 lowerSearchBound, upperSearchBound;
    
    getline(input, line);
    ss = std::stringstream(line);
    ss >> lower >> upper;
    lowerSearchBound = findSQRT(lower);
    upperSearchBound = findSQRT(upper);

    for (__int64 j = lowerSearchBound;j<=upperSearchBound;j++) {
      if (isPalindrome(j) && isPalindrome(j*j) && j*j <= upper) {
        count++;
      }
    }

    output << count << std::endl;
    std::cout << count << std::endl;
  }

  input.close();
  output.close();

  return 0;
}