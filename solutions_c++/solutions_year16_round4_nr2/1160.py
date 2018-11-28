/*                                                            */
/*       Lukasz Marecik, lm277561@students.mimuw.edu.pl       */
/*                                                            */
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
#include <bitset>
#include <sstream>
#include <ext/numeric>
#include <gmpxx.h>				// -lgmpxx -lgmp
//#include <NTL/mat_lzz_p.h> 	// -lntl
using namespace std ;
using namespace __gnu_cxx ;
//using namespace NTL ;
typedef mpz_class BIGNUM ;
typedef long long LL ;
typedef pair<int,int> PII ;
typedef vector<int> VI ;
const int INF = 1e9+100 ;
const LL INFLL = (LL)INF*INF ;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define FOREACH(i,c) for(auto i=(c).begin();i!=(c).end();++i)
#define CLEAR(t) memset(t,0,sizeof(t))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

template<class T1,class T2> ostream& operator<<(ostream &s, const pair<T1,T2> &x) { return s << "(" << x.FI << "," << x.SE << ")" ;}
template<class T>           ostream& operator<<(ostream &s, const vector<T>   &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T>           ostream& operator<<(ostream &s, const set<T>      &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T1,class T2> ostream& operator<<(ostream &s, const map<T1, T2> &t) { FOREACH(it, t) s << *it << " " ; return s ; }

template<class T1, class T2> T1 conv(const T2 &x) {
	stringstream sss ; sss << x ; T1 y ; sss >> y ; return y ;
}

template<class T> void _debug(bool printName, const char* s, const T &x) { if(printName) cerr << s << "=" ; cerr << x << endl ; }
void _debug(bool, const char* s, const char*) {
	for(;*s;s++) if(*s!='"') { cerr << *s ; } cerr << endl ;
}
template<class T, class... R> void _debug(bool printName, const char* s, const T &x, R... y) {
	bool o=0, str=(*s=='"') ;
	for(; o || *s!=',' ; s++) if(*s=='"') o=!o ; else if(printName||str) cerr<<*s ;
	for(s++;*s && *s==' '; s++) ;
	if(!str) { if(printName) cerr << "=" ; cerr << x ; if(*s!='"' && printName) cerr << "," ; } cerr << " " ;
	_debug(printName, s, y...) ;
}

template<class T>             void _coord(const T &x)         { cerr << "[" << x << "]" ;             }
template<class T, class... R> void _coord(const T &x, R... y) { cerr << "[" << x << "]" ; _coord(y...) ; }

template<class T, class I>             void _val(T &t, const I &i)         { cerr << t[i] ; }
template<class T, class I, class... J> void _val(T &t, const I &i, J... j) { _val(t[i], j...) ; }

#ifndef LOCAL
	#define CERR(...)
	#define DEBUG(...)
	#define DARRAY(...)
#else
	#define CERR(...)     if(DFLAG) _debug(0, #__VA_ARGS__, __VA_ARGS__)
	#define DEBUG(...)    if(DFLAG) _debug(1, #__VA_ARGS__, __VA_ARGS__)	
	#define DARRAY(t,...) if(DFLAG) { cerr << #t ; _coord(__VA_ARGS__) ; cerr << " = " ; _val(t,__VA_ARGS__) ; cerr << endl ; }
#endif

////////////////////////////////////////////////////////////////////////////////
void __init() ;
void __main() ;

int main()
{
	ios_base::sync_with_stdio(0) ;
	cout.setf(ios::fixed) ; cout.precision(10) ;
	cerr.setf(ios::fixed) ; cerr.precision(10) ;
	__init() ;
	int C ;
	cin >> C ; cin.ignore() ;
	for(int tests=1 ; tests<=C ; tests++) {
//		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		__main() ;
	}
}
#define DFLAG 1
////////////////////////////////////////////////////////////////////////////////

double C[100+1][100+1] ;
void Newton(int n) {
	C[0][0] = 1 ;
	for(int i=1 ; i<=n ; i++) {
		C[i][0] = C[i][i] = 1 ;
		for(int j=1 ; j<i ; j++)
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) ; //%MOD ;
	}
}

void __init() {
	Newton(100) ;
}
////////////////////////////////////////////////////////////////////////////////

const int MAXN=18 ;
double prob[MAXN] ;
int n, k ;

double S[MAXN], _next[MAXN] ;

void __main() {
	cin >> n >> k ;
	k/=2 ;
	REP(i, n) cin >> prob[i] ;
	
	double ret=0 ;
	REP(mask, (1<<n))
		if(__builtin_popcount(mask)==2*k) {
			CLEAR(S) ;
			S[0]=1 ;
			REP(i, n) {
				if(mask&(1<<i)) {
					CLEAR(_next) ;
					for(int j=k ; j>=0 ; j--) {
						_next[j+1] += S[j]*prob[i] ;
						_next[j]   += S[j]*(1-prob[i]) ;
					}
					for(int j=0 ; j<=k ; j++)
						S[j]=_next[j] ;
				}
			}
			ret = max(ret, S[k]) ;
		}
	cout << ret << endl ;
}

