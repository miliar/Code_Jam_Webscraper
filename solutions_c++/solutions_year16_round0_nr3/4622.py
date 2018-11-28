#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <bitset>
#include <cmath>

using uint64 = unsigned long long;

static uint64 getNonTrivialDivisor(uint64 N);
template <size_t T>
static uint64 jamcoin2int(const std::bitset<T>& bits, uint64 base);
//static void changeBase(uint64 N, int base, uint64& result);

int main() {
  
  const bool small_data_set = true;

  const int jamcoin_len = small_data_set ? 16: 32;
  const int jamcoin_len_internal = jamcoin_len - 3;
  const int jamcoins_count = small_data_set ? 50 : 500;

  printf("Case #1:\n");

  uint64 nonTrivialDivisors[9] = {0};

  uint64 jamcoin_value = (uint64(1) << (jamcoin_len - 1)) + 1;
  uint64 inner_jamcoin_value = 0;
  std::bitset<jamcoin_len - 2> bits(inner_jamcoin_value);

  for (int i = 0; i < jamcoins_count; ++i) {

    bool done = false;
    while (!done) {
      for (int j = 0, base = 2; j < 9; ++j, ++base) {
        uint64 jamcoin_base = jamcoin2int<jamcoin_len - 2>(bits, base);
        // printf("Testing: %lu\n", jamcoin_base);
        // printf("  Getting non trivial divisor\n");
        uint64 nonTrivialDivisor = getNonTrivialDivisor(jamcoin_base);
        if (nonTrivialDivisor != jamcoin_base) {
          nonTrivialDivisors[j] = nonTrivialDivisor; 
          if (base == 10) {
            done = true;
          }
        } else {
          // printf(" Changing\n");
          bits = std::bitset<jamcoin_len - 2>(inner_jamcoin_value += 1);
          break;
        }
      }
    }

    printf("1%s1 ", bits.to_string().c_str());
    for (int j = 0; j < 9; ++j) {
      printf("%lu ", nonTrivialDivisors[j]);
    } 
    printf("\n");
    bits = std::bitset<jamcoin_len - 2>(inner_jamcoin_value += 1);
  }
  
}

// Return -1 when N is prime
uint64 getNonTrivialDivisor(uint64 N) {
  if (N % 2 == 0) return 2;
  for (uint64 i = 3; i*i < N; i += 2) {
    if (N % i == 0) {
      return i;
    }
  }
  return N; 
}

template <size_t T>
uint64 jamcoin2int(const std::bitset<T>& bits, uint64 base) {
  uint64 multiplier = base;
  uint64 result = 1;
  for (size_t i = 0; i < bits.size(); ++i) {
    result += int(bits[i]) * multiplier;  
    multiplier *= base;
  }
  return result + multiplier;
}

/*
void changeBase(uint64 N, int base, uint64& result) {
  if (base == 10) {
    result = N;
    return;
  }

  static int multiplier;
  if (result == -1) { // first call
    result = 0;
    multiplier = 1;
  }
  if (N == 0) {
    return;
  }
  uint64 remainder = N%base;
  multiplier *= 10;
  changeBase(N/base, base, result);
  multiplier /= 10;
  // printf("%lu %d %d    ", N, remainder, multiplier);
  result += remainder * multiplier;
}
*/
