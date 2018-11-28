#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
using namespace std;
#define eps 1e-8
double r , t ;

void  equal( double  A, double  B, double  C, double & ans ){ 
    double  f=B*B-4*A*C; 
    ans=(-B+sqrt(f))/(2*A); 
}

int main(){
	freopen("A-small-attempt2.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	int cas , casn = 1 ;
	scanf("%d",&cas);
	while(cas--){
		scanf("%lf%lf",&r,&t);
		double ans ;
		equal( 2.0 , (2*r-1) , -t , ans );
		long long n = (int)ans ;
		printf("Case #%d: ",casn++);
		if( 2*n*r - 3*n +2*(n+n*n) <= t ){
			printf("%lld\n",n);
		}else
				printf("%lld\n",n-1);
	}
	return 0 ;
}