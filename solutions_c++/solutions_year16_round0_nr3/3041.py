#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char IN_FILE[] = "input.txt";
const char OUT_FILE[] = "output.txt";

inline int getBit(const int mask, const int bit) {
  return (mask >> bit) & 1;
}

inline int64_t convertToBase(const int n, const int mask, const int64_t base) {
  int64_t basePow = 1, value = 0;
  for (int i = 0; i < n; ++i, basePow *= base)
    if (getBit(mask, i))
      value += basePow;
  return value;
}

inline int64_t findDivisor(const int64_t n) {
  if (n > 2 && n % 2 == 0)
    return 2;
  for (int64_t d = 3; d * d <= n; d += 2)
    if (n % d == 0)
      return d;
  return -1;
}

int main() {
  ifstream cin(IN_FILE);
  ofstream cout(OUT_FILE);

  int testCount;
  cin >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int N, J;
    cin >> N >> J;
    cout << "Case #" << test << ":\n";
    for (int mask = 0; mask < (1 << (N - 2)) && J > 0; ++mask) {
      int realMask = (1 << (N - 1)) | (mask << 1) | 1;
      vector<int> divisors;
      bool valid = true;
      for (int base = 2; base <= 10 && valid; ++base) {
        int64_t value = convertToBase(N, realMask, base);
        int64_t divisor = findDivisor(value);
        if (divisor != -1)
          divisors.push_back(divisor);
        else
          valid = false;
      }
      if (valid) {
        --J;
        for (int i = N - 1; i >= 0; --i)
          cout << getBit(realMask, i);
        for (int i = 0; i < int(divisors.size()); ++i)
          cout << " " << divisors[i];
        cout << "\n";
      }
    }
  }

  cin.close();
  cout.close();
  return 0;
}
