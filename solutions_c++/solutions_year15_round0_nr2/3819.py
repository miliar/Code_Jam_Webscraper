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
		
		int ans = 100000 ;
		for ( int i = 0 ; i < n ; ++i ) {
			scanf("%1d",&a[i]);
		}
		
		for ( int st = 1 ; st <= 1000 ; ++st ) {
			int t = 0 ;
			for ( int i = 0 ; i < n ; ++i ) {
				if ( a[i] > st ) {
					t += (a[i]-1)/st ;
				}
			}
			ans = min( ans , st+t);
		}
		
		printf("Case #%d: %d\n",test++,ans);
	}
	return 0;
}