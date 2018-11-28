#include <cmath>
#include <cstdio>
#include <bitset>

#ifdef __LARGE__
  #include <boost/multiprecision/cpp_int.hpp>
  #include <boost/multiprecision/integer.hpp>

  constexpr size_t N = 32, J = 500;
  std::bitset<N> bitnum (std::string("10000000000000000000000000000001"));

  using namespace boost::multiprecision;
  using big_int = uint128_t;
#else
  constexpr size_t N = 16, J = 50;
  std::bitset<N> bitnum (std::string("1000000000000001"));

  using big_int = unsigned long long;
#endif

bool next_n() {
  size_t i;
  for(i = 1; i < (N - 1) && bitnum[i]; ++i) {
    bitnum.reset(i);
  }
  if(i == (N - 1)) return false;

  bitnum.set(i);
  return true;
}

big_int power[11][N];

big_int in(char base) {
  big_int r = 1 + power[base][N-1];
  for(unsigned i = 1; i < (N - 1); ++i)
    if(bitnum[i]) r += power[base][i];
  return r;
}

unsigned long long prime(big_int i) {
  #ifdef __LARGE__
    unsigned long long s = 10^7;
  #else
    unsigned long long s = sqrtl(i);
  #endif

  for(unsigned long long j = 3; j <= s; j += 2)
    if(!(i % j)) return j;
  return 0;
}

int main() {
  for(char base = 2; base < 11; ++base)
    power[base][0] = 1;
  for(unsigned i = 1; i < N; ++i)
    for(char base = 2; base < 11; ++base)
      power[base][i] = power[base][i-1] * base;

  printf("Case #1:\n");
  unsigned j = 0;
  do {
    bool skip = false;
    unsigned long long divisor[11];

    for(char base = 2; base < 11; ++base) {
      if(!(divisor[base] = prime(in(base)))) {
        skip = true;
        break;
      }
    }
    if(skip) continue;

    ++j;
    printf("%s", bitnum.to_string().c_str());
    for(char base = 2; base < 11; ++base)
      printf(" %llu", divisor[base]);
    putchar('\n');
  } while(next_n() && j < J);
}
