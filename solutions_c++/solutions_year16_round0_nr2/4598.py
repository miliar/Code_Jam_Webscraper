#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

const int N = 110  ;

int i , j , k , n , m ; 

bool pos ;

char s[N] ;

int main() {
	int Ca ;
	int cnt = 0 ;
	for( scanf("%d",&Ca ) ; Ca ; Ca -- ) {
		cnt ++ ;
		printf("Case #%d: ",cnt ) ;

		scanf("%s",s+1 ) ;
		pos = 0 ;
		if( s[1]=='+' ) pos = 1 ;
		n = strlen( s + 1 ) ;
		int ans = 0 ;
		for( i=2 ; i<=n ; i++ ) if( ( s[i]=='+' && pos==0 ) || ( s[i]=='-' && pos ) ) {
			ans ++  ;
			pos = 0 ;
			if( s[i]=='+' ) pos = 1 ;
		}
		if( pos==0 ) ans ++ ;
		printf("%d\n",ans ) ;
	}
}
