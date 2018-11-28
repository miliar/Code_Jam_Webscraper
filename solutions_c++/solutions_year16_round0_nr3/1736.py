#include <iostream>

#include <vector>
#include <algorithm>

//#include <random>

using namespace std;

typedef long long llong;

string bit_to_string(long long m, int nbits = 32) {
   string res;
   for (int i = 0; i < nbits; ++i)
      res += (m & (1LL << i)) ? '1' : '0';
   reverse(res.begin(), res.end());
   return res;
}

int N, J;

vector<int> primes = {
      2,      3,      5,      7,     11,     13,     17,     19,     23,     29, 
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71, 
     73,     79,     83,     89,     97,    101,    103,    107,    109,    113
//    127,    131,    137,    139,    149,    151,    157,    163,    167,    173 
};

int get_prime_divisor(llong x, int nbits, int base) {
   for (int p : primes) {
      if (x == p) continue;
      int num = 0;
      for (int j = nbits-1; j >= 0; --j) {
         num *= base;
         if (x & (1LL<<j))
            num++;
         num %= p;
      }
      if (num == 0)
         return p;
   }
   return -1;
}

vector<int> get_prime_divisors(llong x, int nbits) {
   vector<int> res;
   res.reserve(9);
   for (int b = 2; b <= 10; ++b) {
      int p = get_prime_divisor(x, nbits, b);
      if (p < 0)
         return vector<int>();
      res.push_back(p);
   }
   return res;
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   mt19937 mt(123);   // use a seed

   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      cin >> N >> J;
      uniform_int_distribution<int> dist(0, (1<<(N-2))-1);
      cout << "Case #" << tc << ":" << endl;
      for (int j = 0; j < J; ++j) {
         while (true) {
            llong m = dist(mt);
            llong x = (1LL << (N-1)) | (m << 1) | 1;
            vector<int> P = get_prime_divisors(x, N);
            if (!P.empty()) {
               cout << bit_to_string(x, N);
               for (int p : P)
                  cout << ' ' << p;
               cout << '\n';
               break;
            }
         }
      }
   }

   return 0;
}
