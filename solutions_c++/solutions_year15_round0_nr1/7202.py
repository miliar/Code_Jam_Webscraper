#include <stdio.h>
#include <iostream>

using namespace std;

int main() {

	freopen( "x.txt", "r", stdin );
	freopen( "y.txt", "w", stdout );

	int T;
	cin >> T;

	for( int t = 1; t <= T; ++t ) {

		int S, cnt[2000];
		char shy[2000];

		cin >> S >> shy;

		for( int i = 0; shy[i]; ++i ) {
			cnt[ i ] = shy[i] - '0';
		}

		int ans = 0;

		for( int i = 0; shy[i]; ++i ) {
			if( i == 0 ) {
				if( !cnt[i] ) {
					ans++;
					cnt[i]++;
				}
				cnt[i+1] += cnt[i];
			}
			else {
				if( cnt[i] < ( i + 1 ) ) {
					ans++;
					cnt[i]++;
				}
				cnt[i+1] += cnt[i];
			}
		}

		cout << "Case #" << t <<": " << ans << endl;

	}

	return 0;
}