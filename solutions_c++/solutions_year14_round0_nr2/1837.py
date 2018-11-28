#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int cas,cc = 0;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		double f,x,g;
		scanf( "%lf %lf %lf", &f, &x, &g );
		double t = g / 2;
		double t1 = 0;
		double lx = 2;
		while ( t1 < t )
		{
			t1 += f / lx;
			lx += x;
			if ( t1 + g / lx < t )
				t = t1 + g / lx;
		}
		cc++;
		printf( "Case #%d: %.7lf\n", cc, t );
	}
	return 0;
}