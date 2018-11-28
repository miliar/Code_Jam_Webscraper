#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

int i , j , k , n , m ; 

typedef long long ll ;

bool ext[10] ;

int main() {
	int Ca = 0 ;
	int cnt = 0 ;
	for( scanf("%d",&Ca ) ; Ca ; Ca-- ) {
		cnt ++ ;
		printf("Case #%d: ",cnt ) ;
		scanf("%d",&n ) ;
		if( n==0 ) {
			puts("INSOMNIA" ) ;
			continue ;
		}
		int appear = 0 ;
		ll ans = 0 ;
		memset( ext , 0 , sizeof ext ) ;
		for( ll a=n ;  ; a+=n ) {
			ll b = a ;
			while( b ) {
				int t = b % 10 ; 
				if( ext[t] == 0  ) {
					ext[t] = 1 ;
					appear ++ ; 
				}
				b /= 10  ;
			}
			if( appear==10 ) {
				ans = a ;
				break ; 
			}
		}
		printf("%lld\n",ans ) ;
		
	}
}
