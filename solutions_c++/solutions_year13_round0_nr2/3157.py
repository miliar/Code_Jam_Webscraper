#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 


int tbl[100][100];
int N, M;
 


bool canCut( int x, int y ) {

	int target = tbl[x][y];

	bool b = true;
	
	for( int i=0;i<M; i++ ) {
	
		if( tbl[x][i] > target ) {
			b = false;
			break;
		}
	}
	
	if( b ) return true;
	

	b = true;
	for( int i=0;i<N; i++ ) {
	
		if( tbl[i][y] > target ) {
			b = false;
			break;
		}
	}
	
	if( b ) return true;
		
	return false;

}

void solve() {
	
	N = get_i();
	M = get_i();

	for( int i=0;i<N;i++ ) {
		for( int j=0;j<M;j++ ) {
			tbl[i][j] = get_i();
		}
		get_c(); // newline
	}
	
	/*
	for( int i=0;i<N;i++ ) {
		for( int j=0;j<M;j++ ) {
			printf("%d", tbl[i][j] );
		}
	}
	*/
	
	for( int i=0;i<N;i++ ) {
		for( int j=0;j<M;j++ ) {
		
			//printf("> %d %d \n", i, j );
			if( !canCut( i, j ) ) {
				printf("NO");
				return;
			}
		}
	}
	
	printf("YES");
	
}

int main() {

	int i=0, c=0;
				
	freopen( "/Users/tony/svn/tony/codejam/input.txt", "r", stdin );
	freopen( "/Users/tony/svn/tony/codejam/output.txt", "w", stdout );

	c = get_i();
	

	for( i=1; i<=c; i++ ) {
	
		printf( "Case #%d: ", i );

		solve();
		
		printf("\n");
	}



	return 0;
}
