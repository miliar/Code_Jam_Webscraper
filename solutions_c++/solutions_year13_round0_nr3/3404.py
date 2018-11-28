#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <utility>
#include <functional>

int A, B;

std::map<long long, int> f;

bool palindrome(long long v) {
  std::ostringstream sout;
  sout << v;
  std::string str(sout.str());
  int n = str.size();
  for (int i = 0; i < n - 1 - i; ++i) {
    if (str[i] != str[n - 1 - i]) return false;
  }
  return true;
}

void init() {
  int count = 0;
  for (long long num = 1; num <= 10000000; ++num) {
    if (palindrome(num) && palindrome(num * num)) {
      //std::cout << num << " " << num * num << std::endl;
      count++;
      f[num * num] = count;
    }
  }
}

int main(int argc, char *argv[]) {
  int t;
  init();
  std::cin >> t;
  for (int i = 0; i < t; ++i) {
    std::cin >> A >> B;
    std::cout << "Case #" << i + 1<< ": "
              << f.lower_bound(B + 1)->second - f.lower_bound(A)->second
              << std::endl;
  }
  return 0;
}
