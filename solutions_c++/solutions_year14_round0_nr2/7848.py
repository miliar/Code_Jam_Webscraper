#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string>

#define FORr(i,A,B)	for (int i=(A); i<(B); ++i)
#define FOR(i, N)	FORr(i,0,N)

using namespace std;

int 	get_int()		{int a; 	scanf("%d", &a); 	return a;}
double	get_double()	{double a;	scanf("%lf", &a);	return a;}
char	get_char()		{char c; 	scanf("%c", &c); 	return c;}

char str_buf[100000];
string	get_str()		{scanf("%s", str_buf); return str_buf;}

double solve2( double C, double F, double X, int farms )
{
	double cost = 0.0;
	double prod = 2.0;

	FOR( i, farms ) {
		cost += C / prod;
		prod += F;
	}

	cost += X / prod;

	return cost;
}

void solve()
{
	double C = get_double();
	double F = get_double();
	double X = get_double();

	double cost = -1.0;
	for ( int farms = 0;; ++farms )
	{
		double cost2 = solve2( C, F, X, farms );
		if ( cost < 0.0 )
		{
			cost = cost2;
		}
		else if ( cost > cost2 )
		{
			cost = cost2;
		}
		else if ( cost < cost2 )
		{
			printf( "%.7lf", cost );
			return;
		}
	}
}

int main()
{
	int T = get_int();

	FOR (t, T)
	{
		printf("Case #%d: ", t + 1);
		solve();
		printf("\n");
	}
}
