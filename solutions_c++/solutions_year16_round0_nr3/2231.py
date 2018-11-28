#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;


static const unsigned T = 1;
static const unsigned N = 16;
static const unsigned J = 500;
unsigned long long q[9];

struct number {
   number();
   void reset();
   void gen();
   unsigned digits[N];
   unsigned long long coef[9][N];
   unsigned long long seed;
   unsigned long long baseN(unsigned n);
};

void number::reset() {
   for (unsigned i = 0; i < N; ++i) {
      if (i == 0 || i == N-1) {
         digits[i] = 1;
      } else {
         digits[i] = 0;
      }
   }
}

number::number() {
   for (unsigned b = 2; b < 11; ++b) {
      for (unsigned d = 0; d < N; ++d) {
         if (d == 0) {
            coef[b-2][d] = 1;
         } else {
            coef[b-2][d] = b * coef[b-2][d-1];
         }
      }
   }

   reset();
   seed = 0;
}

void number::gen() {
   if (seed >= (1 << 14)) {
      cerr << "Critical error!!";
      exit(-1);
   }
   reset();
   unsigned long long s = seed;
   unsigned b = 1;
   while (s > 0) {
      digits[b] = s & 0x1;
      ++b;
      s >>= 1;
   }
   ++seed;
//cout << "new n is " << baseN(10) << endl;
}

unsigned long long number::baseN(unsigned n) {
   if (n < 2 || n > 10) {
      return 0;
   }

   unsigned long long result = 0;
   for (unsigned d = 0; d < N; ++d) {
      result += coef[n-2][d] * digits[d];
   }

   return result;
}


number num;


bool isPrime(unsigned long long n, unsigned b)
{
//cout << ", n = " << n << endl;
   if (n < 2) {
      q[b-2] = 0;
      return false;
   }
   if (n < 4) {
      return true;
   }
   if ((n & 0x1) == 0) {
      q[b-2] = 2;
      return false;
   }
   if ((n % 3) == 0) {
      q[b-2] = 3;
      return false;
   }

   unsigned long long s = 5;
   while (s*s < n) {
      if ((n % s) == 0) {
         q[b-2] = s;
         return false;
      }
      if ((n % (s + 2)) == 0) {
         q[b-2] = s + 2;
         return false;
      }
      s +=6;
   }

//cout << n << " is a prime!!" << endl << endl;
   return true;
}


bool isJamCoin()
{
   for (unsigned b = 2; b < 11; ++b) {
//cout << "b = " << b;
      if (isPrime(num.baseN(b), b)) {
         return false;
      }
   }

   return true;
}


int main(int, char**) {
   cout << "Case #" << T << ":" << endl;

   unsigned j = 0;
   while (j < J) {
      num.gen();
//cout << "j = " << j << endl;
      if (isJamCoin()) {
         cout << num.baseN(10);
         cout << num.baseN(10);
         for (unsigned b = 2; b < 11; b++) {
            cout << " " << q[b-2];
         }
         cout << endl;
         ++j;
      }
   }

   return 0;
}

