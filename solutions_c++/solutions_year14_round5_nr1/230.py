#include <iostream>
#include <map>
#include <vector>
#include <iomanip>
using namespace std ;
int main(int argc, char *argv[]) {
  int kases ;
  cin >> kases ;
  for (int kase=1; kase<=kases; kase++) {
    cout << "Case #" << kase << ": " ;
    long long N, p, q, r, s ;
    cin >> N ;
    cin >> p ;
    cin >> q ;
    cin >> r ;
    cin >> s ;
    vector<long long> a ;
    long long sum = 0 ;
    for (int i=0; i<N; i++) {
      sum += (i * p + q) % r + s ;
      a.push_back(sum) ;
    }
    a.push_back(sum) ;
    a.push_back(sum) ;
    long long siz = sum ;
    long long bsiz = 1LL ;
    while (bsiz <= siz) {
      bsiz += bsiz ;
    }
    vector<long long>::iterator at1, at2 ;
    long long best = sum ;
    for (; bsiz > 0; bsiz >>= 1) {
      long long tsiz = siz - bsiz ;
      if (tsiz < 0)
	continue ;
      long long hi1 = sum ;
      at1 = lower_bound(a.begin(), a.end(), tsiz) ;
      while (at1 > a.begin() && (at1 == a.end() || *at1 > tsiz))
	at1-- ;
      if (at1 != a.end()) {
	at2 = lower_bound(at1, a.end(), *at1+tsiz) ;
	while (at2 > at1 && (at2 == a.end() || *at2 > *at1+tsiz))
	  at2-- ;
	hi1 = *at1 ;
	if (at2 != a.end()) {
	  if (*at2 - *at1 > hi1)
	    hi1 = *at2 - *at1 ;
	  if (sum - *at2 > hi1)
	    hi1 = sum - *at2 ;
	}
      }
      if (hi1 < best) {
	best = hi1 ;
	siz = hi1 ;
      }
    }
    cout << setprecision(15) ;
    cout << ((sum - best) / (double)sum) << endl ;
  }
}
