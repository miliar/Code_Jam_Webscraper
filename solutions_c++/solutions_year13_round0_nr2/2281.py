#include <cstdio>
#include <fstream>
#include <algorithm>
#include <queue>
#include <cstring>

FILE *fin = fopen( "Bin.txt", "r" );
FILE *fout = fopen( "Bout.txt", "w" );

using namespace std;

struct busen{

	int r, s, h;
	
	busen() {}
	
	busen ( int _r, int _s, int _h ){
		r = _r;
		s = _s;
		h = _h;
	}
	
	friend bool operator < ( const busen &A, const busen &B ){
		return A.h > B.h;
	} 

} niz[110 * 100];

int T, R, S;
int mat[110][110];

bool row[110], col[110];

queue < busen > Q;

inline void solve ( int t ){

	memset( row, false, sizeof row );
	memset( col, false, sizeof col );

	while ( !Q.empty() ) Q.pop();
	
	int cnt = 0;
	fscanf( fin, "%d%d", &R, &S );

	for ( int i = 0; i < R; ++i ){
		for ( int j = 0; j < S; ++j ){
			int x; fscanf( fin, "%d", &x );
			niz[cnt++] = busen( i, j, x );
		}
	}

	sort( niz, niz + cnt );
	
	bool ok = true;
	int curr = 101;
	
	for ( int i = 0; i < cnt; ++i ){
		
		if ( niz[i].h != curr ){
			curr = niz[i].h;
			while ( !Q.empty() ){
				row[ Q.front().r ] = col[ Q.front().s ] = true;
				Q.pop();
			}
		}
		
		if ( row[ niz[i].r ] && col[ niz[i].s ] ){ ok = false; break; }
		Q.push( niz[i] );
		
	}
	
	if ( ok ) fprintf( fout, "Case #%d: YES\n", t ); else fprintf( fout, "Case #%d: NO\n", t );
	
}

int main ( void ){

	fscanf( fin, "%d", &T );
	for ( int i = 0; i < T; ++i ) solve( i + 1 ); 

	return 0;

}