#include <cstdio>
#include <cstdlib>

void Solve( int caseId )
{
	double C, F, X;
	scanf("%lf %lf %lf\n", & C, & F, & X );

	double cps = 2;
	double time = 0;
	double cookies = 0;

	while( cookies < X )
	{
		// isnt it better to just wait?
		if( X / cps < C / cps + X / (cps + F) )
		{
			time += X / cps;
			// printf("waiting %lfs\n", X/cps);
			break;
		}

		// how long to get farm
		time += C / cps;
		// cookies = 0;

		// update cps (cookie per sec)
		cps += F;
		// printf("%lfs cps=%lf %lf\n", time, cps, cookies);
	}

	printf( "Case #%d: %lf\n", caseId, time );
}

int main()
{
	int cases;
	scanf( "%d\n", & cases );
	for( int i = 1; i <= cases; i++ )
		Solve( i );

	return 0;
}