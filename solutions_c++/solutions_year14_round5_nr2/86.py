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

const int MAXN = 110 ;
int P, Q, N ;
int h[MAXN] ;
int g[MAXN] ;
int t[MAXN][210][1100][2][2] ;

bool me(int i, int wys) {
	return wys-P<=0 ;
}
bool tower(int i, int wys) {
	return wys-Q<=0 ;
}

int f(int i, int wys, int shots, bool begin, bool turn) {
	assert(shots < 1100) ;
	int &ret = t[i][wys][shots][begin][turn] ;
	if(ret == -1) {
		if(i>=N) return 0 ;
		
		if(begin && shots>0) {
			bool kill = me(i, wys) ;
			if(kill) ret = max(ret, g[i]+f(i+1, h[i+1], shots-1, true, turn)) ;
			else     ret = max(ret,      f(i,   wys-P,  shots-1, true, turn)) ;
		}
		
		if(turn==1) {
			bool kill = tower(i, wys) ;
			if(kill) ret = max(ret, f(i+1, h[i+1], shots, true,  !turn)) ;
			else     ret = max(ret, f(i,   wys-Q,  shots, false, !turn)) ;
		}
		else {
			ret = max(ret, f(i, wys, shots+1, false, !turn)) ; // opuszczam
			
			bool kill = me(i, wys) ;
			if(kill) ret = max(ret, g[i]+f(i+1, h[i+1], shots, true,  !turn)) ;
			else     ret = max(ret,      f(i,   wys-P,  shots, false, !turn)) ;
		}		
	}
	return ret ;
}

void _main() {
	cin >> P >> Q >> N ;
	int i ;
	REP(i,N) cin >> h[i] >> g[i] ;
	memset(t, -1, sizeof(t)) ;
	cout << f(0,h[0],0, true, 0) << endl ;
}

int main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(int tests=1 ; tests<=C ; tests++) {
		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		_main() ;
	}
}

