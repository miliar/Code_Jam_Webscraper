#include <iostream>
#include <map>
#include <vector>
const int debug = 0 ;
using namespace std ;
struct trie {
  trie(int _parent, int _index) : parent(_parent), index(_index),
				  children(0), strings(0) {}
  int index ;
  int children ;
  int strings ;
  int parent ;
  vector<int> childcounts ;
} ;
long long comb[120][120] ;
const long long MOD = 1000000007 ;
long long add(long long a, long long b) {
  return (a + b) % MOD ;
}
long long mult(long long a, long long b) {
  return (a * b) % MOD ;
}
int main(int argc, char *argv[]) {
  comb[0][0] = 1 ;
  for (int i=1; i<120; i++) {
    comb[i][0] = 1 ;
    for (int j=1; j<=i; j++)
      comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD ;
  }
  int kases ;
  cin >> kases ;
  for (int kase=1; kase<=kases; kase++) {
    cout << "Case #" << kase << ": " ;
    int N, M ;
    cin >> M ;
    cin >> N ;
    string s ;
    map<pair<int, char>, int> h ;
    vector<trie> v ;
    v.push_back(trie(-1, 0)) ;
    int alloc = 1 ;
    for (int i=0; i<M; i++) {
      cin >> s ;
      int at = 0 ;
      for (int j=0; j<s.size(); j++) {
	v[at].strings++ ;
	pair<int, char> ind = make_pair(at, s[j]) ;
	if (h.find(ind) == h.end()) {
	  v[at].children++ ;
	  v.push_back(trie(at, alloc)) ;
	  at = alloc ;
	  h[ind] = alloc++ ;
	} else {
	  at = h[ind] ;
	}
      }
      v[at].strings++ ;
      v[at].childcounts.push_back(1) ;
    }
    int X = 0 ;
    for (int i=0; i<v.size(); i++)
      X += min(N, v[i].strings) ;
    long long prod = 1 ;
    for (int i=1; i<v.size(); i++)
      v[v[i].parent].childcounts.push_back(min(N, v[i].strings)) ;
    for (int i=0; i<v.size(); i++) {
      trie &tr = v[i] ;
      int vp = min(N, tr.strings) ;
      if (debug) {
            cout << "At node " << i << " vp " << vp << " :" ;
            for (int j=0; j<tr.childcounts.size(); j++)
	      cout << " " << tr.childcounts[j] ;
            cout << endl ;
      }
      if (tr.childcounts.size() < 2)
	continue ;
      long long poss[120] ;
      sort(tr.childcounts.begin(), tr.childcounts.end()) ;
      for (int j=0; j<=vp; j++)
	poss[j] = 0 ;
      int minv = tr.childcounts[tr.childcounts.size()-1] ;
      poss[minv] = comb[vp][minv] ;
      if (debug)
	cout << "Initial possibility at " << minv << " is " << poss[minv] << endl ;
      int sum = minv ;
      for (int j=tr.childcounts.size()-2; j>=0; j--) {
	int cnt = tr.childcounts[j] ;
	sum = min(N, cnt+sum) ;
	for (int k=sum; k>=minv; k--) {
	  long long addme = 0 ;
	  for (int m=0; m<=cnt; m++) {
	    if (k-m < 0 || vp-(k-m) < 0)
		continue ;
	    if (debug)
	      cout << "Looking up " << comb[k-m][cnt-m] << " and " << comb[vp-(k-m)][m] << endl ;
	    addme = add(addme,
		mult(mult(poss[k-m], comb[k-m][cnt-m]), comb[vp-(k-m)][m])) ;
	  }
	  poss[k] = addme ;
	  if (debug)
	    cout << "From j " << j << " k " << k << " adding " << addme << endl ;
	}
      }
      if (debug)
	cout << "At node " << i << " multiplying by " << poss[vp] << endl ;
      prod = mult(prod, poss[vp]) ;
    }
    cout << X << " " << prod << endl ;
  }
}
