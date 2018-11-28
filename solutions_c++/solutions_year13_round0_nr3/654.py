#include <assert.h>
#include <time.h>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

clock_t startTime;
void startTimer ( ) { startTime = clock(); }
void printTime ( ) { printf ( "Time = %.5lf\n", (clock()-startTime)/(double)CLOCKS_PER_SEC ); }

typedef long long ll;
const ll MAX_SQRT = 100000000; // sqrt(MAX_N)


bool isPal ( ll x ) {
	ll y = 0;
	for ( ll i = x; i > 0; i /= 10 )
		y = 10*y + i%10;
	return ( x == y );
}

vector<ll> v;
inline void ftry ( ll i ) {
	if ( isPal ( i ) )
		if ( isPal ( i*i ) )
			v.push_back ( i*i );
}

int main ( )
{
	//freopen ( "C.in", "r", stdin );
	//freopen ( "C.out", "w", stdout );

	startTimer();

	for ( ll i = 1; i <= MAX_SQRT; ++i )
		ftry(i);

	int nCases;
	scanf ( "%d", &nCases );
	for ( int curCase = 1; curCase <= nCases; ++curCase )
	{
		ll a=-1, b=-1;
		cin >> a >> b;
		for ( int i = 0; i < (int)v.size(); ++i )
			if ( v[i] >= a )
				{ a = i; break; }
		
		for ( int i = v.size()-1; i >= 0; --i )
			if ( v[i] <= b )
				{ b = i; break; }
		
		assert ( b != -1 && a != -1 );
		printf ( "Case #%d: ", curCase );
		cout << (b-a+1LL) << endl;
	}

	//printTime();
	return 0;
}

