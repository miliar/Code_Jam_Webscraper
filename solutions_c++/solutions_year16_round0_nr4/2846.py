#include <algorithm>
#include <array>
#include <iostream>
#include <ios>
#include <istream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

long power(long base, long exp) {
  long ret = 1;
  for (; exp != 0; exp >>= 1) {
    if (exp & 1) ret *= base;
    base *= base;
  }

  return ret;
}

int main(int argc, char *argv[]) {
  cout.precision(8); cout.setf(ios_base::showpoint);
  long t; cin >> t;

  for (long i = 1; i <= t; ++i) {
    long k, c, s; cin >> k >> c >> s;
    cout << "Case #" << i << ":";

    if ((c == 1 && s < k) || s * 2 < k) {
      cout << " IMPOSSIBLE" << endl;
      continue;
    }

    if (c == 1) {
      for (long j = 0; j < k; j += 1) {
        cout << " " << j + 1;
      }
    } else {
      for (long j = 0; j < k; j += 2) {
        if (j == k-1) {
          cout << " " << j*power(k, c-1) + 1;
        } else {
          cout << " " << j*power(k, c-1) + j + 2;
        }
      }
    }

    cout << endl;
  }

  return 0;
}
