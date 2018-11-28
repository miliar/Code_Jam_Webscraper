#include <iostream>
#include <cstdint>
using namespace std;

int count(int64_t num) {
  int bit = 0;
  while(num > 0) {
    bit |= 1 << (num % 10);
    num /= 10;
  }
  return bit;
}

int64_t solve(int64_t n) {
  int bit = 0;
  uint64_t ret;
  for(int64_t i = 1; bit != (1 << 10) - 1; i++) {
    ret = i * n;
    bit |= count(ret);
  }
  return ret;
}

int main() {
  int tc;
  cin >> tc;
  for(int caze = 1; caze <= tc; caze++) {
    cout << "Case #" << caze << ": ";
    int64_t n;
    cin >> n;
    if(n == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << solve(n) << endl;
    }
  }
}
