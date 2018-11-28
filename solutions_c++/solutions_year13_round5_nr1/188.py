#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;
typedef long long LL ;
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

const int MAXN = 40 ;
LL t[MAXN] ;

double try_(LL S, LL B, LL N) {
	if(B == 0) return 0 ;
	LL x = t[0] ;
	int i ;
	REP(i,N) t[i] -=x ;
	
	vector<int> pom ;
	
	LL need = 0 ;
	LL ile=0 ;
	REP(i,N) {
		if(t[i]<=S) {
			need += S-t[i] ;
			pom.PB(S-t[i]) ;
			ile++ ;
		}
	}
	sort(ALL(pom)) ;
//	cout << "need = " << need << ", ile = " << ile << endl ;
	double ret = 0 ;
	LL rezygnacja = 0 ;
	for(LL add = 0 ; need+add<=B && add<ile ; add++) {
//		cout << "add= " << add << endl ;
		ret = max(ret, -(double)need -add + 36*(double)(need-rezygnacja)/(ile-add)) ;
//		cout << "ret = " << ret << endl ;
		rezygnacja += pom[add] ;
	}
	
	return ret ;
}

void _main() {
	CLEAR(t) ;
	
	LL N, B ;
	cin >> B >> N ;
	int i ;
	REP(i,N) cin >> t[i] ;
	sort(t, t+37) ;
	double ret = 0 ;
	for(i=1 ; i<=B ; i++) ret = max(ret, try_(i, B, 37)) ;
	cout.setf(ios::fixed) ;
	cout.precision(10) ;
	cout << ret << endl ;
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

