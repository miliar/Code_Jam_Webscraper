#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

#define BASE_START 2
#define BASE_END 10


unsigned long long convert_to_base(unsigned long long n, int base)
{
  return stoull(to_string(n), nullptr, base);
}

bool is_prime(unsigned long long n, unsigned long long *divisor)
{
  if (n < 2) {
    *divisor = 1;
    return false;
  } else if (n % 2 == 0) {
    *divisor = 2;
    return false;
  }

  unsigned long long upper_limit = (unsigned long long)floor(sqrt(n));
  for (unsigned long long i = 3; i <= upper_limit; i += 2) {
    if (n % i == 0) {
      *divisor = i;
      return false;
    }
  }

  return true;
}

bool is_jam_coin(unsigned long long n, vector<unsigned long long> &divisors)
{
  divisors.clear();
  for (int b = BASE_START; b <= BASE_END; ++b) {
    unsigned long long divisor = 0;
    unsigned long long n_in_base = convert_to_base(n, b);
    if (is_prime(n_in_base, &divisor)) {
      return false;
    } else {
      divisors.push_back(divisor);
    }
  }

  return true;
}

void process_case()
{
  int N, J;
  cin >> N >> J;

  unsigned long long start = (unsigned long long)pow(2, N - 1) + 1;
  unsigned long long end = (unsigned long long)pow(2, N) - 1;

  vector<unsigned long long> divisors;
  int count = 0;
  for (unsigned long long n_in_base_2 = start; n_in_base_2 <= end; n_in_base_2 += 2) {
    auto n_in_base_2_str = bitset<64>(n_in_base_2).to_string();
    unsigned long long n = stoull(n_in_base_2_str, nullptr, 10);
    if (is_jam_coin(n, divisors)) {
      cout << n;

      for (int b = BASE_START; b <= BASE_END; ++b) {
        int i = b - BASE_START;
        cout << " " << divisors[i];
      }

      cout << endl;

      ++count;
      if (count == J) {
        return;
      }
    }
  }
}

int main()
{
  int t;
  cin >> t;

  for (int i = 0; i < t; ++i) {
    process_case();
  }

  return 0;
}