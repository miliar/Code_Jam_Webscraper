#include <cstdio>
#include <vector>

using namespace std;

inline long long fctr(long long x) {
   if (x == 2) {return -1;}
   if ((x & 1) == 0) {return 2;}
   for(long long i = 3 ; i * i <= x ; i++) {
      if ((x % i) == 0) {return i;}
   }
   return -1;
}

int num = 0;

inline void func(int mask) {
   if (num == 50) {return;}
   bool good = true;
   vector<long long> vec;
   for(int b = 2 ; b <= 10 ; b++) {
      long long tot = 0;
      for(int j = 15 ; j >= 0 ; j--) {
         tot = tot * b + ((mask >> j) & 1);
      }
      long long ret = fctr(tot);
      if (ret == -1) {
         good = false;
         break;
      }
      else {
         vec.push_back(ret);
      }
   }
   if (good) {
      for(int j = 15 ; j >= 0 ; j--) {
         printf("%d", ((mask >> j) & 1));
      }
      for(int j = 0 ; j < (int)vec.size() ; j++) {
         printf(" %lld", vec[j]);
      }
      printf("\n");
      num++;
   }
}

int main() {
   for(int mask = (1 << 15) + 1 ; mask < (1 << 16) ; mask += 2) {
      func(mask);
   }
   return 0;
}
