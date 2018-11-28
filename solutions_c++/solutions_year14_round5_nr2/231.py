#include <iostream>
#include <map>
#include <vector>
#include <iomanip>
using namespace std ;
int debug = 0 ;
long long v1[10000], v2[10000] ;
int main(int argc, char *argv[]) {
  int kases ;
  cin >> kases ;
  for (int kase=1; kase<=kases; kase++) {
    cout << "Case #" << kase << ": " ;
    int P, Q, N ;
    cin >> P ;
    cin >> Q ;
    cin >> N ;
    vector<int> h, g ;
    for (int i=0; i<N; i++) {
      int t ;
      cin >> t ;
      h.push_back(t) ;
      cin >> t ;
      g.push_back(t) ;
    }
    int ms = 1 ;
    v1[0] = 0 ;
    v1[1] = 0 ;
    const int MIN = -10000000 ;
    long long *thisv = v1 ;
    long long *nextv = v2 ;
    for (int i=0; i<N; i++) {
      int hi = 1 + h[i] / P ;
      int maxhitaccum = MIN ;
      int maxmissaccum = MIN ;
      for (int ds=0; ds<=hi && (maxhitaccum == MIN || maxmissaccum == MIN); ds++) {
	// diana shoots this monster ds times
	// tower shoots how many?
	int left = h[i] - ds * P ;
	int ts = 0 ;
	if (left > 0) {
	  ts = 1 + (left - 1) / Q ;
	}
	// if hit, let tower shoot more.
	while (ds > 0 && (ts + 1) * Q + (ds - 1) * P < h[i])
	  ts++ ;
	// does diana manage to get this monster with the last shot?
	if (ds > 0 && ts * Q + (ds - 1) * P < h[i]) {
	  // diana gets the monster; how expensive?
	  // might be positive, might be negative
	  if (ts - ds > maxhitaccum) {
	    if (debug)
	    cout << "Valid hit ds " << ds << " ts " << ts << endl ;
	    maxhitaccum = ts - ds ;
	  }
	} else {
	  // tower gets the monster; save max
	  if (ts - ds > maxmissaccum)
	    maxmissaccum = ts - ds ;
	}
      }
      if (debug)
      cout << "At " << i << " ms " << ms << " maxhit " << maxhitaccum << " maxmiss " << maxmissaccum << endl ;
      int nms = ms + maxmissaccum ;
      for (int j=0; j<=nms; j++) {
	long long gv = 0 ;
	if (j >= maxmissaccum)
	  gv = thisv[j-maxmissaccum] ;
	else
	  gv = 0 ;
	if (j >= maxhitaccum && j-maxhitaccum <= ms) {
	  long long gv2 = g[i] + thisv[j-maxhitaccum] ;
	  if (gv2 > gv)
	    gv = gv2 ;
	}
	if (debug)
	cout << "Gold val for " << i << " " << j << " is " << gv << endl ;
	nextv[j] = gv ;
      }
      swap(thisv, nextv) ;
      ms = nms ;
    }
    long long r = 0 ;
    for (int i=0; i<=ms; i++)
      if (thisv[i] > r)
	r = thisv[i] ;
    cout << r << endl ;
  }
}
