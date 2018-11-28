
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
	in.open( "B-large.in", ios_base::app );
	int t;
	in>>t;
	for( int i = 1; i <= t; ++i )
	{
		long double c, f, x, ans = 0, sp = 2;
		in>>c>>f>>x;
		while( 1 )
		{
			long double spF = c / sp + x / ( sp + f );
			if( ( x / sp ) > spF )
			{
				ans += ( c / sp );
				sp += f;
			}
			else
			{
				ans += ( x / sp );
				break;
			}
		}
		ofstream out;
		out.open( "ans.txt", ios_base::app );
		char a[ 100000 ];
		sprintf( a, "Case #%d: %lf\n", i, ans );
		out<<a;
	}
	in.close();
}
			
