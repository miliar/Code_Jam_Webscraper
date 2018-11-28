/**
 * Tittle:	
 * Author:	Cheng-Shih, Wong
 * Date:	
 */

// include files
#include <bits/stdc++.h>

using namespace std;

// definitions
#define FOR(i,a,b) for( int i=(a),_n=(b); i<=_n; ++i )
#define clr(x,v) memset( x, v, sizeof(x) )
#define F first
#define S second
#define PB push_back

// declarations
int t;
string s;
int cnt[30];
string digit[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
string digitN[10] = { "ZERO", "ONE", "TWO", "THRE", "FOUR", "FIVE", "SIX", "SEVN", "EIGHT", "INE" };
int dig[10][30] = {};
vector<int> seq;
string out;

// functions

// main function
int main( void )
{
	FOR( i, 0, 9 ) {
		for( char c:digit[i] )
			++dig[i][c-'A'];
	}
	seq.PB(8);
	seq.PB(0);
	seq.PB(6);
	seq.PB(2);
	seq.PB(3);
	seq.PB(4);
	seq.PB(7);
	seq.PB(1);
	seq.PB(5);
	seq.PB(9);

	scanf( "%d", &t );
	bool valid;

	FOR( ti, 1, t ) {
		clr( cnt, 0 );
		cin >> s;

		for( char c:s ) {
			++cnt[c-'A'];
		}

		printf( "Case #%d: ", ti );
		out = "";

		for( int i:seq ) {
			int minv = 2000;

			for( char c:digitN[i] )
				minv = min( minv, cnt[c-'A']/dig[i][c-'A'] );

			for( char c:digitN[i] )
				cnt[c-'A'] -= minv*dig[i][c-'A'];

			FOR( j, 1, minv ) out += (char)(i+'0');
		}
		sort( out.begin(), out.end() );
		cout << out << endl;
	}
	
	return 0;
}
