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

LL worst(LL i, LL n) {
	LL size = 1ll<<n ;
	if(i==1) return 1 ;
	else {
		LL A = i-2 ;
		LL B = size-i ;
		return size/2 + worst(A/2 + 1, n-1) ;
		/*if(A<=B)
			return size/2 + worst(A+1, n-1) ;
		else
			return size/2 + worst(B + (A-B)/2 +1, n-1) ;*/
	}
}
LL best(LL i, LL n) {
	LL size = 1ll<<n ;
	if(i==size) return size ;
	else return best(i-(i-1)/2, n-1) ;
}

LL BS(LL l, LL r, LL n, LL p, LL (*f)(LL, LL) ) {
	while(l<r) {
		LL sr = (l+r)/2 ;
		LL temp = f(sr+1, n) ;
//		cout << sr+1 << " -> " << temp << endl; 
		if(temp > p) r=sr ;
		else l=sr+1 ;
	}
	return l ;
}

void _main() {
	LL n ;
	LL P ;
	cin >> n >> P ;
	cout << BS(1, 1ll<<n, n, P, worst)-1 << " " ;
	//cout << endl ;
	cout << BS(1, 1ll<<n, n, P, best)-1 << endl ;
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

