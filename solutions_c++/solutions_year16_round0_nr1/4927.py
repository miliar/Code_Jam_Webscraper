#include <bits/stdc++.h>
#define D(x) cout << ">> " << #x << " = >" << x << "<" << endl
#define FOR(i,a,b) for ( int i = int(a); i < int(b); ++i )
using namespace std;
typedef long long ll;

int main( ) {
	/*FOR( i, 1, 1e6+1 ) {
		bool digits[10] = { };
		int cnt = 0;
		int n = i;
		while ( 1 ) {
			for ( int tmp = n; tmp; tmp /= 10 ) {
				if ( !digits[tmp % 10] ) {
					digits[tmp % 10] = 1;
					++cnt;
				}
			}
			if ( cnt == 10 ) {
			//	cout << n << endl;
				break;
			}
			//D( i );
			assert( (ll) n + i <= INT_MAX );
			n += i;
		}
	}/*/
	int t, n;
	cin >> t;
	FOR( caseNr, 1, t+1 ) {
		cin >> n;
		cout << "Case #" << caseNr << ": ";
		if ( !n ) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		bool digits[10] = { };
		int cnt = 0;
		int  k  = n;
		while ( 1 ) {
			for ( int tmp = k; tmp; tmp /= 10 ) {
				if ( !digits[tmp % 10] ) {
					digits[tmp % 10] = 1;
					++cnt;
				}
			}
			if ( cnt == 10 ) {
				cout << k << endl;
				break;
			}
			k += n;
		}
	}//*/
	return 0;
}