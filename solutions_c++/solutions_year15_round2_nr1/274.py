#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

ifstream fin( "A2.in" );
ofstream fout( "A2.out" );
#define cin fin
#define cout fout


string toS( long long num ){
	ostringstream fout;
	fout << num;
	return fout.str();
}

long long dist( long long ten, long long num ){
	if( num == ten )
		return 0;
	if( num % 10 == 0 ){
		return min( num - ten, dist( ten, num - 1 ) + 1 );
	}
	long long ret = num - ten;
	
	long long c1 = 0;
	string ss = toS( num );
	ss = ss.substr( 0, ss.length() / 2 );
	reverse( ss.begin(), ss.end() );
	istringstream sin( ss );
	long long cnt;
	sin >> cnt;

	//cout << cnt << endl;

	c1 += ( cnt + 1 );
	
	ten += cnt;
	string SS = toS( ten );

	long long nm = 0, tmp = 1;
	for( int i = 0; i < SS.length(); i++ ){
		nm += ( SS[i] - '0' ) * tmp;
		tmp *= 10LL;
	}

	//cout << nm << endl;

	c1 += ( num - nm );
	ret = min( ret, c1 );

	return ret;
}

long long solve( long long num ){
	if( num < 10 )
		return num;
	long long m = 1;
	while( m <= num )
		m *= 10;
	m /= 10;
	//cout << num << ' ' << m << endl;
	return dist( m, num ) + 1 + solve( m - 1 );
}



int main()
{
	//cout << dist( 10, 19 ) << endl;
	//freopen("A.in","in",stdin);
	//freopen( "A.out", "out", stdout );

	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		long long n;
		cin >> n;
		cout << "Case #" << T << ": " << solve( n ) << endl;
	}

	return 0;
}