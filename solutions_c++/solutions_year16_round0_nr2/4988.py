#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

const int maxn = 105;

char S[maxn];

int reverse(int value, int len) {
	int ret = 0;
	while ( len-- ) {
		ret <<= 1;
		ret |= value & 1;
		value >>= 1;
	}
	return ret;
}

int flip(int value, int cut) {
	int ret = value & ~((1 << cut) - 1);
	int pan = value &  ((1 << cut) - 1);
	ret |= ~reverse(pan,cut) & ((1 << cut) - 1);
	return ret;
}

int main()
{
	int T;
	scanf( "%d", &T );

	FOR(tc,1,T) {
		scanf( "%s", S );

		int len = strlen(S);
		int goal = (1 << len) - 1;

		int init = 0;
		REP(i,strlen(S)) if ( S[i] == '+' ) init |= 1 << i;
		
		int ans[5000];
		memset(ans,-1,sizeof(ans));
		
		queue <int> q;
		q.push(init);
		ans[init] = 0;

		while ( !q.empty() && ans[goal] == -1 ) {
			int p = q.front(); q.pop();
			FOR(i,1,len) {
				int next = flip(p,i);
				if ( ans[next] != -1 ) continue;
				ans[next] = ans[p] + 1;
				q.push(next);
			}
		}

		printf( "Case #%d: %d\n", tc, ans[goal] );
	}

	return 0;
}
