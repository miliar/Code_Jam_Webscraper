#include <iostream>
#include <map>
#include <math.h>

using namespace std;

bool isPalindrome(long long x) {
  long long num = x;
  long long rev = 0;
  while (x > 0) {
    int digit = x % 10;
    rev = rev * 10 + digit;
    x = x / 10;
  }
  return (rev == num);
}

int main(int argc, char** argv) {
  map<long long, long long> fair_sq;
  long long max = 10000000;
  long long count = 0;
  for (long long i = 1; i <= max; ++i) {
    long long sq = i * i;
    if (!isPalindrome(i)) {
      fair_sq[i] = count;
      continue;
    }
    if (!isPalindrome(sq)) {
      fair_sq[i] = count;
      continue;
    }
    count++;
    fair_sq[i] = count;
  }
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    long long A;
    cin >> A;
    long long B;
    cin >> B;
    long long a_root = sqrt(A - 1);
    long long b_root = sqrt(B);
    long long a_count = fair_sq[a_root];
    long long b_count = fair_sq[b_root];
    long long result = b_count - a_count;
    cout << "Case #" << i << ": " << result << endl;
  }
  return 0;
}
