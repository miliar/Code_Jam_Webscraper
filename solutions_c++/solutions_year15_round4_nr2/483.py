#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define eps (1e-7)
const double Inf = 123129387129312938721931232132148124.0;

int T, n, Case;
double V, X, R[105], C[105] ;

int main()
{
	double v0, v1 ;
	int i ;
	
	freopen("B-small-attempt0.in","r",stdin) ;
	freopen("output.txt","w",stdout) ; 
	
	for( scanf("%d", &T) ; T-- ; ) {
		scanf("%d%lf%lf", &n, &V, &X) ;
		rep( i, 1, n ) 
			scanf("%lf%lf", &R[i], &C[i]) ;
		
		if( n == 1 ) {
			if(abs(C[1] - X)<eps)
				printf("Case #%d: %.8lf\n", ++Case, V/R[1]) ;
			else 
				printf("Case #%d: IMPOSSIBLE\n", ++Case) ;
		} else {
			if((abs(C[1]-X)<eps)&&(abs(C[2]-X)<eps)) {
				printf("Case #%d: %.8lf\n", ++Case, V/(R[1]+R[2])) ;
			} else if((abs(C[1]-X)<eps)||(abs(C[2]-X)<eps)) {
				v0 = v1 = Inf ;
				if(abs(C[1]-X)<eps)
					v0 = V/R[1] ;
				if(abs(C[2]-X)<eps)
					v1 = V/R[2] ;
				printf("Case #%d: %.8lf\n", ++Case, min( v0, v1)) ;
			} else if(abs(C[1]-C[2]) < eps) 
				printf("Case #%d: IMPOSSIBLE\n", ++Case) ;
			else {
				v0 = V*(X-C[2])/(C[1]-C[2]) ;
				v1 = V-v0 ;
				if((v0<0) || (v1<0))
					printf("Case #%d: IMPOSSIBLE\n", ++Case) ;
				else 
					printf("Case #%d: %.8lf\n", ++Case, max(v0/R[1], v1/R[2])) ;
			}
		}
	}
	return 0 ;
}

