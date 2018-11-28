#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std ;
typedef long long ull ;
const ull INF = 1000000000000000LL ;
double val[1<<20] ;
int main(int argc, char *argv[]) {
   int kases ;
   scanf("%d\n", &kases) ;
   for (int kase=1; kase<=kases; kase++) {
     ull N = 0 ;
     int bits = 0 ;
     int i = 0 ;
     while (1) {
       char c ;
       scanf("%c", &c) ;
       if (c == '.' || c == 'X') {
	 if (c == 'X')
	   bits |= 1<<N ;
	 N++ ;
       } else if (N > 0)
	 break ;
     }
     val[(1<<N)-1] = 0 ;
     for (int m=((1<<N)-2); m>=0; m--) {
       int q = 0 ;
       for (int j=0; j<N; j++)
	 if ((m >> j) & 1)
	   q++ ;
         else
           q = 0 ;
       double s = 0 ;
       double n = 0 ;
       for (int j=0; j<N; j++)
	 if ((m >> j) & 1)
	   q++ ;
         else {
	   s += (N * (q + 1) - q * (q + 1) / 2) + (q + 1) * val[m | (1 << j)] ;
	   q = 0 ;
	 }
       val[m] = s / N ;
     }
     cout.precision(15) ;
     cout << "Case #" << kase << ": " << val[bits] << endl ;
   }
}
