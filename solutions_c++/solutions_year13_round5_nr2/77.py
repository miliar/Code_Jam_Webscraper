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
ull N ;
ull side(ull x1, ull y1, ull x2, ull y2, ull x, ull y) {
  ull t = (x2-x1)*(y-y1)-(y2-y1)*(x-x1) ;
  if (t < 0) {
    return -1 ;
  }
  if (t > 0) {
    return 1 ;
  }
  return t ;
}
ull dot(ull x1, ull y1, ull x2, ull y2, ull x3, ull y3) {
  x2 -= x1 ;
  y2 -= y1 ;
  x3 -= x1 ;
  y3 -= y1 ;
  return x2 * x3 + y2 * y3 ;
}
int intsct(ull x1, ull y1, ull x2, ull y2, ull x3, ull y3, ull x4, ull y4) {
  ull t1 = side(x1, y1, x2, y2, x3, y3) ;
  ull t2 = side(x1, y1, x2, y2, x4, y4) ;
  ull t3 = side(x3, y3, x4, y4, x1, y1) ;
  ull t4 = side(x3, y3, x4, y4, x2, y2) ;
  if (t1 * t2 < 0 && t3 * t4 < 0)
    return 1 ;
  if (t1 * t2 > 0 || t3 * t4 > 0)
    return 0 ;
  ull d0 = dot(x1, y1, x2, y2, x2, y2) ;
  ull d1 = dot(x1, y1, x2, y2, x3, y3) ;
  ull d2 = dot(x1, y1, x2, y2, x4, y4) ;
  if ((d1 > d0 && d2 > d0) || (d1 < 0 && d2 < 0))
    return 0 ;
  return 1 ;
}
typedef pair<ull, ull> pt ;
int cross(pt a, pt b, pt c, pt d) {
  return intsct(a.first, a.second, b.first, b.second,
		c.first, c.second, d.first, d.second) ;
}
int main(int argc, char *argv[]) {
   int kases ;
   scanf("%d", &kases) ;
   for (int kase=1; kase<=kases; kase++) {
     scanf("%lld", &N) ;
     vector<pair<ull, ull> > a ;
     vector<int> perm ;
     for (int i=0; i<N; i++) {
       ull x,y ;
       scanf("%lld %lld", &x, &y) ;
       a.push_back(make_pair(x, y)) ;
       perm.push_back(i) ;
     }
     vector<int> best ;
     ull bestval = 0 ;
     do {
       if (perm[0] != 0)
	 break ;
       int bad = 0 ;
       for (int i=0; bad == 0 && i+1<N; i++)
	 for (int j=i+2; bad==0 && j<N; j++) {
	   if (i == 0 && j == N-1)
	     continue ;
	   if (cross(a[perm[i]], a[perm[i+1]],
		     a[perm[j]], a[perm[(j+1)%N]])) {
	     bad++ ;
	     break ;
	   }
	 }
       if (bad)
	 continue ;
       ull x = a[perm[N-1]].first ;
       ull y = a[perm[N-1]].second ;
       ull v = 0 ;
       for (int i=0; i<a.size(); i++) {
	 v += (y + a[perm[i]].second) * (x - a[perm[i]].first) ;
	 x = a[perm[i]].first ;
	 y = a[perm[i]].second ;
       }
       if (v < 0)
	 v = - v ;
       //       cout << "Area " << v << endl ;
       if (v > bestval) {
	 bestval = v ;
	 best = perm ;
       }
     } while (next_permutation(perm.begin(), perm.end())) ;
     if (bestval == 0)
       cerr << "Failed to find a non-crosser" << endl ;
     cout << "Case #" << kase << ":" ;
     for (int i=0; i<N; i++)
       cout << " " << best[i] ;
     cout << endl ;
   }
}
