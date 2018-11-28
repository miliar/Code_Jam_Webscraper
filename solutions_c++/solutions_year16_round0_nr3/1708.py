#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
using namespace std;
using namespace boost::multiprecision;

const uint256_t NO_DIVISOR = (std::numeric_limits<uint256_t>::max)();

uint256_t findNTDivisor(uint256_t n) {
  if (n % 2 == 0) {
    return 2;
  }

  for (uint256_t divisor = 3; divisor < sqrt(n) + 1 && divisor < 1500; divisor += 2) {
    if (n % divisor == 0) {
      return divisor;
    }
  }

  return n;
}

uint256_t interpret(uint32_t jamCoin, int radix, uint32_t n) {
  uint256_t interpretation = 0;
  for (int bitIndex = 0; bitIndex < n; bitIndex++) {
    uint32_t mask = 1 << bitIndex;
    uint32_t bitVal = jamCoin & mask;

    if (bitVal > 0) {
      interpretation += pow(uint256_t(radix), bitIndex);
    }
  }

  return interpretation;
}

bool isJamCoin(uint32_t &a, uint32_t &n) {
  if ((a & 1) == 0 || (a & (1 << (n - 1))) == 0) {
    return false;
  }

  for (int base = 2; base <= 10; base++) {
    uint256_t interpretation = interpret(a, base, n);
    if (findNTDivisor(interpretation) == interpretation) return false;
  }

  return true;
}


uint32_t clearBit(uint32_t vector, int bitIndex) {
  return vector & ~(1 << bitIndex);
}

uint32_t setBit(uint32_t vector, int bitIndex) {
  return vector | (1 << bitIndex);
}

void backtrackJamCoins(uint32_t &a, int k, uint32_t &n, uint32_t &j, int &solutionsFound) {
  if (k == n) {
    if (isJamCoin(a, n)) {
      cout << interpret(a, 10, n) << " ";

      for (int base = 2; base <= 10; base++) {
        uint256_t interpretation = interpret(a, base, n);
        cout << findNTDivisor(interpretation);
        if (base < 10) cout << " ";
      }
      cout << endl;
      solutionsFound++;
    }
  } else {
    a = clearBit(a, k);
    backtrackJamCoins(a, k + 1, n, j, solutionsFound);

    if (solutionsFound == j) return;

    a = setBit(a, k);
    backtrackJamCoins(a, k + 1, n, j, solutionsFound);
  }
}

void jamCoins(uint32_t n, uint32_t j) {
  int solutionsFound = 0;
  uint32_t a = 0;
  backtrackJamCoins(a, 0, n, j, solutionsFound);
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    uint32_t n, j;
    cin >> n >> j;

    cout << "Case #" << i << ": " << endl;

    jamCoins(n, j);
  }
}
