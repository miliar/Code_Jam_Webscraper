#include <iostream>
using namespace std;

typedef long long bigint;

int main() {
  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; case_num++) {
    bigint N;
    cin >> N;
    if (N == 0) {
      cout << "Case #" << case_num << ": INSOMNIA\n";
      continue;
    }
    bigint i = 0;
    int seen_digits = 0;
    while (seen_digits != 0x3ff) {
      i += 1;
      bigint k = i * N;
      while (k > 0) {
        seen_digits |= 1 << (k % 10);
        k /= 10;
      }
    }
    cout << "Case #" << case_num << ": " << i * N << "\n";
  }
  return 0;
}
