#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>

using namespace std ;

int i , j , k , n , m ; 

typedef long long ll ;

#define N 18 

int bit[N] ;

int divisor( ll va ) {
	ll top = sqrt( va ) ;
	for( ll j=2 ; j<=top ; j++ ) if( va % j == 0 ) return j ;
	return 0 ;
}

int tmp[N] ;

void Dfs( int dep ) {
	if( !m ) return ;
	if( dep>n ) {
		for( int i=2 ; i<=10 ; i++ ) {
			ll ori = 1 ;
			ll sig = 0 ;
			for( int j=1 ; j<=n ; j++ , ori = ori * i ) {
				if( bit[j] ) sig += ori ;
			}
			tmp[i] = divisor( sig ) ;
			if( tmp[i] == 0 ) {
				return ;
			}
		}
		for(  int i=n ; i ; i-- ) printf("%d",bit[i] ) ;
		for(  int i=2 ; i<=10 ; i++ ) printf(" %d",tmp[i] ) ;
		puts("" ) ;
		--m ;
		return ;
	}
	bit[dep] = 1 ;
	Dfs( dep + 1 ) ;
	if( dep!=n && dep!=1 ) {
		bit[dep] = 0  ;
		Dfs( dep + 1 ) ;
	}
}

int main() {
	int Ca ;
	scanf("%d",&Ca ) ;
	int cnt = 0 ;
	while( Ca-- ) {
		cnt ++ ;
		printf("Case #%d:\n",cnt ) ;
		scanf("%d%d",&n,&m ) ;
		Dfs( 1 ) ;
	}
}
