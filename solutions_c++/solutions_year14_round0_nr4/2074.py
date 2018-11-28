
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
#include <list>
#include <cmath>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int dUSort( const void *a, const void *b )
{
	if( *( double * )a < *( double * )b )
		return -1;
	if( *( double * )a == *( double * )b )
		return 0;
	if( *( double * )a > *( double * )b )
		return 1;
}

int uDSort( const void *a, const void *b )
{
	if( *( double * )a > *( double * )b )
		return -1;
	if( *( double * )a == *( double * )b )
		return 0;
	if( *( double * )a < *( double * )b )
		return 1;
}

void main()
{
	ifstream in;
	in.open( "D-large.in", ios_base::app );
	int t;
	in>>t;
	for( int i = 1; i <= t; ++i )
	{
		int n, ans = 0, dAns = 0;
		in>>n;
		double *nao = new double[ n ];
		double *ken = new double [ n ];
		double *dNao = new double [ n ];
		double *dKen = new double [ n ];
		for( int i = 0; i < n; ++i )
		{
			in>>nao[ i ];
			dNao[ i ] = nao[ i ];
		}
		for( int i = 0; i < n; ++i )
		{
			in>>ken[ i ];
			dKen[ i ] = ken[ i ];
		}
		qsort( nao, n, sizeof( double ), dUSort );
		qsort( ken, n, sizeof( double ), dUSort );
		qsort( dNao, n, sizeof( double ), dUSort );
		qsort( dKen, n, sizeof( double ), uDSort );
		for( int j = 0; j < n; ++j )
		{
			bool ok = 0;
			for( int k = 0; k < n; ++k )
			{
				if( ken[ k ] > nao[ j ] )
				{
					ken[ k ] = 0;
					ok = 1;
					break;
				}
			}
			if( !ok )
				++ans;
			nao[ j ] = 0;
		}
		for( int j = 0; j < n; ++j )
		{
			bool ok = 0;
			for( int k = 0; k < n; ++k )
			{
				if( dNao[ j ] > dKen[ k ] && dKen[ k ] )
				{
					ok = 1;
					for( int l = n - 1; l >= 0; --l )
						if( dKen[ k ] )
						{
							dKen[ k ] = 0;
							break;
						}
					break;
				}
			}
			if( ok )
				++dAns;
			else
				for( int k = 0; k < n; ++k )
					if( dKen[ k ] )
					{
						dKen[ k ] = 0;
						break;
					}
		}
		ofstream out;
		out.open( "ans.txt", ios_base::app );
		out<<"Case #"<<i<<": "<<dAns<<' '<<ans<<endl;
	}
	in.close();
}
			
