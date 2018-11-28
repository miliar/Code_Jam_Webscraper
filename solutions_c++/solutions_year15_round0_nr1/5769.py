#include <bits/stdc++.h>

long long int read() {
	char c = getchar_unlocked();
	while( c < '0' || c > '9')
		c = getchar_unlocked();
	long long int ret = 0;
	while(c >= '0' && c <= '9' ) {
		ret = 10 * ret + c - 48;
		c = getchar_unlocked();
	}
	return ret;
}

int main() {
	long long int i, test, t, max, ans, n, cur;
	char a[10000];
	t = read();
	for( test=1;test<=t;test++ ) {
		max = read();
		n = max + 1;
		ans = 0;
		scanf( "%s", a );
		cur = a[0] - '0';
		for(i=1;i<n;i++) {
			//printf( "Cur = %lld, i = %lld\n", cur, i );
			if( cur < i ) {
				ans += i - cur;
				cur = i;
			}
			cur = cur + a[i] - '0';
		}
		printf( "Case #%lld: %lld\n", test, ans );
	}

	return 0;
}