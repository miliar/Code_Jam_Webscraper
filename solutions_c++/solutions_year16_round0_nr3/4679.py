#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int N, J;

long long get_div( long long number ) {
	long long limit = sqrt( number ); //cout << "Divs> " << number << ", limit: " << limit << '\n';
	for ( int i = 2; i <= limit; ++i ) {
		if ( number % i == 0 && i  ) return i;
	}
	return 0;
}

void check( string &s ) {
	long long number, divs[ 10 ];
	for ( int base = 2; base <= 10; ++base ) {
		number = stoll( s, nullptr, base );
		divs[ base - 2 ] = get_div( number ); //cout << "# " << s << ", " << base << ": " << number << ", div: " << divs[ base - 2 ] << '\n';
		if ( divs[ base - 2 ] == 0LL )
			return;
	}
	cout << s << " ";
	for ( int i = 0; i < 9; ++i ) {
		cout << divs[ i ] << " ";
	}
	cout << '\n';
	--J;
}

void gen_num ( int x, string &s ) { //cout << "@@ " << s << '\n';
	if ( J == 0 ) return;

	if ( x == (N - 1) ) { //cout << "$$ " << s << '\n';
		check( s );
		return;
	}

	gen_num( x + 1, s );

	s[ x ] = '1';
	gen_num( x + 1, s );
	s[ x ] = '0';

	return;
}

int main() {

	int T;
	cin >> T;

	cin >> N >> J;

	string s ( N, '0' );
	s[ 0 ] = s[ N - 1 ] = '1';

	cout << "Case #1:\n";
	gen_num( 1, s );


	return 0;
}