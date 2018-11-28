#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <math.h>

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "B-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		double fFarmPrice;
		double fFarmGain;
		double fTarget;

		fscanf( fin, "%lf %lf %lf", &fFarmPrice, &fFarmGain, &fTarget );
/*
		if ( fFarmGain <= 2.0 )
		{
			fprintf( fout, "Case #%d: %f\n", iCase + 1, fTarget / 2.0f );
			continue;
		}
*/
/*		double curGain = 2.0;
		double curTime = 0;
		while( true )
		{
			double nextFarmTime = fFarmPrice / curGain;
			double targetTime = fTarget / curGain;
			if ( targetTime < nextFarmTime )
			{
				curTime += targetTime;
				break;
			}
			curGain += fFarmGain;
			curTime += nextFarmTime;
		}*/


/*		double d = 2 * fFarmGain * 2 * fFarmGain - 4 * ( 2 * fFarmGain * ( -fFarmPrice * fTarget ) );
		assert( d >= 0 );
		double ds = sqrt( d );
		double x1 = ( 2 * fFarmGain + ds ) / ( 2 * 2 * fFarmGain );
		double x2 = ( 2 * fFarmGain - ds ) / ( 2 * 2 * fFarmGain );
		int n1 = (int)floor( x1 );
		int n2 = (int)floor( x2 );
		int n = ( n1 > n2 ? n1 : n2 );
		double res;
		if ( n > 0 )
		{
			double tn = ( 2.0 * n + fFarmGain * ( n - 1 ) / 2 ) / fFarmPrice;
			double gn = fFarmGain * ( n - 1 );
			res = tn + fTarget / fTarget;
		}
		else
		{
			res = fTarget / 2.0;
		}
*/
		int n = int( fTarget / fFarmPrice - 2.0 / fFarmGain );
		if ( n < 0 ) n = 0;

		double curGain = 2.0;
		double res = 0;
		for( int i = 1; i <= n; i++ )
		{
			res += fFarmPrice / curGain;
			curGain += fFarmGain;
		}
		res += fTarget / curGain;

		fprintf( fout, "Case #%d: %.7f\n", iCase + 1, res );
	}

	fclose( fin );
	fclose( fout );
}
