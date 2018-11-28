#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

const int N = 8192; 

int n , m , T ; 

int s[3] , real[3] ; 

int base[N] ; 

struct pai {
	int x , y ; 
}z[N] ;

void Solve( int l , int r , int p , int c ) {
	if( l==r ) {
		base[l] = c ; 
		return  ;
	}
	int m = l + r >> 1 ; 
	Solve( l , m , p*2 , c ) ;
	Solve( m+1 , r , p*2+1 , ( c+1 ) % 3 ) ; 
	for( int i=l , j=m+1 ; i<=m ; j++ , i++ ) {
		if( base[i] < base[j] ) break ;
		if( base[i] > base[j] ) {
			for( ; i<=m ; i++ , j++ ) {
				swap( base[i] , base[j] )  ;
			}
			break ; 
		}
	}
}

bool cmp( pai a , pai b ) {
	return a.x < b.x || ( a.x==b.x && a.y < b.y ) ; 
}

int alpa[N] ;

int main() {
	scanf("%d",&T ) ;
	int ca = 0 ; 
	while( T-- ) {
		ca ++ ; 
		scanf("%d%d%d%d",&n,&s[1],&s[0],&s[2] ) ; 
		n = ( 1 << n ) ; 
		memset( alpa , 255 , sizeof alpa ) ; 
		for( int i=0 ; i<3 ; i++ ) {
			Solve( 1 , n , 1 , i ) ; 
			int cnt = 0  ;
			real[0] = real[1] = real[2] = 0 ; 
			for( int j=1 ; j<=n ; j++ ) real[ base[j] ] ++ ; 
			if( real[0] != s[0] || real[1]!=s[1] || real[2]!=s[2] ) continue  ;

			bool ju = 0 ; 
			if( alpa[0] == -1 ) {
				ju = 1 ; 
			}
			if( ju==0 ) {
				for( int j=1 ; j<=n ; j++ ) {
					if( base[j] < alpa[j] ) {
						ju = 1 ;
						break ; 
					} 
					if( base[j] > alpa[j] ) {
						ju = 0 ;
						break ;
					}
				}
			}
			if( ju ) {
				memcpy( alpa , base , sizeof alpa ) ;
			}
		}
		printf("Case #%d: ",ca ) ;  
		if( alpa[0]!=-1 ) {
			for( int i=1 ; i<=n ; i++ ) if( alpa[i]==0 ) printf("P" ) ; 	
				else if( alpa[i]==1 ) printf("R" ) ;
					else printf("S" ) ; 
		} else printf("IMPOSSIBLE" ) ; 
		if( T ) puts("" ) ; 
	}
}
