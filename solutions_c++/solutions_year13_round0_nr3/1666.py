#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <set>

using std::string;
using std::vector;

std::set<long long> FPNumbers;

bool IsPalindrome(long long number) {
  std::stringstream ss;
  ss << number;
  string s;
  ss >> s;
  
  size_t len = s.size();
  for (size_t index = 0; index < len / 2; ++index) {
    if (s[index] != s[len - index - 1])
      return false;
  }

  return true;
}

void CalculateFPNumbersCount(long long A, long long B) {
  //int result = 0;
  long long A_sqr = sqrt((double)A);
  long long B_sqr = sqrt((double)B);
  for (long long number = A_sqr; number <= B_sqr; ++number) {
    long long sqr = number * number;
    //result += (IsPalindrome(number) && IsPalindrome(sqr) && sqr >= A && sqr <= B);
    if (IsPalindrome(number) && IsPalindrome(sqr) && sqr >= A && sqr <= B)
      FPNumbers.insert(sqr);
  }

  //return result;
}

int FPNumbersCount(long long A, long long B) {
  int result = 0;

  for (std::set<long long>::const_iterator it = FPNumbers.begin();
       it != FPNumbers.end(); ++it) {
    if ((*it) >= A && (*it) <= B)
      ++result;
  }

  return result;
}

void Solve() {
  CalculateFPNumbersCount(1, 100000000000000);
  int T;
  scanf("%d\n", &T);
  for (int test_number = 1; test_number <= T; ++test_number) {
    long long A, B;
    scanf("%lld%lld", &A, &B);
    printf("Case #%d: %d\n", test_number, FPNumbersCount(A, B));
  }
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  Solve();
  return 0;
}