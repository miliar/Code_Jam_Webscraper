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

const int MAXN = 1000100 ;
int t[MAXN] ;
LL sum[MAXN] ;

void _main() {
	LL p, q, r, s ;
	int n, i ;
	cin >> n >> p >> q >> r >> s ;
	for(i=1 ; i<=n ; i++) t[i] = ((((i-1) * p + q) % r) + s) ;
	for(i=1 ; i<=n ; i++) sum[i] = sum[i-1]+t[i] ;
	LL ret=0 ;
	int j=0 ;
	for(int b=1 ; b<=n ; b++) {
		while(j<b && sum[j+1]*2<=sum[b]) j++ ;
		ret = max(ret, sum[n]-max(max(sum[j], sum[b]-sum[j]), sum[n]-sum[b])) ;
		if(j<b)
			ret = max(ret, sum[n]-max(max(sum[j+1], sum[b]-sum[j+1]), sum[n]-sum[b])) ;
	}
	cout << (double)ret/sum[n] << endl ;
}

int main()
{
	ios_base::sync_with_stdio(0) ;
	cout.setf(ios::fixed) ;
	cout.precision(10) ;
	int C ;
	cin >> C ;
	for(int tests=1 ; tests<=C ; tests++) {
//		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		_main() ;
	}
}

