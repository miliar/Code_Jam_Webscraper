#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXR 100
#define MAXC 100

int T, R, C;
int b[MAXR][MAXC];
int act[MAXR][MAXC];

void modifyC(int ci, int nv) {
	for (int ri = 0; ri < R; ri++) {
		act[ri][ci] = nv;
	}
}

int canModifyC(int ci) {
	int bmax = b[0][ci];
	for (int ri = 1; ri < R; ri++) {
		bmax = max(bmax, b[ri][ci]);
	}
	int dmax = act[0][ci] - bmax;
	for (int ri = 0; ri < R; ri++) {
		int d = act[ri][ci] - bmax;
		dmax = max(d, dmax);
	}
	return dmax > 0 ? bmax : 0;
}

void modifyR(int ri, int nv ) {
	for (int ci = 0; ci < C; ci++) {
		act[ri][ci] = nv;
	}
}

int canModifyR(int ri ) {
	int bmax = b[ri][0];
	for (int ci = 1; ci < C; ci++) {
		bmax = max(bmax, b[ri][ci]);
	}
	int dmax = act[ri][0] - bmax;
	for (int ci = 0; ci < C; ci++) {
		int d = act[ri][ci] - bmax;
		dmax = max(d, dmax);
	}
	return dmax > 0 ? bmax : 0;
}

int ok() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if ( b[i][j] != act[i][j]) return 0;
		}
	}
	return 1;
}

int solve() {
	for ( int ri = 0; ri < R; ++ri ) for ( int ci = 0; ci < C; ++ci ) act[ri][ci] = 100;
	while ( 1 ) {
		int modified = 0;
		for (int ri = 0; ri < R; ri++) {
			int d = canModifyR(ri);
			if ( d > 0 ) {
				modifyR(ri, d);
				modified = 1;
			}
		}
		for (int ci = 0; ci < C; ci++) {
			int d = canModifyC(ci);
			if (d > 0 ) {
				modifyC(ci, d);
				modified = 1;
			}
		}
		if ( ok() ) {
			return 1;
		}
		if (modified == 0) {
			return 0;
		}
	}
}

int main() {
	scanf( "%d", &T );
	for ( int ii = 1; ii <= T; ++ii ) {
		scanf( "%d%d", &R, &C );
		for ( int ri = 0; ri < R; ++ri ) {
			for ( int ci = 0; ci < C; ++ci ) {
				scanf( "%d", &b[ri][ci] );
			}
		}
		printf( "Case #%d: %s\n", ii, solve() ? "YES" : "NO" );
	}
	return 0;
}