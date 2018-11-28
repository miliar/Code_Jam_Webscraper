#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
using namespace std ;
typedef long long ull ;
ull recurlow(ull P, ull N) {
  if (P == (1LL<<N))
    return P-1 ;
  if (P == 0)
    return -1LL ;
  ull b = 2 ;
  ull r = 0 ;
  while (P > (1LL << (N-1))) {
    r |= b ;
    b <<= 1 ;
    P -= (1LL << (N - 1)) ;
    N-- ;
  }
  return r ;
}
int main(int argc, char *argv[]) {
   int kases ;
   scanf("%d", &kases) ;
   for (int kase=1; kase<=kases; kase++) {
      ull N, P ;
      scanf("%lld %lld", &N, &P) ;
      ull r = recurlow(P, N) ;
      ull r2 = (1LL<<N) - 2 - recurlow((1LL<<N)-P, N) ;
      printf("Case #%d: %lld %lld\n", kase, r, r2) ;
   }
}
