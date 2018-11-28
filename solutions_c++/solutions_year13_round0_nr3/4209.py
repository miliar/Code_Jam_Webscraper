#include <cstdio>
#include <cmath>
#include <sstream>
#include <vector>

using namespace std;

vector<long long> fair;

bool isSorted(const vector<long long>& v) {
  for (int i = 1; i < v.size(); ++i) {
    if (v[i - 1] > v[i]) {
      return false;
    }
  }
  return true;
}

long long construct(int num, int digit = -1) {
  stringstream ss;
  ss << num;
  string numString = ss.str();
  stringstream resStream;
  resStream << num;
  if (digit != -1) {
    resStream << digit;
  }
  reverse(numString.begin(), numString.end());
  resStream << numString;
  long long res;
  resStream >> res;
  return res;
}

long long constructFast(int num, int digit = -1) {
  long long res = num;
  if (digit != -1) {
    res *= 10;
    res += digit;
  }
  while (num) {
    res *= 10;
    res += num % 10;
    num /= 10;
  }
  return res;
}

bool isPalindrome(long long num) {
  stringstream ss;
  ss << num;
  string s1 = ss.str(), s2 = ss.str();
  reverse(s2.begin(), s2.end());
  return s1 == s2;
}

bool isPalindromeFast(long long num) {
  long long rev = 0;
  long long orig = num;
  while (num) {
    rev *= 10;
    rev += num % 10;
    num /= 10;
  }
  return orig == rev;
}

bool isFairSquare(long long num) {
  long long s = sqrt(num);
  if (s * s != num) {
    return false;
  }
  return isPalindromeFast(s);
}

int main() {
  for (int i = 0; i <= 1e7 + 100; ++i) {
    if (i % 1000 == 0) {
      fprintf(stderr, "processed %d\n", i);
    }
    long long cur = constructFast(i);
//    printf("cur is %lld\n", cur);
    if (isFairSquare(cur)) {
      fair.push_back(cur);
    }
    for (int middle = 0; middle < 10; ++middle) {
      long long cur = constructFast(i, middle);
      if (isFairSquare(cur)) {
        fair.push_back(cur);
      }
    }
  }
  fprintf(stderr, "There are %u nums; is sorted: %d\n", fair.size(), isSorted(fair));
  for (int i = 0; i < fair.size(); ++i) {
    fprintf(stderr, "%lld\n", fair[i]);
  }

  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    long long A, B;
    scanf("%lld %lld", &A, &B);
    int count = 0;
    for (int i = 0; i < fair.size(); ++i) {
      if (fair[i] >= A && fair[i] <= B) {
        ++count;
      }
    }
    printf("Case #%d: %d\n", t + 1, count);
  }
}
