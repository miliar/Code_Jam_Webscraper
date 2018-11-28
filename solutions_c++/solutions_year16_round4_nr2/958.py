#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

const int N = 400 ; 

int n ; 

double p[N] ; 

double f[N][N] ; 

int id[N] ; 

double ans = 0 ; 

int K ; 


int main() {
	int ca ;
	scanf("%d",&ca ) ; 
	for( int cc = 1 ; cc <= ca ; cc ++ ) {
		scanf("%d%d",&n,&K )  ;
		for( int i=1 ; i<=n ; i++ ) {
			scanf("%lf",&p[i] ) ; 
		}
		ans = 0 ; 
		sort( p+1 , p+1+n ) ; 
		int k = K ; 
		for( int l=0 ; l<=K ; l++ ) {
			int cnt = 0 ; 
			for( int j=1 ; j<=l ; j++ ) id[++cnt] = j ;
			int lef = k-l ; 
			for( int j=n-lef+1 ; j<=n ; j++) id[++cnt] = j ; 
			f[0][0] = 1 ; 
			for( int i=1 ; i<=k ; i++ ) {
				for( int j=0 ; j<=k/2 ; j++ ) {
					f[i][j] = 0 ; 
					if( j ) {
						f[i][j] += f[i-1][j-1] * p[ id[i] ] ; 
					} 
					f[i][j] += f[i-1][j] * ( 1-p[ id[i] ] ) ; 
				}
			}
			ans = max( ans , f[k][k/2] ) ; 

		}
		printf("Case #%d: ",cc ) ;  
		printf("%.8lf\n",ans  ) ; 
	}
}

