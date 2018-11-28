#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
using namespace std ;
typedef long long ull ;
ull md = 1000002013LL ;
map<ull, ull> in, out ;
ull m3(ull a, ull b) {
  return (a * (b % md)) % md ;
}
int main(int argc, char *argv[]) {
   int kases ;
   scanf("%d", &kases) ;
   for (int kase=1; kase<=kases; kase++) {
      ull N, M ;
      scanf("%lld %lld", &N, &M) ;
      ull s = 0 ;
      in.clear() ;
      out.clear() ;
      for (int i=0; i<M; i++) {
	ull o, e, p ;
	scanf("%lld %lld %lld", &o, &e, &p) ;
	in[-o] += p ;
	out[e] += p ;
	s += m3(p, ((e - o) * (2*N-(e-o)+1) / 2)) ;
	s = s % md ;
      }
      ull s2 = 0 ;
      map<ull, ull>::iterator to = out.begin() ;
      while (to != out.end()) {
	ull need = to->second ;
	ull end = to->first ;
	map<ull, ull>::iterator from = in.begin() ;
	while (to->first + from->first < 0)
	  from++ ;
	while (1) {
	  ull start = - from->first ;
	  ull excess = from->second ;
	  ull calc = min(excess, need) ;
	  need -= calc ;
	  from->second -= calc ;
	  s2 += m3(calc, ((end - start) * (2*N-(end - start)+1) / 2)) ;
	  s2 = s2 % md ;
	  if (need == 0)
	    break ;
	  from++ ;
	  start = from->first ;
	  excess = from->second ;
	}
	to++ ;
      }
      ull r = (s + md - s2) % md ;
      printf("Case #%d: %lld\n", kase, r) ;
   }
}
