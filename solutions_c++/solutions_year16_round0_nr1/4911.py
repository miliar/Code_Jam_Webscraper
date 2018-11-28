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
		int N;
		scanf( "%d", &N );

		printf( "Case #%d: ", tc );

		if ( N == 0 ) { puts( "INSOMNIA" ); continue; }

		bool flag[10] = {false};
		int  cnt = 0;
		
		LL curr = 0;
		while ( cnt != 10 ) {
			curr += N;
			LL tmp = curr;
			while ( tmp != 0 ) {
				int x = tmp % 10;
				if ( !flag[x] ) flag[x] = true, cnt++;
				tmp /= 10;
			}
		}

		printf( "%lld\n", curr );
	}

	return 0;
}
