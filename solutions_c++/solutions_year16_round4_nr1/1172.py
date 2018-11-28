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

void __init() {
	
}
////////////////////////////////////////////////////////////////////////////////

const int MAXN = 20 ;
int R[MAXN], P[MAXN], S[MAXN] ;

char win(char x, char y) {
	if(x=='R' && y=='P') return 'P' ;
	if(x=='R' && y=='S') return 'R' ;
	
	if(x=='P' && y=='S') return 'S' ;
	if(x=='P' && y=='R') return 'P' ;
	
	if(x=='S' && y=='P') return 'S' ;
	if(x=='S' && y=='R') return 'R' ;
	
	assert(false) ;
}

bool ok(vector<char> ret) {
	int i=0 ;
	while(!ret.empty()) {
		int r=0, p=0, s=0 ;
		FOREACH(it, ret) {
			if(*it=='R') r++ ;
			if(*it=='S') s++ ;
			if(*it=='P') p++ ;
		}
		if(r>R[i] || s>S[i] || p>P[i]) return false ;
		vector<char> tmp ;
		for(int j=0 ; j+1<ret.size() ; j+=2) {
			if(ret[j]==ret[j+1]) return false ;
			tmp.PB(win(ret[j],ret[j+1])) ;
		}
		
		ret = tmp ;
		i++ ;
	}
	return true ;
}

void __main() {
	int N ;
	cin >> N >> R[0] >> P[0] >> S[0] ;
	for(int i=1 ; i<=N ; i++) {
		int r=R[i-1], p=P[i-1], s=S[i-1] ;
		int a = (r+s-p)/2, b=(p+r-s)/2, c=(s+p-r)/2 ;
		if(!(2*(a+b+c)==r+p+s && 0<=a && a<=r && 0<=b && b<=p && 0<=c && c<=s)) {	
			cout << "IMPOSSIBLE" << endl ;
			return ;
		}
		R[i]=a ;
		P[i]=b ;
		S[i]=c ;
	}
	int all=R[0]+P[0]+S[0] ;
	int r=R[0], p=P[0], s=S[0] ;
	vector<char> ret ;
	while(ret.size()<all) {
		if(p) {
			p-- ;
			ret.PB('P') ;
			if(ok(ret)) continue ;
			else {
				ret.pop_back() ;
				p++ ;
			}
		}
		if(r) {
			r-- ;
			ret.PB('R') ;
			if(ok(ret)) continue ;
			else {
				ret.pop_back() ;
				r++ ;
			}
		}
		if(s) {
			s-- ;
			ret.PB('S') ;
			if(ok(ret)) continue ;
			else {
				ret.pop_back() ;
				s++ ;
			}
		}
		for(int k=0 ; k<=N ; k++)
			DEBUG(k, ")", R[k], P[k], S[k]) ;
		DEBUG(ret) ;
		assert(false) ;
	}
	FOREACH(it, ret) cout << *it ;
	cout << endl ;
}

