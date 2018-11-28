#include <iostream>
using namespace std;

size_t digitsMask(size_t n) {
  size_t ans = 0;
  while (n > 0) {
    ans |= 1 << (n % 10);
    n /= 10;
  }
  return ans;
}

void dw(size_t caseNo) {
  size_t N;
  cin >> N;
  if (N == 0) {
    cout << "Case #" << caseNo << ": INSOMNIA" << endl;
    return;
  }

  size_t ans = N;
  size_t dm = digitsMask(ans);
  while (dm < 1023) {
    ans += N;
    dm |= digitsMask(ans);
  }

  cout << "Case #" << caseNo << ": " << ans << endl;
}

int main() {
  size_t T;
  cin >> T;
  for (size_t i = 1; i <= T; i++) {
    dw(i);
  }
}

