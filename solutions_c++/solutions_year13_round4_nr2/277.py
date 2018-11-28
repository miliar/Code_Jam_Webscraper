#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int t;
	cin >> t;
	for( int tt = 1; tt <= t; tt++ ) {
		
		long long ans1, ans2;

		long long n, p;
		cin >> n >> p;

		int pp = p;
		
		long long nn = 1;
		for( int i = 0; i < n; i++ ) {
			nn *= 2;
		}
		
		if( p >= nn ) {
			printf( "Case #%d: ", tt );
			cout << nn - 1 << " " << nn - 1 << endl;
			continue;
		}
		
		int count = 1;
		long long nnn = nn;
		while( p < nnn / 2 ) {
			count++;
			nnn /= 2;
		}

		ans2 = 1;
		for( int i = 0; i < count; i++ ) {
			ans2 *= 2;
		}
		ans2 = nn - ans2;

		
		
		count = 1;
		nnn = nn;
		while( p > nnn / 2 ) {
			count++;
			p -= nnn / 2;
			nnn /= 2;
		}
		ans1 = 1;
		for( int i = 0; i < count; i++ ) {
			ans1 *= 2;
		}
		ans1 -= 2;
		
		
		printf( "Case #%d: ", tt );
			
		cout << ans1 << " " << ans2;
	
		cout << endl;
	}
	return 0;
}

