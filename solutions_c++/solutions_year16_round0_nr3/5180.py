#include <algorithm>
#include <array>
#include <bitset>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <limits>
#include <vector>

static const int INF = std::numeric_limits<int>::max() >> 1;

using ll = long long;

// constexpr ll MAX_L = 100000000000;
// constexpr ll MAX_SQRT_B = 1000000;

constexpr ll MAX_L = 1000000000;
constexpr ll MAX_SQRT_B = 100000;

bool is_prime[MAX_L];
bool is_prime_small[MAX_SQRT_B];

void init() {
  std::fill(is_prime, is_prime + MAX_L, false);
  std::fill(is_prime_small, is_prime_small + MAX_SQRT_B, false);
}

void segment_sieve(ll a, ll b) {
  for (int i = 0; (ll) i * i < b; i++) { is_prime_small[i] = true; }
  for (int i = 0; i < b - a; i++) { is_prime[i] = true; }

  for (int i = 2; (ll) i * i < b; i++) {
    if (is_prime_small[i]) {
      for (int j = 2 * i; (ll) j * j < b; j += i) { is_prime_small[j] = false; }
      for (ll j = std::max(2LL, (a + i - 1) / i) * i; j < b; j += i) {
        is_prime[j - a] = false;
      }
    }
  }
}

static const std::map<int, bool> done;

std::string intToCoin(int n, int N) {
  char buff[N];
  char *p = buff + N;
  do {
    *--p = '0' + (n & 1);
  } while (n >>= 1);
  return std::string(p, buff + N);
}

ll coinToLong(const std::string& coin, int base) {
  ll b = 1;
  ll n = 0;

  for (int i = coin.size() - 1; i >= 0; --i) {
    n += (coin[i] - '0') * b;
    b *= base;
  }
  return n;
}

ll findDivisor(ll m) {
  ll r = -1;
  for (int d = 2; d <= std::sqrt(m) + 1; d++) {
    if (m % d == 0) {
      r = d;
      break;
    }
  }
  return r;
}

bool isPrime(ll n) {
  ll x = findDivisor(n);
  return x == -1;
}

bool coinjam(int coin, std::string& result, int N) {
  std::string coinStr = intToCoin(coin, N);
  std::string buf;
  buf += coinStr;
  for (int i = 2; i <= 10; ++i) {
    ll m = coinToLong(coinStr, i);
    // std::cout << "validating m: " << m << std::endl;
    // if (!is_prime[m]) {
    if (!isPrime(m)) {
      // std::cout << "m is not prime " << m << std::endl;
      buf += " " + std::to_string(findDivisor(m));
    } else {
      // std::cout << "m is prime, escaping...  " << m << std::endl;
      return false;
    }
  }
  buf += "\n";
  result += buf;
  return true;
}

int main(int argc, char *argv[])
{
  int n;
  std::scanf("%d\n", &n);
  // std::cout << "Initializing..." << std::endl;
  // init();
  // std::cout << "Done" << std::endl;
  std::set<int> done;

  int N, J;
  std::string result;
  int j = 0;
  for (int i = 1; i <= n; ++i) {
    std::scanf("%d %d\n", &N, &J);
    // std::cout << "N, J = " << N << ", " << J << std::endl;
    result += "Case #" + std::to_string(i) + ": \n";
    int base = (1 << (N - 1)) + 1;
    int max = (1 << N) -  1;
    // std::cout << "Initializing..." << std::endl;
    // segment_sieve(base, max);
    // segment_sieve(0, max);
    // std::cout << "Done..." << std::endl;
    for (int i = 0; i <= (max >> 1); ++i) {
      int x = (i << 1) | base;
      if (done.find(x) == done.end()) {
        bool is_valid = coinjam(x, result, N);
        if (is_valid) {
          // std::cout << x << " can be coinjam" << std::endl;
          done.insert(x);
          j += 1;
          if (j >= J) {
            break;
          }
        }
      }
    }
    // result += std::to_string(flip(v, 0));
  }

  std::cout << result;
  
  return 0;
}
