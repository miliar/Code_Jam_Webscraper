#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 
axScope_NSAutoreleasePool pool;


#define   DataSet axArray<uint64_t, 1204 >


void removeSmall( DataSet &data ) {
	
	int idx = 0;
	uint64_t n = data[0];
	
	for( int i=0; i<data.size(); i++ ) {
		if( n < data[i] ) {
			n = data[i];
			idx = i;
		}
	}
	data.removeBySwap( idx );
	
}


void eat_all(  uint64_t &s, DataSet &data ) {

	for( ;; ) {
	
		bool isExit = true;
		
		for( int i=0; i<data.size(); i++ ) {
			if( s > data[i] ) {
				s += data[i];
				data.removeBySwap( i );
				isExit = false;
				break;
			}
		}
		
		if( isExit ) return;
	}

}
int eat( uint64_t &s, DataSet &data ) {

	//ax_log( "{?} {?}", s , data.size() );
	
	eat_all( s, data );
	
	//ax_log( ">>{?} {?}", s , data.size() );
	
	if( data.size() == 0 ) return 0;

	if( s == 1 ) return (int) data.size();
	
	uint64_t s1 = s; 
	uint64_t s2 = s + s-1 ; 
	
	DataSet data1, data2 ;
	data1.copy( data );
	data2.copy( data );

	
	removeSmall( data1 );
	
	int r1 = eat( s1, data1 );
	int r2 = eat( s2, data2 );
	
	return ax_min( r1, r2 ) + 1 ;
}
 
	   
void solve() {
 
 
	uint64_t s;
	DataSet data;
	
	s = get_i();
	int c = get_i();

	data.resize( c );
	
	for( int i=0; i<c; i++ ) {
		data[i] = get_i();
	}
	
	printf("%d", eat( s, data ) );
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
