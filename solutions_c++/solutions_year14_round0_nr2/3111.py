#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std ;

double C, F, X, Ans, N ;
int Case, T ;

int main()
{
	double p0, p1 ;
	
	freopen("B_large.in","r",stdin) ;
	freopen("B_large.out","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		Ans = 0 ;
		N = 2.0 ;
		
		scanf("%lf%lf%lf", &C, &F, &X) ;// X-determination
		for( ; ; ) {
			p0 = X / N ; 
			p1 = C / N + X / ( N + F ) ;
			if( p0 < p1 ) {
				Ans += p0 ;
				break ;	
			} else {
				Ans += C / N ;
				N += F ;
			}
		}
		printf("Case #%d: %.7lf\n", ++Case, Ans) ;
	}
//	system("pause") ;
	return 0 ; 
}
