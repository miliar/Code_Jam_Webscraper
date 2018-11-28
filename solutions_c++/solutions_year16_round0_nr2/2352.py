#include <iostream>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

int a[101][2];

void precalc() {
	a[1][0] = 1;
	a[1][1] = 0;
	for( int i = 2; i <= 100; ++i ) {
		for( int j = 0; j < 2; ++j ) {
			a[i][j] = std::min( 1 + a[i-1][1-j], 2 + a[i-1][j] );
		}
	}
}

int main() {
	precalc();

	string s;
	getline( cin, s );
	int cases = stoi( s );

	for( int c = 0; c < cases; ++c ) {
		cout << "Case #" << c+1 << ": ";

		getline( cin, s );
		assert( 1 <= s.size() && s.size() <= 100 );
		for( char x : s ) {
			assert( x == '-' || x == '+' );
		}

		int groups = 1;
		for( size_t i = 1; i < s.size(); ++i ) {
			if( s[i] != s[i-1] ) ++groups;
		}

		cout << a[groups][s[0] == '+'] << endl;
	}

	return 0;
}
