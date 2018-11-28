
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct square
{
public:
	square() {}

	square( int h_, int r_, int c_ )
		: h( h_ ), r( r_ ), c( c_ ) {}

	int h;
	int r, c;
};

bool operator==( const square& s1, const square& s2 )
{
	return s1.h == s2.h;
}

bool operator<( const square& s1, const square& s2 )
{
	return s1.h < s2.h;
}

bool solve( int n, int m, int a[ 100 ][ 100 ] )
{
	vector< square > sv;
	for ( int r = 0; r < n; ++r )
		for ( int c = 0; c < m; ++c )
			sv.push_back( square( a[ r ][ c ], r, c ) );
	sort( sv.begin(), sv.end() );
	for ( int i = 0; i < (int)sv.size(); ++i ) {
		bool can_by_row = true;
		for ( int c = 0; c < m; ++c )
			if ( a[ sv[ i ].r ][ c ] > sv[ i ].h )
				can_by_row = false;
		bool can_by_col = true;
		for ( int r = 0; r < n; ++r )
			if ( a[ r ][ sv[ i ].c ] > sv[ i ].h )
				can_by_col = false;
		if ( ! can_by_row && ! can_by_col )
			return false;
	}
	return true;
}

int main()
{
	int a[ 100 ][ 100 ];
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int n, m;
		cin >> n >> m;
		for ( int r = 0; r < n; ++r )
			for ( int c = 0; c < m; ++c )
				cin >> a[ r ][ c ];
		cout << "Case #" << tc << ": " << ( solve( n, m, a ) ? "YES" : "NO" ) << endl;
	}
	return 0;
}
