//============================================================================
// Name        : Google.cpp
// Author      : Anmol Ahuja
//============================================================================

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctype.h>
#include <cstdlib>
#include <climits>
#include <algorithm>
using namespace std;
#define MAX 1001
#define e 0.0000001

inline int deceitfulWar( const double naomi[MAX], const double ken[MAX], const int n )
{
	bool ntemp[MAX];
	memset( ntemp, 0, MAX );
	int score = 0;
	int kupper = n-1, nupper = n-1, klower = 0, nlower = 0;
	for( int i=0; i<n; ++i )
	{
		while( ntemp[nupper] )
			--nupper;
		while( ntemp[nlower] )
			++nlower;
		bool flag = false;
		for( int j=0; j<n; ++j )
		{
			if( !ntemp[j] && naomi[j] - ken[klower] > e )
			{
				flag = true;
				ntemp[j] = true;
				++score;
				++klower;
				break;
			}
		}
		if( !flag )
		{
			ntemp[nlower] = true;
			++nlower;
			--kupper;
		}
	}
	return score;
}

inline int war( const double naomi[MAX], const double ken[MAX], int n )
{
	bool ktemp[MAX];
	memset( ktemp, 0, MAX );
	int score = 0;
	for( int i=0; i<n; ++i )
	{
		bool flag = false;
		for( int j=0; j<n; ++j )
		{
			if( !ktemp[j] && naomi[n-i-1] - ken[j] < e )
			{
				// ++ken's score;
				ktemp[j] = true;
				flag = true;
				break;
			}
		}
		if( !flag )
			++score;
	}
	return score;
}

int main()
{
	int t;
	scanf("%d",&t);
	int n;
	double naomi[MAX], ken[MAX];
	for( int k=1; k<=t; ++k )
	{
		scanf( "%d", &n );
		for( int i=0; i<n; ++i )
			scanf( "%lf", &naomi[i] );
		for( int i=0; i<n; ++i )
			scanf( "%lf", &ken[i] );
		sort( naomi, naomi + n );
		sort( ken, ken + n );

		int y = deceitfulWar( naomi, ken, n );
		printf( "Case #%d: %d %d\n", k, y, war( naomi,ken,n ) );
	}
	return 0;
}
