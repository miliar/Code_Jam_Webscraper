
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

void main()
{
	ifstream in;
	in.open( "B-small-attempt0.in", ios_base::in );
	int test;
	in>>test;
	ull *ans = new ull [ test ];
	for( int i = 0; i < test; ++i )
	{
		ull a, b, k;
		in>>a>>b>>k;
		ans[ i ] = 0;
		for( ull j = 0; j < a; ++j )
		{
			for( ull jj = 0; jj < b; ++jj )
			{
				if( ( j & jj ) < k )
					++ans[ i ];
			}
		}
	}
	in.close();
	ofstream out;
	out.open( "a.txt", ios_base::app );
	for( int i = 0; i < test; ++i )
		out<<"Case #"<<i + 1<<": "<<ans[ i ]<<endl;
	out.close();
}



