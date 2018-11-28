#include <iostream>
#include <fstream>
#include <cmath>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define forn(i, n) for ( int i = 0; i < n; i++ )
#define MK(x,y) make_pair( x, y )
#define sqr(x) ( (x) * (x) )

fstream fin( "in.txt" );
fstream fout( "out.txt" );

void solve()
{
	string str;
	fin >> str;
	deque<char> que;
	forn ( i, str.length() )
	{
		if ( i == 0 ) que.push_back( str[i] );
		else
		{
			if ( str[i] >= que.front() ) que.push_front( str[i] );
			else que.push_back( str[i] ); 
		}
	}
	for( deque<char>::iterator it = que.begin();
			it != que.end(); ++it )
	{
		fout << *it;
	}
	fout << endl;
}

int main()
{
	
	int T;
	fin >> T;
	forn( t, T )
	{
		fout << "Case #" << t + 1 << ": ";
		solve();
	}

	return 0;
}