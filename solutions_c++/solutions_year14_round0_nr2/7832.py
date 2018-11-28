#include <stdio.h>
double C, F , X ;
double sum;

void calc( double Remain , double speed )
{
	double t1 =  ( Remain / speed ) ;
	double t2 = ( C / speed ) + ( Remain / ( speed + F ) ) ;
	if ( t1 <= t2 ) {
		sum += t1;
		return ; 
	}
	sum += (C /speed ) ;
	calc( Remain , speed + F ) ; 
}

void solve(int n) 
{
	int sol;
	float time;
	sum  = 0;
	calc(X,2.0) ; 	
	printf("Case #%d: %.10f\n" , n,sum ) ;
}

int main()
{
	int n;
	scanf("%d" , &n ) ;
	for ( int i = 0 ; i < n ; i ++ )
	{
		scanf("%lf %lf %lf" , &C, &F , &X ) ;
		solve(i+1);
	}
	return 0;
}
