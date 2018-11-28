#include <iostream>
#include <limits>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <vector>

typedef unsigned long long ull;
using namespace std;

void fill(string& output, size_t num, size_t bits) {
  int place = output.size();
  while (bits--) {
    if (num & 1) {
      output[place-2] = '1';
    } else {
      output[place-2] = '0';
    }
    --place;
    num >>= 1;
  }
}

bool isPrime(ull n, ull& divisor) {
  divisor = 1;
  if (n <= 1) {
    return false;
  } else if (n <= 3) {
    return true;
  } else if (0 == (n%2)) {
    divisor = n / 2;
    return false;
  } else if (0 == (n%3)) {
    divisor = n / 3;
    return false;
  } else { 
    ull i = 5;
    while ( (i * i) <= n) {
      if (0 == (n%i)) {
        divisor = n / i;
        return false;
      } else if (0 == (n%(i+2))) {
        divisor = n / (i+2);
        return false;
      }
      i = i + 6;
    }
    return true;
  }
}

void solve(ull N, ull J) {
  size_t stop = pow(2,N-2);
  string start(N, '0');
  start[0] = '1';
  start[N-1] = '1';

  for (size_t num = 0; num < stop; ++num) {
    string candidate = start;
    fill(candidate, num, N-2);
    bool isJamCoin = true;
    vector<ull> factor(11, 0);
    for (unsigned int base = 2; base <= 10; ++base) {
      ull toTest = strtoul(candidate.c_str(), NULL, base);
      ull divisor;
      if (isPrime(toTest, divisor)) {
        isJamCoin = false;
        break;
      } else {
        factor[base] = divisor;
      }
    }
    if (isJamCoin) {
      --J;
      cout << candidate;
      for (size_t i = 2; i < 11; ++i) {
        cout << ' ' << factor[i];
      }
      cout << '\n';
      if (J == 0) {
        break;
      }
    }
  }
}

int main() {
  std::ios::sync_with_stdio(false);
  ull T; cin >> T;
  for (ull i = 1; i <= T; ++i) {
    ull N, J;
    cin >> N >> J;
    cout << "Case #" << i << ":\n";
    solve(N, J);
  }
}
