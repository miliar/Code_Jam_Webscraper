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
const int HI = 2010 ;
ull N, a[HI], b[HI], p[HI] ;
int recur(int at) {
  if (at == N)
    return 1 ;
  ull hileft = 1 ;
  for (int i=0; i<N; i++) {
    if (p[i] < N) {
      if (hileft < 1 + a[i])
	hileft = 1 + a[i] ;
    } else if (a[i] + b[i] - 2 <= at && a[i] == hileft) {
      p[i] = at ;
      ull hi = 1 ;
      for (ull j=i+1; j<N; j++)
	if (p[j] < N && hi < 1 + b[j])
	  hi = 1 + b[j] ;
      if (hi == b[i]) {
	// make sure no unset value to the right at hileft
	int okay = 1 ;
	for (ull j=i+1; j<N; j++)
	  if (p[j] > N && a[j] == a[i])
	    okay = 0 ;
	// make sure no unset value to the left at hi
	for (ull j=0; j<i; j++)
	  if (p[j] > N && b[j] == b[i])
	    okay = 0 ;
	if (okay)
	  if (recur(at+1))
	    return 1 ;
      }
      p[i] = 1000 * N ;
    }
  }
  return 0 ;
}
int main(int argc, char *argv[]) {
   int kases ;
   scanf("%d", &kases) ;
   for (int kase=1; kase<=kases; kase++) {
     scanf("%lld", &N) ;
     for (int i=0; i<N; i++) {
       ull v ;
       scanf("%lld", &v) ;
       a[i] = v ;
     }
     for (int i=0; i<N; i++) {
       ull v ;
       scanf("%lld", &v) ;
       b[i] = v ;
     }
     memset(p, 10, sizeof(p)) ;
     if (recur(0) == 0)
       cout << "Didn't get a solution" << endl ;
     cout << "Case #" << kase << ":" ;
     for (int i=0; i<N; i++)
       cout << " " << (1+p[i]) ;
     cout << endl ;
   }
}
