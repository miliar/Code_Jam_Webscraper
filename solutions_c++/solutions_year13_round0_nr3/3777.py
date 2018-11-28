#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MAX_DIGITS = 101;
vector<int> digits (MAX_DIGITS);

bool is_palindrome(int n) {
  int i = 0;
  while (n != 0) {
    digits[i] = n%10;
    n /= 10;
    ++i;
  }
  for (int j = 0; j < i; ++j) {
    if (digits[j] != digits[i-j-1]) {
      return false;
    }
  }
  return true;
}

unsigned long make_even_palindrome(unsigned long n) {
  unsigned long m = 0;
  unsigned long base = 1;
  unsigned long N = n;
  while (n != 0) {
    base *= 10;
    m *= 10;
    m += n%10;
    n /= 10;
  }
  return base*N + m;
}

unsigned long make_odd_palindrome(unsigned long n) {
  unsigned long m = 0;
  unsigned long base = 1;
  unsigned long N = n;
  while (n >= 10) {
    base *= 10;
    m *= 10;
    m += n%10;
    n /= 10;
  }
  return base*N + m;
}

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    unsigned long A, B;
    cin >> A >> B;

    unsigned long a = floor(sqrt(A));
    unsigned long b = ceil(sqrt(B));

    // NOTE: This is an optimized naive solution, i.e. generate all
    // palindromes between a and b and check if their squares are also
    // palindromes between A and B.

    unsigned long count = 0;
    unsigned long n, p, P;

    //
    // count even palindromes
    // 
    n = 1;
    while (make_even_palindrome(10*n) < a) n *= 10;
    while (make_even_palindrome(n+1) < a)  ++n;
    
    while (make_even_palindrome(n) <= b) {
      unsigned long p = make_even_palindrome(n);
      unsigned long P = p*p;
      if (A <= P && P <= B && is_palindrome(P)) {
        ++count;
      }
      ++n;
    }

    //
    // count odd palindromes
    // 
    n = 1;
    while (make_odd_palindrome(10*n) < a) n *= 10;
    while (make_odd_palindrome(n+1) < a)  ++n;
    
    while (make_odd_palindrome(n) <= b) {

      unsigned long p = make_odd_palindrome(n);
      unsigned long P = p*p;
      if (A <= P && P <= B && is_palindrome(P)) {
        ++count;
      }
      ++n;
    }

    //
    // result
    // 
    cout << "Case #" << t << ": " << count << '\n';
  }
  
  return 0;
}
