//Joe Snider
//4/13
//
//code for codejam round1_1 2013

#include <iostream>
#include <gmp.h>
#include <math.h>

using namespace std;

int main() {
   int T;
   double ar, at;
   mpf_t r;
   mpf_t t;
   mpf_init2(r, 1000);
   mpf_init2(t, 1000);
   cin >> T;
   
   for(int i = 0; i < T; ++i) {
      cin >> ar >> at;
      mpf_set_ui(r, (2.*ar-1.));
      mpf_set_ui(t, 8.*at);
      mpf_mul(r, r, r);
      mpf_add(r, r, t);
      mpf_sqrt(r, r);
      double res = (mpf_get_d(r) - (2.*ar-1.))/4.;
      cout << "Case #" << i+1 << ": " << int(res) << "\n";
   }
   
   return 0;
}


