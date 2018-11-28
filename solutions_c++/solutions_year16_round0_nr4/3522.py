#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;

int main()
{
	int T;
	scanf( "%d", &T );

	FOR(tc,1,T) {
		int K, C, S;
		scanf( "%d %d %d", &K, &C, &S );
		printf( "Case #%d:", tc );
		FOR(i,1,K) printf( " %d", i );
		printf( "\n" );
	}

	return 0;
}
