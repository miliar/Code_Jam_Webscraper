#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

const int MOD = 10000000000;

class Number {
public:
  Number(int init) {
    num.push_back(init);
  }

  void time(int n) {
    int carry = 0;
    for (int i = 0; i < num.size(); i++) {
      num[i] = num[i] * n + carry;
      carry = num[i] / MOD;
      num[i] %= MOD;
    }
    if (carry != 0) {
      num.push_back(carry);
    }
  }

  void add(int n) {
    int carry = n;
    for (int i = 0; i < num.size(); i++) {
      num[i] += carry;
      carry = num[i] / MOD;
      num[i] %= MOD;
    }
    if (carry != 0) {
      num.push_back(carry);
    }
  }

  bool canDivid(int n) {
    if (num.size() == 1 && num[0] == n) return false;

    long long carry = 0;
    for (int i = num.size() - 1; i >= 0; i--) {
      carry = (num[i] + carry * MOD) % n;
    }
    return carry == 0;
  }

private:
  vector<long long> num;
};

Number convert(const string& digits, int base) {
  Number result(0);
  for (int i = 0; i < digits.length(); i++) {
    result.time(base);
    result.add(digits[i] - '0');
  }
  return result;
}

bool isPrime(Number num) {
  long long limit = 1000000;
  for (long long i = 2; i <= limit; i++) {
    if (num.canDivid(i)) return false;
  }
  return true;
}

bool isValide(const string& digits) {
  for (int i = 2; i <= 10; i++) {
    Number num = convert(digits, i);
    if (isPrime(num)) return false;
  }
  return true;
}

bool next_digits(string& digit) {
  for (int i = digit.length() - 2; i >= 0; i--) {
    if (digit[i] == '0') {
      digit[i] = '1';
      return true;
    }
    else {
      digit[i] = '0';
    }
  }
  return false;
}

long long getNontrivialDivisor(Number num) {
  long long limit = 1000000;
  for (long long i = 2; i <= limit; i++) {
    if (num.canDivid(i)) return i;
  }

  return -1;
}

int main() {

  int N = 32;
  int J = 500;
 // for (int N = 2; N <= 10; N++) {
    string digits(N, '0');
    digits[0] = '1';
    digits[N - 1] = '1';

    cout << "Case #1:" << endl;
    do {
      if (isValide(digits)) {
        cout << digits;
        for (int i = 2; i <= 10; i++) {
          Number num = convert(digits, i);
          cout << ' ' << getNontrivialDivisor(num);
        }
        cout << endl;
        J--;
        if (J == 0) break;
      }
    } while (next_digits(digits));
  //}

  return 0;
}
