#include <bits/stdc++.h>
using namespace std;

typedef long double lf;
typedef long long ll;

const int TAM = 1000100;

int a[TAM], n;
ll aa[TAM];
ll dp2[TAM];
ll dp3[TAM];

lf solve ( )
{
	cin >> n; {
		ll p, q, r, s;
		cin >> p >> q >> r >> s;
		for ( int i = 0; i < n; ++i )
			a[i] = int ( (ll(i)*p+q)%r+s );
	}

	aa[0] = a[0];
	for ( int i = 1; i < n; ++i )
		aa[i] = aa[i-1]+a[i];

	if ( n <= 3 ) {
		if ( n == 1 ) return 0;
		if ( n == 2 ) return lf(1)-lf(max(a[0],a[1]))/lf(a[0]+a[1]);
		return lf(1)-lf(max(a[0],max(a[1],a[2]))) / lf(a[0]+a[1]+a[2]);
	}

	//fill dp2
	{
		int i = 0;
		for ( int j = 1; j < n; ++j ) {
			dp2[j] = max ( aa[i], aa[j]-aa[i] );
			while ( i < j && max ( aa[i+1], aa[j]-aa[i+1] ) < dp2[j] ) {
				dp2[j] = max ( aa[i+1], aa[j]-aa[i+1] );
				i++;
			}
		}
	}	

	//fill dp3
	{
		int i = 1;
		for ( int j = 2; j < n; ++j ) {
			dp3[j] = max ( dp2[i], aa[j]-aa[i] );
			while ( i < j && max ( dp2[i+1], aa[j]-aa[i+1] ) < dp3[j] ) {
				dp3[j] = max ( dp2[i+1], aa[j]-aa[i+1] );
				i++;
			}
		}
	}
	return lf(1) - lf(dp3[n-1]) / lf(aa[n-1]);
}

int main ( )
{
	fixed(cout);
	cout.precision(12);

	int nTests; cin >> nTests;
	for ( int i = 1; i <= nTests; ++i ) {
		lf ans = solve();
		cout << "Case #" << i << ": " << ans << "\n";
	}

	return 0;
}
