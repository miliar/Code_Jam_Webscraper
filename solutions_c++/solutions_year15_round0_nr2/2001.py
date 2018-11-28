#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<stack>
#include<fstream>
#include<sstream>
#include<map>
#include<algorithm>
#include<cassert>
#include<vector>
#include<climits>

#define DEBUG 0
#define SMALL 0
#define LARGE 1

using namespace std;
#if DEBUG
#define TRACE(a) cerr << "value of " << #a << ":" << a << endl
#define TRACE(a,b) TRACE(a);TRACE(b)
#define TRACE(a,b,c) TRACE(a,b);TRACE(c)
#define TRACE(a,b,c,d) TRACE(a,b);TRACE(c,d)
#else
#define TRACE(a) 
#define TRACE(a,b) 
#define TRACE(a,b,c) 
#define TRACE(a,b,c,d) 
#endif

#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a);

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()


typedef long long int64;
typedef unsigned long long uint64;


#define MAX 1010
int arr[MAX];

int main() {
#if SMALL
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);
#endif
#if LARGE
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	int T,D,N;
	
	si(T);
	
	FOR(test,1,T) {
		si(N);
		int m=INT_MIN;
		FOR(i,0,N-1){
			si(arr[i]);
			if(m<=arr[i]) {
				m = arr[i];
			}
		}
		long long int  ans=INT_MAX;
		long long int s=0;
		FORD(i,m,1) {
			s = i;
			//s += ((m-i-1)/i);
			FOR(j,0,N-1){
				s += ((arr[j]-1)/(i));
			}
			if(ans>=s) ans = s;
		}
		cout << "Case #"<< test << ": " << ans << endl;
	}
	return 0;
}
