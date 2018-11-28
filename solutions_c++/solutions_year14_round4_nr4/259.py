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
const int INF = 1000*1000*1000 ;
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

template<class T1, class T2> ostream & operator<<(ostream &s, pair<T1,T2> x) { s << "(" << x.FI << "," << x.SE << ")" ; return s ; }
template<class T> ostream & operator<<(ostream &s, const vector<T> &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T1, class T2> ostream & operator<<(ostream &s, const map<T1, T2> &t) { FOREACH(it, t) s << *it << " " ; return s ; }

const int MAXN = 10 ;
const int MOD = 1000000007 ;
string s[MAXN] ;

void _main() {
	int n, m, i, j ;
	cin >> m >> n ;
	REP(i,m) cin >> s[i] ;
//	cout << m << " " << n << endl ;
	int ret=0, counter=0 ;
	int end=power(n,m) ;
//	cout << "end=" << end << endl ;
	for(int way=0 ; way<end ; way++) {
		set<string> T[MAXN] ;
		int w=way ;
		for(j=0 ; j<m ; j++) {
			int where = w%n ;
//			cout << "where = " << where << endl ;
//			cout << j << ") where = " << where << " " << s[j] << endl ;
			w /= n ;
			for(int p=0 ; p<=s[j].size() ; p++) {
//				cout << "klade " << where << " " << s[j].substr(0, p) << endl ;
				T[where].insert(s[j].substr(0, p)) ;
			}
		}
		int act=0 ;
		REP(j,n) act+=T[j].size() ;
		if(act > ret) {
			ret = act ;
			counter=1 ;
/*			REP(j,n) {
				cout << j << ") " ;
				FOREACH(q, T[j]) cout << *q << " " ;
				cout << endl ;
			}*/
		}
		else if(act==ret) {
			counter = (counter+1)%MOD ;
		}
	}
	cout << ret << " " << counter << endl ;
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

