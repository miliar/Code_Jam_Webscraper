#include <stdio.h>
#include <iostream>
using namespace std ;

double C,F,X ;
double s ;
int T ;
double EPS = 1e-9 ;
double ans ; 

int main()
{
	freopen("B1.in","r",stdin) ;
	freopen("B1.out","w",stdout) ;
	int i ;
	while(cin>>T) {
		for( i = 1 ; i <= T ; i ++ ) {
			cin>>C>>F>>X ;
			s = 2 ;
			ans = 0 ;
			while( ( X / s - C / s - X / ( s + F ) ) > EPS ) {
				ans += C / s ; 
				s += F ;
			}
			ans += X / s ;
			printf("Case #%d: %.7lf\n",i,ans);
		}
	}

	return 0 ;
}