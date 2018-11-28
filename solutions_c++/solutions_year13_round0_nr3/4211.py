#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;

vector <LL> v;

bool is_palin(LL n) {
	char s[50];
	sprintf( s, "%I64d", n );
	for ( int i = 0, j = strlen(s) - 1; i < j; i++, j-- )
		if ( s[i] != s[j] ) return false;
	return true;
}

int main()
{
	FOR(i,1,10000000) {
		if ( !is_palin(i) ) continue;
		LL x = (LL) i * i;
		if ( !is_palin(x) ) continue;
		v.push_back(x);
	}

	int T;
	scanf( "%d", &T );

	FOR(tc,1,T) {
		LL a, b;
		cin >> a >> b;
		int ans = upper_bound(v.begin(),v.end(),b) - lower_bound(v.begin(),v.end(),a);
		printf( "Case #%d: %d\n", tc, ans );
	}

	return 0;
}
