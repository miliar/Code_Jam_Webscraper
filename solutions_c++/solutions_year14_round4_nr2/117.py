#include <iostream>
#include <map>
#include <vector>
using namespace std ;
int main(int argc, char *argv[]) {
  int kases ;
  cin >> kases ;
  for (int kase=1; kase<=kases; kase++) {
    cout << "Case #" << kase << ": " ;
    int N ;
    cin >> N ;
    vector<int> a ;
    for (int i=0; i<N; i++) {
      int v ;
      cin >> v ;
      a.push_back(v) ;
    }
    int lo = 0 ;
    int hi = a.size() ;
    int r = 0 ;
    while (hi - lo > 1) {
      int loi = lo ;
      for (int i=lo+1; i<hi; i++)
	if (a[i] < a[loi])
	  loi = i ;
      if (loi - lo < hi - 1 - loi) {
	while (loi > lo) {
	  swap(a[loi], a[loi-1]) ;
	  loi-- ;
	  r++ ;
	}
	lo++ ;
      } else {
	while (loi+1 < hi) {
	  swap(a[loi], a[loi+1]) ;
	  loi++ ;
	  r++ ;
	}
	hi-- ;
      }
    }
    cout << r << endl ;
  }
}
