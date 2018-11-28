
#include <vector>
#include <list>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

int solve( int n, int x, list< int >& s )
{
	int r = 0;
	list< int >::iterator it1, it2;
	it1 = s.begin();
	it2 = s.end();
	while ( it1 != it2 ) {
		--it2;
		if ( it1 == it2 ) {
			++r;
		}
		else {
			if ( *it1 + *it2 <= x ) {
				++it1;
				++r;
			}
			else {
				++r;
			}
		}
	}
	return r;
}

int main()
{
	int T;
	cin >> T;
	for ( int t = 1; t <= T; ++t ) {
		vector< int > sv;
		int n, x;
		cin >> n >> x;
		sv.resize( n );
		for ( int i = 0; i < n; ++i )
			cin >> sv[ i ];
		sort( sv.begin(), sv.end() );
		list< int > s;
		copy( sv.begin(), sv.end(), back_inserter( s ) );
		cout << "Case #" << t << ": " << solve( n, x, s ) << endl;
	}
	return 0;
}
