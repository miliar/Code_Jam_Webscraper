#include <cstdio>

long long n , k;

void read() {
	scanf ( "%lld%lld" , &n , &k );
}

void solve() {
	long long pow = 4;
	long long ans1 = 0 , ans2 = 0;
	long long i;
	
	for (i = 2; i < (1LL << n); i *= 2) {
//		printf ( "%lld  %lld\n" , k , (1 << n) / i * (i - 1) );
		if ( k > (1LL << n) / i * (i - 1) ) {
			ans1 = pow - 2;
		}
		pow *= 2;
	}
	
	for (i = 1; i <= (1LL << n); i *= 2) {
		if ( k >= (1LL << n) / i ) {
			ans2 = (1LL << n) - i;
			break;
		}
	}
	
	if ( k == (1LL << n) ) ans1 = (1LL << n) - 1;
	
	printf ( "%lld %lld\n" , ans1 , ans2 );
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
