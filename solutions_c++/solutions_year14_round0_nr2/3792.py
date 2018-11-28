#include<cstdio>
#include<algorithm>
using namespace std;
int main ()
{
	double c, f, x;
	int t;
	scanf ( "%d", &t );
	for ( int i = 1; i <= t; i ++ )
	{
		printf ( "Case #%d: ", i );
		scanf ( "%lf %lf %lf\n", &c, &f, &x );
		double ans = 0, b = 2.0;
		while ( x )
		{
			if ( x / b < c / b + x / (f + b) ) 
			{
				ans += x / b;
				x = 0;
			}
			else 
			{
				ans += c / b;
				b += f;
			}
		}
		printf ( "%.7lf\n", ans );
	}
	return 0;
}