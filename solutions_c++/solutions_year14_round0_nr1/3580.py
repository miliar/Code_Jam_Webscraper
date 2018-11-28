#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 



void solve() {

    int a[4] = {0,0,0,0};
	int r = get_i() -1 ;
    
    for( int i=0; i<4; i++ ) {
        for( int j=0; j<4; j++ ) {
        
            int v = get_i();
            
            if( r == i ) {
                a[j] = v;
                
            }
        }
        
    }

    
    int c = 0;
    
    r = get_i() -1 ;
    
    for( int i=0; i<4; i++ ) {
        for( int j=0; j<4; j++ ) {
            
            int v = get_i();
            if( r == i ) {
                
                for( int k=0; k<4; k++ ) {
                    if( a[k] == v ) {
                        
                        if( c == 0 ) {
                            c = v;
                        }else {
                            
                            c = -1;
                        }
                    }
                }
                
            }
        }
        
    }
    
    if( c == 0 ) {
        
        printf( "Volunteer cheated!" );
        
    }else if( c == -1 ) {
        
        printf( "Bad magician!" );
    
    }else {
        printf( "%d", c );
    }
	

}

int main() {
 
 
	
	int i=0, c=0;
				
	freopen( "/Users/tony/svn/personal/codejam/input.txt", "r", stdin );
    freopen( "/Users/tony/svn/personal/codejam/output.txt", "w", stdout );

	c = get_i();
	
	for( i=1; i<=c; i++ ) {
	
		printf( "Case #%d: ", i );
		solve();
		printf("\n");
	}



	return 0;
}
