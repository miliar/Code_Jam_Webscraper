#include <cstdlib>
#include <iostream>
#include <bitset>
#include <cmath>
using namespace std;

bool isPal(long l) {
   long l2 = 0;
   long l3 = l;
   while (l3 > 0) {
      l2 = l2 * 10 + (l3 % 10);
      l3 /= 10;
   }
   return (l2 == l);
}

int main(void) {
   /*for (long i = 1 ; i <= 10000000 ; i ++ ) {
   for (long i = 1 ; i <= 200 ; i ++ ) {
       if (isPal(i)) {  cout << i << endl; }
   }*/
   long a, b, t;
   cin >> t;
   long* arr = new long[10000010];
   long count1 = 0 ;
   for (long j = 1 ; j < 10000010; j++) {
         if (isPal(j) && isPal(j*j)) {
             count1 += 1;
             arr[j] = count1;
         } else 
         { arr[j] = count1; }
   }
//   cout << "OK" << endl;
   for (int j = 1 ; j <= t; j++) {
       cin >> a >> b;
       long l = sqrt(a);
       long l2 = sqrt(b);
       long result = arr[l2] - arr[l] ;
       if ((l*l == a) && isPal(l) && isPal(a)) { result += 1; }
       if (l * l < a) { l += 1; }
       /*long i = l * l;
       long count = 0;
       while (i <= b) {
            if (isPal(l) && isPal(i)) { count += 1; }
            l += 1;
            i = l * l;
       }*/
       cout << "Case #" << j << ": " << result << endl; 
   }
   delete[] arr;
   return 0;
}
