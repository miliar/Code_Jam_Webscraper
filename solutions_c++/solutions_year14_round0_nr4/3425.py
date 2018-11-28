#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 


int CURRENT_R = 0;


inline bool GameA( axArray< float > &P1, axArray< float > &P2 ) {
    
    if( P1[0] < P2[0] ) {

        //printf("- %f %f\n", P1[0], P2.last() );
        
        P1.remove( 0 );
        P2.decSize( 1 );
        
        return false;
        
    }else {
        
        for( int i=0; i<P1.size(); i++ ) {
            
            if( P1[i] > P2[0] ) {
                P1.remove( i );
                P2.remove( 0 );
                return true;
            }
        }
        
        
        printf("\n******** ERROR!!!!!! *********** ");
        return false;
    }
    
}



inline bool GameB( axArray< float > &P1, axArray< float > &P2 ) {
    
    float a = P1.last(); P1.decSize( 1 );
    
    if( a > P2.last() ) {
        
        P2.remove( 0 );
        
        return true;
    }else {
        
        
        for( int i=0; i<P2.size(); i++ ) {
            
            if( P2[i] > a ) {
                P2.remove( i );
                break;
            }
            
        }
        
        return false;
    }
    
}


void solve() {

    int N = get_i();
    
    axArray< float > P1, P2, P3, P4;
    
    P1.resize( N );
    P2.resize( N );
    
    for( int i =0; i<N; i++ ) { P1[i] = get_f(); }
    for( int i =0; i<N; i++ ) { P2[i] = get_f(); }
    
    P1.bubbleSort( true ); P3.copy( P1 );
    P2.bubbleSort( true ); P4.copy( P2 );
 
    
    int A=0, B=0;
    for( int i =0; i<N; i++ ) {
        
        if( GameA( P1, P2 ) ) A++;
        if( GameB( P3, P4 ) ) B++;

    }
    
    
    
    printf( "%d %d", A, B );
    
    
}

int main() {
 
 
	
	int i=0, c=0;
				
	freopen( "/Users/tony/svn/personal/codejam/input.txt", "r", stdin );
    freopen( "/Users/tony/svn/personal/codejam/output.txt", "w", stdout );

	c = get_i();
	
	for( i=1; i<=c; i++ ) {
        CURRENT_R = i;
        
		printf( "Case #%d: ", i );
		solve();
		printf("\n");
	}



	return 0;
}
