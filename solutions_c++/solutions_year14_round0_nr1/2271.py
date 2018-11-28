
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
	in.open( "A-small-attempt0.in", ios_base::app );
	int t;
	in>>t;
	for( int i = 1; i <= t; ++i )
	{
		int ans1, ans2;
		in>>ans1;
		vector< int > s1( 4 ), s2( 4 );
		int temp;
		for( int j = 1; j < 5; ++j )
		{
			if( j == ans1 )
			{
				for( int k = 0; k < 4; ++k )
					in>>s1[ k ];
			}
			else
				in>>temp>>temp>>temp>>temp;
		}
		in>>ans2;
		for( int j = 1; j < 5; ++j )
		{
			if( j == ans2 )
			{
				for( int k = 0; k < 4; ++k )
					in>>s2[ k ];
			}
			else
				in>>temp>>temp>>temp>>temp;
		}
		
		ofstream out;
		out.open( "ans.txt", ios_base::app );
		vector< int > ans;
		for( int j = 0; j < s1.size(); ++j )
		{
			for( int k = 0; k < s2.size(); ++k )
				if( s1[ j ] == s2[ k ] )
					ans.push_back( s2[ k ] );
		}
		if( !ans.size() )
			out<<"Case #"<<i<<": Volunteer cheated!\n";
		if( ans.size() > 1 )
			out<<"Case #"<<i<<": Bad magician!\n";
		if( ans.size() == 1 )
			out<<"Case #"<<i<<": "<<ans[ 0 ]<<endl;
	}
	in.close();
}
			
