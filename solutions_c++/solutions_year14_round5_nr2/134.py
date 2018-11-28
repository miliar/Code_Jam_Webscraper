#include <bits/stdc++.h>
using namespace std;

const int TAM = 102;
const int MAX_HEALTH = 201;
const int MAX_TURNS = 21*TAM;

int dp[TAM][MAX_HEALTH][MAX_TURNS];
int health[TAM], gold[TAM], n;
int powerTower, powerDiana;

int go ( int i, int h, int x )
{
	int& r = dp[i][h][x];
	if ( r != -1 ) return r;
	if ( i == n ) return r=0;
	if ( h == 0 ) return r=go(i+1,health[i+1],x);

	r = 0;

	//diana skips turn
	if ( powerTower >= h ) r = max ( r, go(i+1,health[i+1],x+1) );
	else r = max ( r, go(i,h-powerTower,x+1) );

	//shoot this monster
	if ( powerDiana >= h ) r = max ( r, go(i+1,max(0,health[i+1]-powerTower),x)+gold[i] );
	else if ( powerTower >= h-powerDiana ) r = max (r, go(i+1,health[i+1],x) );
	else r = max ( r, go(i+1,h-powerDiana-powerTower,x) );

	//shoot this monster with one of skipped turns
	if ( powerDiana >= h && x ) r = max ( r, go(i+1, health[i+1], x-1 ) + gold[i] );
	else if ( x ) r = max ( r, go(i, h-powerDiana, x-1 ) );

	return r;
}

int solve ( ) {
	cin >> powerDiana >> powerTower >> n;
	for ( int i = 0; i < n; ++i )
		cin >> health[i] >> gold[i];
	health[n] = 0;
	memset ( dp, -1, sizeof(dp) );
	return go(0,health[0],0);
}

int main ( )
{
	fixed(cout);
	cout.precision(12);

	int nTests; cin >> nTests;
	for ( int i = 1; i <= nTests; ++i ) {
		int ans = solve();
		cout << "Case #" << i << ": " << ans << "\n";
	}

	return 0;
}
