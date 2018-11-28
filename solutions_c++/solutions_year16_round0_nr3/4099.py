#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;

LL get_factor(LL n) {
	for ( LL i = 2; i * i <= n; i++ )
		if ( n % i == 0 ) return i;
	return -1;
}

LL todec(int value, int base) {
	LL ret = 0;
	LL p   = 1;
	while ( value != 0 ) {
		ret += (value & 1) * p;
		p   *= base;
		value >>= 1;
	}
	return ret;
}

int main()
{
	int T;
	scanf( "%d", &T );

	FOR(tc,1,T) {
		int N, J;
		scanf( "%d %d", &N, &J );

		printf( "Case #%d:\n", tc );
		
		int ans = 0;
		REP(bit,1<<(N-2)) {
			int value = 1 << (N - 1);
			value |= bit << 1;
			value |= 1;

			vector <LL> v;
			FOR(base,2,10) v.push_back(get_factor(todec(value,base)));

			bool valid = true;
			REP(i,v.size()) if ( v[i] == -1 ) valid = false;

			if ( valid ) {
				FORD(i,15,0) printf( "%d", value & (1 << i) ? 1 : 0 );
				REP(i,v.size()) printf( " %lld", v[i] );			
				puts("");
				ans++;
			}
			if ( ans == J ) break;
		}

	}

	return 0;
}
