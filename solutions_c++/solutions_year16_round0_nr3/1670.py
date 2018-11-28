#include <vector>
#include <string>
#include <iostream>
#include <cassert>

using namespace std;

// TEST
//constexpr int N = 6;
//constexpr int J = 3;
// SMALL
// constexpr int N = 16;
// constexpr int J = 50;
// LARGE
constexpr int N = 32;
constexpr int J = 500;

__uint128_t getDivisor(__uint128_t n) {
  // returns -1 if n is prime
  if (n == 1) {
    throw std::runtime_error("n is 1");
  }
  if (n == 2) {
    return -1;
  }
  if (n % 2 == 0) {
    return 2;
  }
  __uint128_t d = 3;
  while (d*d <= n && d*d <= UINT32_MAX) {
    if (n % d == 0) {
      return d;
    } 
    d += 2;
  }
  return 0;
}

__uint128_t binToCoin(uint64_t bin, uint64_t base) {
  assert(base >= 2);
  assert(base <= 10);

  /* Interpret jam as string of zeroes and ones of length (N-2).
   * Tack on 1 at beginning and end to create potential jam coin.
   */
  uint64_t highPower = 1;
  for (int i = 1; i <= N-1; ++i) {
    highPower *= 2;
  }

  uint64_t fullBin = highPower + 1 + (2 * bin);
  // Now interpret this "binary" number into base BASE
  __uint128_t n = 0;
  __uint128_t mult = 1;
  while (fullBin > 0) {
    uint64_t tail = fullBin % 2;
    if (tail != 0) {
      n += mult;
    }
    mult *= base;
    fullBin /= 2;
  }

  //cout << "Bin " << bin << " base " << base << " rv " << n;
  return n;
}

char* binRep(uint64_t n) {
  static char rv[N+1] = {0};
  rv[0] = '1';
  rv[N-1] = '1';
  rv[N] = '\0';
  for (int i = 1; i < N-1; ++i) {
    if (n % 2 == 0) {
      rv[N-1-i] = '0';
    } else {
      rv[N-1-i] = '1';
    }
    n /= 2;
  }
  return rv;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  assert(T == 1);  

  // TODO
  // DO NOT FORGET N AND J parsing
  // FIXME
  //
  uint64_t upperLimit = 1;
  for (int i = 0; i < (N-2); ++i) {
    upperLimit *= 2;
  }

  vector<int64_t> divisors;

  cout << "Case #1:" << endl;
  int success = 0;
  for (int n = 0; n < upperLimit; ++n) {
    // Create coin in every base, checking for divisors
    divisors.clear();
    for (int b = 2; b <= 10; ++b) {
      const __uint128_t coin = binToCoin(n, b);
      const __uint128_t d = getDivisor(coin);
      if (d > 0) {
        divisors.push_back(d);
      } else {
        break;
      }
    }
    if (divisors.size() == 9) {
      ++success;
      //cout << binRep(n) << " Where n=" << n << "**";
      printf("%s", binRep(n));
      for (const __uint128_t d : divisors) {
        cout << ' ' << (uint64_t)d;
      }
      cout << endl;
    }

    if (success == J) {
      break;
    }
  }


  return 0;
}
