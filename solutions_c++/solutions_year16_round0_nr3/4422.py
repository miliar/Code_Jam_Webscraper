#include <gmpxx.h>
#include <iostream>

using namespace std;

const int PRIME_REPS = 40;

mpz_class get_nt_divisor(mpz_class n) {
   mpz_class bound = sqrt(n);
   for (mpz_class i = 2; i <= bound; i++) {
      if (n % i == 0) {
         return i;
      }
   }
   return mpz_class(-1);
}

int main(void) {
   int tests, bits, needed, total = 0;
   mpz_class *bases = new mpz_class[9];

   cin >> tests;
   cin >> bits;
   cin >> needed;

   mpz_class bound = mpz_class(1) << bits;

   cout << "Case #1:" << endl;
   
   // Loop through all coins from 2^15 + 1 to 2^16 - 1
   for (bases[0] = (mpz_class(1) << (bits - 1)) + 1;
        bases[0] < bound; bases[0] += 2) {
      string bits = bases[0].get_str(2);
      
      // If not prime in base 2, check all other bases
      if (mpz_probab_prime_p(bases[0].get_mpz_t(), PRIME_REPS) == 0) {
         bool found = true;
         for (int i = 3; i <= 10; i++) {
            mpz_set_str(bases[i-2].get_mpz_t(), bits.c_str(), i);
            if (mpz_probab_prime_p(bases[i-2].get_mpz_t(), PRIME_REPS) != 0) {
               found = false;
               break;
            }
         }

         if (found == true) {
            // Get the factors and make sure they're definitely prime (probably not needed)
            mpz_class *divisors = new mpz_class[9];
            for (int i = 0; i < 9; i++) {
               divisors[i] = get_nt_divisor(bases[i]);
               if (divisors[i] < 0) {
                  continue;
               }
            }

            // Print the factors
            cout << bits;
            for (int i = 0; i < 9; i++) {
               cout << " " << divisors[i];
            }
            cout << endl;
            
            if (++total == needed) {
               break;
            }
         }
      }
   }

   delete[] bases;
}
