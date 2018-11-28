#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MOD = 1000000007;
const int ALPH = 26;

inline int add ( int a, int b ) { return (a+b)%MOD; }
inline int prod ( int a, int b ) { return (int) ( (ll(a)*ll(b))%ll(MOD) ); }
inline int prod3 ( int a, int b, int c ) { return prod(a,prod(b,c)); }

const int MAX_N = 102;

int fact[MAX_N];
bool G[ALPH][ALPH], seen[ALPH];

bool cycle ( int i ) {
	if ( seen[i]++ ) return true;
	for ( int j = 0; j < ALPH; ++j )
		if ( G[i][j] && i != j )
			if ( cycle ( j ) )
				return true;
	return false;
}

int solveGroup ( vector<pair<int,int> > v )
{
	int ans = 1;
	int beg_cnt, end_cnt, mid_cnt;
	for ( int x = 0; x < ALPH; ++x )
	{
		beg_cnt = end_cnt = mid_cnt = 0;
		for ( int i = 0; i < (int)v.size(); ++i )
			if ( v[i].first == x && v[i].second == x ) mid_cnt++;
			else if ( v[i].first == x ) beg_cnt++;
			else if ( v[i].second == x ) end_cnt++;

		if ( beg_cnt > 1 || end_cnt > 1 )
			return 0;

		ans = prod ( ans, fact[mid_cnt] );
	}
	return ans;
}

int nCars;
string cars[MAX_N];
int color[MAX_N];

bool invalidCar ( const string& s )
{
	const int len = s.size();
	for ( int i = 0; i < len; ++i )
		for ( int j = i+1; j+1 < len; ++j )
			if ( s[j] != s[i] && s[j+1] == s[i] )
				return true;
	return false;
}

int solve ( )
{
	memset ( G, false, sizeof ( G ) );

	vector<int> car_mask ( nCars, 0 );
	vector<pair<int,int> > car_code ( nCars );
	for ( int i = 0; i < nCars; ++i ) {
		for ( int j = 0; j < (int)cars[i].size(); ++j )
			car_mask[i] |= (1<<int(cars[i][j]-'a'));
		car_code[i].first = int(cars[i][0]-'a');
		car_code[i].second = int(cars[i][cars[i].size()-1]-'a');
		G[car_code[i].first][car_code[i].second] = true;
	}

	for ( int x = 0; x < ALPH; ++ x )
		for ( int i = 0; i < nCars; ++i )
			if ( ((car_mask[i]>>x)&1) ) 
				if ( car_code[i].first != x && car_code[i].second != x )
					for ( int j = 0; j < nCars; ++j )
						if ( (((car_mask[j])>>x)&1) && i != j )
							return 0;

	for ( int i = 0; i < nCars; ++i )
		if ( invalidCar(cars[i]) )
			return 0;

	for ( int i = 0; i < ALPH; ++i ) {
		memset ( seen, false, sizeof ( seen ) );
		if ( !seen[i] && cycle ( i ) )
			return 0;
	}

	for ( int i = 0; i < nCars; ++i )
		color[i] = i;
	for ( int i = 0; i < nCars; ++i )
		for ( int j = 0; j < nCars; ++j )
			if ( car_mask[i]&car_mask[j] ) {
				int oldC=color[i], newC=color[j];
				for ( int k = 0; k < nCars; ++k )
					if ( color[k] == oldC )
						color[k] = newC;
			}


	int ans = 1, nGroups = 0;
	for ( int c = 0; c < nCars; ++c ) {
		vector<pair<int,int> > group;
		for ( int i = 0; i < nCars; ++i )
			if ( color[i] == c )
				group.push_back ( car_code[i] );
		if ( group.empty() ) continue;

		ans = prod ( ans, solveGroup ( group ) );
		nGroups++;
	}

	ans = prod ( ans, fact[nGroups] );
	return ans;
}

int main ( )
{
	fact[0] = 1;
	for ( int i = 1; i < MAX_N; ++i )
		fact[i] = prod ( i, fact[i-1] );

	int nCases;
	cin >> nCases;
	for ( int curCase = 1; curCase <= nCases; ++curCase )
	{
		cin >> nCars;
		for ( int i = 0; i < nCars; ++i )
			cin >> cars[i];

		printf ( "Case #%d: %d\n", curCase, solve() );
	}
	
	return 0;
}
