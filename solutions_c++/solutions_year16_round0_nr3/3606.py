#include <iostream>
#include <cstdio>
#include <map>
#include <gmpxx.h>
#include <bitset>

using namespace std;

mpz_class interpretation(unsigned int coin, int base) {
   mpz_class x = 0;
   mpz_class f = 1;
   while (coin > 0) {
      x += f * (coin % 2);
      coin /= 2;
      f *= base;
   }
   return x;
}

int main() {
   int T, N, J;
   cin >> T >> N >> J;
   unsigned int coin = 1 << (N - 1) | 1;
   unsigned int max = 0xFFFFFFFF >> (32 - N);
   mpz_class ivals[11];
   cout << "Case #1:" << endl;
   while (coin < max && J > 0) {
      int p = 0;
      for (int i = 2; i <= 10 && p == 0; ++i) {
         ivals[i] = interpretation(coin, i);
         p = mpz_probab_prime_p(ivals[i].get_mpz_t(), 1);
         //cout << ivals[i] << "(" << i << ") = " << p << endl;
      }
      if (p == 0) {
         string bits = "";
         unsigned int x = coin;
         while (x > 0) {
            bits = (x % 2 == 1 ? '1' : '0') + bits;
            x /= 2;
         }
         cout << bits;
         //cout << bits << "=" << coin;
         for (int i = 2; i <= 10; ++i) {
            mpz_t p, m;
            mpz_init(p);
            mpz_init(m);
            mpz_class f = 1;
            while(1) {
               mpz_nextprime(p, f.get_mpz_t());
               f = mpz_class(p);
               //cout << "   (" << ivals[i] << "," << p << "):" << mpz_divisible_p(ivals[i].get_mpz_t(), p) << endl;
               if (mpz_divisible_p(ivals[i].get_mpz_t(), p) != 0) break;
            }
            cout << " " << f;
            //cout << " " << ivals[i] << ":" << p;
         }
         cout << endl;
         --J;
      }
      coin += 2;
   }
   return 0;
}

