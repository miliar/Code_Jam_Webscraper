#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;
const int N = 16;
int J = 500;

const int PTMAX = 50000000;
int prime_table[PTMAX];
vector<int> primes;

int cand[N];
int keys[11];

void make_prime_table()
{
  for (int i = 2; i < PTMAX; ++i)
    prime_table[i] = 1;

  for (int p = 2; p < PTMAX; ++p)
    if (prime_table[p])
      for (int q = p * 2; q < PTMAX; q += p)
        prime_table[q] = 0;

  primes.reserve(count(prime_table, prime_table + PTMAX, 1));
  for (int p = 2; p < PTMAX; ++p)
    if (prime_table[p])
      primes.push_back(p);
}

int main()
{
  make_prime_table();

  cout << "Case #1:" << endl;

  for (LL x = (1 << (N - 1)) + 1; x < (1 << N); x += 2) {
    LL y = x;
    for (int i = 0; i < N; ++i, y /= 2)
      cand[i] = y % 2;

    // for (int i = 0; i < N; ++i)
    //   cout << cand[N - i - 1];
    // cout << endl;

    for (int i = 0; i <= 10; ++i)
      keys[i] = 0;
    for (int i = 2; i <= 10; ++i) {
      LL z = 0, base = 1;
      for (int j = 0; j < N; ++j, base *= i)
        z += cand[j] * base;
      for (int j = 0; j < primes.size(); ++j) {
        int p = primes[j];
        if (p * p > z)
          break;
        if (!(z % p)) {
          keys[i] = primes[j];
          break;
        }
      }
    }

    if (count(keys + 2, keys + 11, 0))
      continue;

    for (int i = 0; i < N; ++i)
      cout << cand[N - i - 1];
    for (int i = 0; i < N; ++i)
      cout << cand[N - i - 1];
    for (int i = 2; i <= 10; ++i)
      cout << " " << keys[i];
    cout << endl;

    if (!(--J))
      break;
  }

  return 0;
}
