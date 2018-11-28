
#include <iostream>

#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>


using namespace std;

long long divisor( long long v )
{
	const long long l = sqrt( v ) +1;
	for( long long i=2; i<l; ++i )
	{
		if ( v%i == 0 )
		{
			return i;
		}
	}
	return 0;
}

int main( int, const char*[] )
{

	int test_num;
	cin >> test_num;

	for( int test=0; test<test_num; ++test )
	{
		int n, j;
		cin >> n >> j;

		vector<long long> ac;

		int s[32];
		int iter = 0;
		for( int i=0; i<=n-2; ++i )
		{
			for( int z=0; z<=i; ++z )
			{
				s[z+1] = 0;
			}
			for( int z=i; z<n-2; ++z )
			{
				s[z+1] = 1;
			}
			s[0] = s[n-1] = 1;
			do
			{
				bool accepted = true;
				long long bv[11];
				for( int b=2; b<=10; ++b )
				{
					long long v = 0;
					long long m = 1;
					for( int di=0; di<n; ++di )
					{
						v += m * s[di];
						m *= b;
					}
					bv[b] = v;
					if ( divisor( v ) == 0 )
					{
						accepted = false;
						break;
					}
				}
				if ( accepted )
				{
					ac.push_back( bv[2] );
					if ( ac.size() >= j )
					{
						break;
					}
				}
				++iter;
			} while( next_permutation( s+1, s+n-1 ) );

			if ( ac.size() >= j )
			{
				break;
			}
		}
		//cout << iter << endl;

		cout << "Case #" << (test+1) << ": " << endl;
		for( const auto it : ac )
		{
			char mem[33] = { '\0' };
			for( int i=0; i<n; ++i )
			{
				mem[n-i-1] = '0' + ( it & (1<<i) ? 1 : 0 );
			}
			cout << mem << " ";
			for( int b=2; b<=10; ++b )
			{
				long long v = 0;
				long long m = 1;
				for( int di=0; di<n; ++di )
				{
					v += m * ( it & (1<<di) ? 1 : 0 );
					m *= b;
				}
				cout << divisor(v) << " ";
			}
			cout << endl;
		}
		cout << endl;
	}

	return 0;
}

