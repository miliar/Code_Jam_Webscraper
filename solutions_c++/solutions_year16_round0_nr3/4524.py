#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

namespace {
  vector<long long> generate_digits(long long base2_digit) {
    vector<long long> digits = vector<long long>(9, 0LL);
    vector<long long> bases = vector<long long>(9, 1LL);
    digits[0] = base2_digit;

    while (base2_digit != 0) {
      long long a = base2_digit % 2;
      for (int l = 1; l <= 8; ++l) {
	digits[l] += a * bases[l];
	bases[l] *= (l+2);
      }
      base2_digit /= 2;
    }

    return digits;
  }

  long long prime_check(long long digit) {
    long long div = 3;
    double tmp = static_cast<double>(digit);
    long long limit = static_cast<long long>(sqrt(tmp) +1);

    while (div <= limit)
      {
	if (digit % div == 0) {
	  return div;
	}
	div += 2;
      }
    return 1;
  }

  string write_base2(long long digit) {
    string res = "";
    while (digit != 0) {
      if (digit % 2 == 0) res = "0" + res;
      else res = "1" + res;
      digit /= 2;
    }
    return res;
  }

  bool check(const vector<long long>& digits) {
    vector<long long> res;
    for (int l = 0; l <= 8; ++l) {
      long long r = prime_check(digits[l]);
      if (r == 1LL) return false;
      res.push_back(r);
    }
    cout << write_base2(digits[0]);
    for (int l = 0; l <= 8; ++l) {
      cout << " " << res[l];
    }
    cout << endl;
    return true;
  }
}

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    int N, J;
    cin >> N >> J;

    cout << "Case #" << t << ":" << endl;

    int base2_num = 1;
    for (int j = 1; j < N; ++j) {
      base2_num *= 2;
    }
    base2_num += 1;

    int generated = 0;
    while (1) {
      vector<long long> digits = generate_digits(base2_num);
      if (check(digits)) generated++;
      if (generated == J) break;
      base2_num += 2;
    }
  }
  return 0;
}
