#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;


inline
float getK(vector<float>& K, const float n, bool peek = false) {
   float ret = 0;
   auto iter = upper_bound(K.begin(), K.end(), n);

   if (iter == K.end()) {
      iter = K.begin();
   }
   ret = *iter;
   if (!peek) {
      K.erase(iter);
   }

   return ret;
}


inline
float getDWn(vector<float>& K, const float n) {
   float ret = n;
   const float peekK = getK(K, n, true);
   unsigned sizeK = K.size();
   if (n < peekK && sizeK > 1) {
      if (peekK == K[0]) {
         ret = (K[sizeK - 1] + K[sizeK - 2]) / 2;
      } else {
         ret = K[sizeK - 1] + 1e-7;
      }
   }

   return ret;
}


inline
unsigned DW(vector<float> N, vector<float> K) {
   unsigned ret = 0;

   for (unsigned i = 0; i < N.size(); ++i) {
      const float n = getDWn(K, N[i]);
      const float k = getK(K, n);
//cout << "Debug: N[" << i << "] = " << N[i] << ", n = " << n << ", k = " << k << endl;
      if (n > k) {
         ++ret;
      }
   }

   return ret;
}


inline
unsigned W(vector<float> N, vector<float> K) {
   unsigned ret = 0;

   for (unsigned i = 0; i < N.size(); ++i) {
      const float n = N[i];
      const float k = getK(K, n);
      if (n > k) {
         ++ret;
      }
   }

   return ret;
}

int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      unsigned resultDW = 0;
      unsigned resultW = 0;
      unsigned N;

      cin >> N;

      vector<float> Naomi(N);
      vector<float> Ken(N);

      for (unsigned i = 0; i < N; ++i) {
         cin >> Naomi[i];
      }
      for (unsigned i = 0; i < N; ++i) {
         cin >> Ken[i];
      }
      sort(Naomi.begin(), Naomi.end());
      sort(Ken.begin(), Ken.end());

      resultDW = DW(Naomi, Ken);
      resultW = W(Naomi, Ken);

      cout << "Case #" << t + 1 << ": " << resultDW << ' ' << resultW << endl;
   }

   return 0;
}

