
#include <iostream>
#include <vector>

using namespace std;

long long get_reverse_number( long long n )
{
	long long r = 0;
	while ( n > 0 ) {
		r *= 10;
		r += n % 10;
		n /= 10;
	}
	return r;
}

bool is_palindrome( long long n )
{
	return get_reverse_number( n ) == n;
}

void calc_solve( vector< bool >& solve )
{
	const int MAXN = 10000000 + 500;
	solve.clear();
	solve.resize( MAXN + 1 );
	for ( int i = 1; i <= MAXN; ++i )
		solve[ i ] = is_palindrome( i ) && is_palindrome( i * i );
}

void calc_solve_count( const vector< bool >& solve, vector< int >& solve_count )
{
	solve_count.clear();
	solve_count.resize( solve.size() );
	solve_count[ 0 ] = 0;
	for ( int i = 1; i < (int)solve.size(); ++i )
		solve_count[ i ] = solve_count[ i - 1 ] + ( solve[ i ] ? 1 : 0 );
}

long long sqrt( long long n )
{
	long long d = 1;
	long long u;
	for ( u = 10; u*u <= n; u *= 10 )
		;
	if ( d*d == n )
		return d;
	if ( u*u == n )
		return u;
	while ( u - d >= 2 ) {
		long long m = d + (u - d) / 2;
		if ( m*m == n )
			return m;
		else if ( m*m < n )
			d = m;
		else
			u = m;
	}
	return d;
}

int main()
{
	vector< bool > solve;
	calc_solve( solve );
	vector< int > solve_count;
	calc_solve_count( solve, solve_count );
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		long long A, B;
		cin >> A >> B;
		int a, b;
		a = sqrt( A );
		if ( a*a != A )
			++a;
		b = sqrt( B );
		//cout << "--- " << a << " - " << b << endl;
		cout << "Case #" << tc << ": " << (solve_count[ b ] - solve_count[ a - 1 ]) << endl;
	}
	return 0;
}
