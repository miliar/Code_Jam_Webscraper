
#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

bool is_up_down( const vector< int >& a )
{
	bool up = true;
	for ( int i = 1; i < (int)a.size(); ++i ) {
		if ( up ) {
			if ( a[ i - 1 ] < a[ i ] ) {
			}
			else {
				up = false;
			}
		}
		else {
			if ( a[ i - 1 ] > a[ i ] ) {
			}
			else
				return false;
		}
	}
	return true;
}

int swaps_count( vector< int > a, vector< int > b )
{
	assert( a.size() == b.size() );
	int r = 0;
	for ( int i = 0; i < (int)a.size(); ++i ) {
		int bp = -1;
		for ( int j = i; j < (int)b.size(); ++j ) {
			if ( b[ j ] == a[ i ] ) {
				bp = j;
				break;
			}
		}
		assert( bp != -1 );
		while ( i != bp ) {
			swap( b[ bp ], b[ bp - 1 ] );
			--bp;
			++r;
		}
	}
	assert( a == b );
	return r;
}

int solve1( int n, const vector< int >& a )
{
	int min_cnt = (int)a.size() * (int)a.size() + 10;
	int cnt;
	vector< int > b( a );
	sort( b.begin(), b.end() );
	do {
		if ( is_up_down( b ) ) {
			cnt = swaps_count( a, b );
			min_cnt = min( min_cnt, cnt );
		}
	} while ( next_permutation( b.begin(), b.end() ) );
	return min_cnt;
}

int solve2( int n, vector< int > a )
{
	vector< int >::iterator it1, it2, it_min;
	it1 = a.begin();
	it2 = a.end();
	int r = 0;
	while ( it1 < it2 ) {
		it_min = min_element( it1, it2 );
		int to_left = it_min - it1;
		int to_right = it2 - it_min - 1;
		if ( to_left <= to_right ) {
			r += to_left;
			while ( it_min > it1 ) {
				swap( *it_min, *(it_min-1) );
				--it_min;
			}
			++it1;
		}
		else {
			r += to_right;
			while ( it_min < it2 - 1 ) {
				swap( *it_min, *(it_min+1) );
				++it_min;
			}
			--it2;
		}
	}
	return r;
}

int main()
{
	int T;
	cin >> T;
	for ( int t = 1; t <= T; ++t ) {
		int n;
		cin >> n;
		vector< int > a;
		a.resize( n );
		for ( int i = 0; i < n; ++i )
			cin >> a[ i ];
		cout << "Case #" << t << ": " << solve2( n, a ) << endl;
	}
	return 0;
}
