#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void simplify ( ll& num, ll& den, const ll x ) {
	if ( x == ll(1) ) return;
	while ( num%x == 0 && den%x == 0 ) {
		num/=x; den/=x;
	}
}

bool calc ( ll a, ll b, ll den, ll& ans )
{
/*	if ( a*b % den == 0 ) {
		ans = a*b / den;
		return true;
	} return false; */

	for ( ll i = 2, j; i*i <= den; ++i ) {
		if ( den%i == ll(0) ) {
			j = den/i;
			simplify ( a, den, i );
			simplify ( a, den, j );
			simplify ( b, den, i );
			simplify ( b, den, j );
		}
	}

	simplify ( a, den, den );
	simplify ( b, den, den );

	if ( den != 1 )
		return false;

	ans = a*b;
	return true;
}

int main ( )
{
	int nCases;
	cin >> nCases;

	for ( int curCase = 1; curCase <= nCases; ++curCase )
	{
		string line;
		cin >> line;
		for ( int i = 0; i < (int)line.size(); ++i )
			if ( line[i] == '/' )
				line[i] = ' ';
		stringstream ss ( line );

		ll num, den;
		ss >> num >> den;

		const ll den2 = (ll(1) << ll(40));
		ll x, y;
		int ans = -1;
		for ( int p = 1; p < 40; ++p )
		{
			y = ( ll(1) << ll(40-p) );
			// num/den = (x+y)/den2
			// x = (num*den2)/den
			// x = (num*den2)/den - y must be >= 0

			if ( !calc ( num, den2, den, x ) ) continue;
			if ( x < y ) continue;

			ans = p;
			break;
		}

		cout << "Case #" << curCase << ": ";
		if ( ans == -1 ) cout << "impossible";
		else cout << ans;
		cout << endl;
	}
	
	return 0;
}
