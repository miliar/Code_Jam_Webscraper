#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1005;

ifstream in( "p2.in" );
ofstream out( "p2.out" );

#define fo( i, x, y ) for ( int i=x; i<y; ++i )

int n, Res;
int a[N];

int main()
{
	ios :: sync_with_stdio( 0 );
	int T; in >> T;
	fo ( Case, 0, T )
	{
		Res = 0x7FFFFFFF;
		in >> n;
		fo ( i, 0, n ) in >> a[i];
		fo ( ti, 1, 1005 )
		{
			int Sum = ti;
			fo ( i, 0, n ) Sum += ( a[i] - 1 ) / ti;
			Res = min( Res, Sum );
 		}
		out << "Case #" << ( Case+1 ) << ": " << Res << endl;
	}
	in.close(), out.close();
	return 0;
}

