#include <iostream>


using namespace std;


typedef unsigned long long ulong;

void print_digits(bool* digits) {
  for (int i=0; i < 10; i++) {
    cout << digits[i] << ' ';
  }
  cout << endl;
}

void mark_digits(ulong n, bool* digits) {
  while (n) {
    int d = n % 10;
    digits[d] = true;
    n = n / 10;
  }
}

bool all_found(bool* digits) {
  for (int i=0; i < 10; i++) {
    if (!digits[i])
      return false;
  }
  return true;
}

ulong get_last(ulong n) {
  bool digits[10];
  fill(digits, digits + 10, false);
  mark_digits(n, digits);
  //print_digits(digits);
  ulong nn = n;
  while( ! all_found(digits) ) {
    nn += n;
    mark_digits(nn, digits);
    //  print_digits(digits);
    //  cout << idx << endl;
  }
  return nn;
}

int main() {

  int T;
  unsigned long long n;
  cin >> T;

  for (int i=0; i < T; i++ ) {
    cin >> n;
    cout << "Case #" << i + 1 << ": ";
    if ( n == 0 ) {
      cout << "INSOMNIA" << endl;
    } else {
      ulong fin = get_last(n);
      cout << fin << endl;
    }
  }
}
