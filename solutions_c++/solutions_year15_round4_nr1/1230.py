#include <bits/stdc++.h>
using namespace std;
int h, w;
vector<string> G;

bool ok ( int i, int j, char d ) {
	int ni = i, nj = j, di = 0, dj = 0;
	if ( d == '^' ) di = -1;
	else if ( d == 'v' ) di = 1;
	else if ( d == '>' ) dj = 1;
	else dj = -1;
	do {
		ni += di;
		nj += dj;
		if ( ni < 0 || nj < 0 ) return false;
		if ( ni >= h || nj >= w ) return false;
		if ( G[ni][nj] != '.' ) return true;
	}
	while ( true );
}

int main ( )
{
	freopen ( "A-large.in", "r", stdin );
	freopen ( "output", "w", stdout );
	int ntc;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test ) {

		cin >> h >> w;
        G.resize(h);
        for ( int i = 0; i < h; ++i )
			cin >> G[i];

		int ans = 0;
		for ( int i = 0; i < h; ++i )
			for ( int j = 0; j < w; ++j )
			{
				if ( G[i][j] == '.' ) continue;
				if ( ok(i,j,G[i][j]) ) continue;
				if ( ok(i,j,'<') || ok(i,j,'>') || ok(i,j,'^') || ok(i,j,'v') )
					ans++;
				else {
					ans = -1;
					i = h; j = w;
				}
			}

		printf ( "Case #%d: ", test );
		if ( ans == -1 ) printf ( "IMPOSSIBLE\n" );
		else printf ( "%d\n", ans );

	}
	return 0;
}
