#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 


bool isPD( uint64_t v ) {
	
	char sz[512];
	size_t l = sprintf( sz, "%llu", v );

	for( uint64_t i=0; i<l/2; i++ ) {
		if( sz[i] != sz[l-i-1] ) return false;
	}
	
	return true;
}

 
void solve() {
	
	uint64_t _min = get_ll();
	uint64_t _max = get_ll();
 
	
	//uint64_t s = (uint64_t) floor( sqrt( double( a ) ) );
	
	uint64_t s=1;
	
	int c = 0;
	
	for(;; s++ ) {
		
		if( !isPD( s ) ) continue;
	
		uint64_t r = s * s;
		if( r < _min ) continue;
		if( r > _max ) break;
		
		if( !isPD( r ) ) continue;
		
		c++;
	}
	
	printf("%d",c);
	
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
