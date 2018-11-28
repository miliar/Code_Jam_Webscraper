#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define fo( Case, x, y ) for ( int Case=x; Case<y; ++Case )

ifstream in( "p1.in" );
ofstream out( "p1.out" );

string S;
int n;

int main()
{
	ios :: sync_with_stdio( 0 );
	int T; in >> T;
	fo ( Case, 0, T )
	{
		in >> n;
		in >> S;
		int PreSum = 0, Res = 0;
		int Len = S.length();
		fo ( i, 0, Len )
		{
			while ( PreSum<i ) ++Res, ++PreSum;
			PreSum += S[i] - '0';
		}
		out << "Case #" << ( Case+1 ) << ": " << Res << endl;
	}
	in.close(); out.close();
	return 0;
}

