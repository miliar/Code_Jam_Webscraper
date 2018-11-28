#include <bits/stdc++.h>

using namespace std;

typedef vector<int> VI;

int t;
int n, k;
float prob[205];
float maxp;

float calc( const VI &sel )
{
	float pb[105] = {};
	float yes, no;
	int u;
	pb[0] = 1.0;
	int kd2 = k>>1;

	for( int j=0, k=sel.size(); j<k; ++j ) {
		u = sel[j];
		yes = prob[u];
		no = 1-yes;

		for( int i=kd2; i>=0; --i ) {
			pb[i] *= no;
			if(i>0) pb[i] += pb[i-1]*yes;
		}
	}

	return pb[kd2];
}

void dfs( int u, VI &s )
{
	if( s.size()==k ) {
		maxp = max( maxp, calc(s) );
		return;
	}
	if( u>=n ) return;

	s.push_back(u);
	dfs( u+1, s );
	s.pop_back();
	dfs( u+1, s );
}

void input( void )
{
	scanf( "%d%d", &n, &k );
	for( int i=0; i<n; ++i ) scanf( "%f", &prob[i] );
}

int main( void )
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
	VI s;
	cin >> t;

	for( int ti=1; ti<=t; ++ti ) {
		input();

		maxp = 0;
		s = VI();
		dfs( 0, s );

		printf( "Case #%d: %.8f\n", ti, maxp );
	}


	return 0;
}
