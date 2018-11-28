#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cassert>
#include <cstring>
#include <sstream>
#include <ext/numeric>
#include <gmpxx.h>			// -lgmpxx -lgmp
using namespace std ;
using namespace __gnu_cxx ;
typedef mpz_class BIGNUM ;
typedef long long LL ;
typedef pair<int,int> PII ;
typedef vector<int> VI ;
const int INF = 1e9 ;
const LL INFLL = (LL)INF * (LL)INF ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define CLEAR(t) memset(t,0,sizeof(t))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

template<class T1,class T2> ostream& operator<<(ostream &s, const pair<T1,T2> &x) { s<< "(" << x.FI << "," << x.SE << ")"; return s;}
template<class T>           ostream& operator<<(ostream &s, const vector<T>   &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T>           ostream& operator<<(ostream &s, const set<T>      &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T1,class T2> ostream& operator<<(ostream &s, const map<T1, T2> &t) { FOREACH(it, t) s << *it << " " ; return s ; }

//////////////////////////////////////////////////////////////

const int MAXN = 15 ;

bool t[MAXN+1][1<<MAXN] ;

bool agree(int i, int a) {
	if(a==-1) return true ;
	else return i==a ;
}

void _main() {
	int n, i, j, m, a ;
	cin >> n ;
	int next=0 ;
	char action ;
	map<int, int> change ;
	CLEAR(t) ;
	for(m=0 ; m<(1<<n) ; m++)
		t[0][m] = true ;
	
	for(i=1 ; i<=n ; i++) {
		cin >> action >> a ;
		if(a==0) a=-1 ;
		else {
			if(change.find(a) == change.end())
				change[a] = next++ ;
			a = change[a] ;
		}
		for(m=0 ; m<(1<<n) ; m++) {
			if(!t[i-1][m]) continue ;
			
			if(action=='E') {
				for(j=0 ; j<n ; j++) {
					if(!agree(j, a)) continue ;
					
					if(m&(1<<j)) continue ;
					t[i][m^(1<<j)] |= t[i-1][m] ;
				}
			}
			else {	// L
				for(j=0 ; j<n ; j++) {
					if(!agree(j, a)) continue ;
					
					if(!(m&(1<<j))) continue ;
					t[i][m^(1<<j)] |= t[i-1][m] ;
				}
			}
		}
	}
	int ret=INF ;
	for(m=0 ; m<(1<<n) ; m++)
		if(t[n][m])
			ret = min(ret, __builtin_popcount(m)) ;
			
	if(ret==INF) cout << "CRIME TIME" << endl ;
	else cout << ret << endl ;
}

int main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(int tests=1 ; tests<=C ; tests++) {
//		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		_main() ;
	}
}

