#include <iostream>

using namespace std;

void solve ( void )
{
	const int COMPLETE = 0x3ff;
	int cnt = 0, seen = 0;
	long long n, sum = 0;

	cin >> n;

	if ( n == 0 ) {
		cout << "INSOMNIA";
		return;
	}

	sum = n;
	while ( 1 ) {
		long long tmp = sum;
		do {
			seen |= 1 << ( tmp % 10 );
		} while ( tmp /= 10 );

		if ( seen == COMPLETE ) {
			break;
		}
		sum += n;
	}

	cout << sum;
}

int main ( void )
{
	// cin.tie( 0 );
	// ios::sync_with_stdio( false );
	int T;

	cin >> T;

	for ( int t = 1; t <= T; ++t ) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
