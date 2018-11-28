#include <algorithm>
#include <functional>
#include <utility>
#include <memory>
#include <numeric>
#include <iterator>

#include <string>
#include <bitset>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>

#include <stdexcept>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>

#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <ctime>
#include <cmath>

using namespace std;

#define N 4
char data[N][N];

string solve()
{
	for( int i=0; i<N; ++i )
	{
		if(data[i][0]=='X' && data[i][1]=='X' && data[i][2]=='X' && data[i][3]=='X')
			return string( "X won" );
		if(data[i][0]=='T' && data[i][1]=='X' && data[i][2]=='X' && data[i][3]=='X')
			return string( "X won" );
		if(data[i][0]=='X' && data[i][1]=='T' && data[i][2]=='X' && data[i][3]=='X')
			return string( "X won" );
		if(data[i][0]=='X' && data[i][1]=='X' && data[i][2]=='T' && data[i][3]=='X')
			return string( "X won" );
		if(data[i][0]=='X' && data[i][1]=='X' && data[i][2]=='X' && data[i][3]=='T')
			return string( "X won" );
	}
	for( int j=0; j<N; ++j )
	{
		if(data[0][j]=='X' && data[1][j]=='X' && data[2][j]=='X' && data[3][j]=='X')
			return string( "X won" );
		if(data[0][j]=='T' && data[1][j]=='X' && data[2][j]=='X' && data[3][j]=='X')
			return string( "X won" );
		if(data[0][j]=='X' && data[1][j]=='T' && data[2][j]=='X' && data[3][j]=='X')
			return string( "X won" );
		if(data[0][j]=='X' && data[1][j]=='X' && data[2][j]=='T' && data[3][j]=='X')
			return string( "X won" );
		if(data[0][j]=='X' && data[1][j]=='X' && data[2][j]=='X' && data[3][j]=='T')
			return string( "X won" );
	}

	if(data[0][0]=='X' && data[1][1]=='X' && data[2][2]=='X' && data[3][3]=='X')
		return string( "X won" );
	if(data[0][0]=='T' && data[1][1]=='X' && data[2][2]=='X' && data[3][3]=='X')
		return string( "X won" );
	if(data[0][0]=='X' && data[1][1]=='T' && data[2][2]=='X' && data[3][3]=='X')
		return string( "X won" );
	if(data[0][0]=='X' && data[1][1]=='X' && data[2][2]=='T' && data[3][3]=='X')
		return string( "X won" );
	if(data[0][0]=='X' && data[1][1]=='X' && data[2][2]=='X' && data[3][3]=='T')
		return string( "X won" );

	if(data[0][3]=='X' && data[1][2]=='X' && data[2][1]=='X' && data[3][0]=='X')
		return string( "X won" );
	if(data[0][3]=='T' && data[1][2]=='X' && data[2][1]=='X' && data[3][0]=='X')
		return string( "X won" );
	if(data[0][3]=='X' && data[1][2]=='T' && data[2][1]=='X' && data[3][0]=='X')
		return string( "X won" );
	if(data[0][3]=='X' && data[1][2]=='X' && data[2][1]=='T' && data[3][0]=='X')
		return string( "X won" );
	if(data[0][3]=='X' && data[1][2]=='X' && data[2][1]=='X' && data[3][0]=='T')
		return string( "X won" );

	///
	for( int i=0; i<N; ++i )
	{
		if(data[i][0]=='O' && data[i][1]=='O' && data[i][2]=='O' && data[i][3]=='O')
			return string( "O won" );
		if(data[i][0]=='T' && data[i][1]=='O' && data[i][2]=='O' && data[i][3]=='O')
			return string( "O won" );
		if(data[i][0]=='O' && data[i][1]=='T' && data[i][2]=='O' && data[i][3]=='O')
			return string( "O won" );
		if(data[i][0]=='O' && data[i][1]=='O' && data[i][2]=='T' && data[i][3]=='O')
			return string( "O won" );
		if(data[i][0]=='O' && data[i][1]=='O' && data[i][2]=='O' && data[i][3]=='T')
			return string( "O won" );
	}
	for( int j=0; j<N; ++j )
	{
		if(data[0][j]=='O' && data[1][j]=='O' && data[2][j]=='O' && data[3][j]=='O')
			return string( "O won" );
		if(data[0][j]=='T' && data[1][j]=='O' && data[2][j]=='O' && data[3][j]=='O')
			return string( "O won" );
		if(data[0][j]=='O' && data[1][j]=='T' && data[2][j]=='O' && data[3][j]=='O')
			return string( "O won" );
		if(data[0][j]=='O' && data[1][j]=='O' && data[2][j]=='T' && data[3][j]=='O')
			return string( "O won" );
		if(data[0][j]=='O' && data[1][j]=='O' && data[2][j]=='O' && data[3][j]=='T')
			return string( "O won" );
	}

	if(data[0][0]=='O' && data[1][1]=='O' && data[2][2]=='O' && data[3][3]=='O')
		return string( "O won" );
	if(data[0][0]=='T' && data[1][1]=='O' && data[2][2]=='O' && data[3][3]=='O')
		return string( "O won" );
	if(data[0][0]=='O' && data[1][1]=='T' && data[2][2]=='O' && data[3][3]=='O')
		return string( "O won" );
	if(data[0][0]=='O' && data[1][1]=='O' && data[2][2]=='T' && data[3][3]=='O')
		return string( "O won" );
	if(data[0][0]=='O' && data[1][1]=='O' && data[2][2]=='O' && data[3][3]=='T')
		return string( "O won" );

	if(data[0][3]=='O' && data[1][2]=='O' && data[2][1]=='O' && data[3][0]=='O')
		return string( "O won" );
	if(data[0][3]=='T' && data[1][2]=='O' && data[2][1]=='O' && data[3][0]=='O')
		return string( "O won" );
	if(data[0][3]=='O' && data[1][2]=='T' && data[2][1]=='O' && data[3][0]=='O')
		return string( "O won" );
	if(data[0][3]=='O' && data[1][2]=='O' && data[2][1]=='T' && data[3][0]=='O')
		return string( "O won" );
	if(data[0][3]=='O' && data[1][2]=='O' && data[2][1]=='O' && data[3][0]=='T')
		return string( "O won" );

	/////////////////////////////
	for( int i=0; i<N; ++i )
		for( int j=0; j<N; ++j )
		{
			if( data[i][j]=='.' ) return string( "Game has not completed" );
		}
	
	return string( "Draw" );

}
int main()
{
	int T;
	cin>>T;
	for( int t=1; t<=T; ++t )
	{
		for( int i=0; i<N; ++i )
			for( int j=0; j<N; ++j )
				cin>>data[i][j];

		cout<<"Case #"<<t<<": ";
		cout<<solve();
		cout<<endl;
	}

	return 0;
}

