#include <cstdio>
#include <algorithm>
using namespace std ;
int n ;
int a[10000];

int main() {
	int T , test = 1 ;
	scanf("%d",&T);
	while ( T-- ) {
		scanf("%d",&n);
		++n ;
		int ans = 0 , s = 0 ; 
		for ( int i = 0 ; i < n ; ++i ) {
			scanf("%1d",&a[i]);
			if ( s < i )
				ans = max( ans , i-s ) ;
			s += a[i] ;
		}
		printf("Case #%d: %d\n",test++,ans);
	}
	return 0;
}