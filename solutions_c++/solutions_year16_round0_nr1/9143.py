#include <iostream>
#include <vector>

using namespace std;

unsigned long markDigits(unsigned long digits, unsigned long n) {
  while (n > 0) {
    unsigned long q = n / 10;
    unsigned long r = n - (q * 10);
    unsigned long digit = 1 << r;
    digits |= digit;
    n = q;
  }
  return digits;
}

void solve() {
  unsigned long n;
  cin >> n;
  if (n == 0) {
    cout << "INSOMNIA" << endl;
    return;
  }
  unsigned long digits = markDigits(0, n);
  unsigned long i = 1;
  while (digits != 0x3FF) {
    i++;
    digits = markDigits(digits, i * n);
  }
  cout << i * n << endl;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i ++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
