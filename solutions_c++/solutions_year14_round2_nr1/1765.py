#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 


const int kN = 255;


int N;

char r [kN][kN];
int  ri[kN][kN];

int _clac( int idx ) {

    int min = INT_MAX;
    int max = 0;
    
    for( int i=0; i<N; i++ ) {
        
        int v = ri[i][ idx ];
        
        if( v > max ) {
            max = v;
        }
        
        if( v < min ) {
            min = v;
        }
        
        
    }
    
    if( min == max ) return 0;
    
    int r = INT_MAX;
    
    for( int c=min; c<=max; c++ ) {
        
        int s = 0;
        for( int i=0; i<N; i++ ) {
            
            s += abs( c - ri[i][ idx ] );
            
        }
        
        if( s < r ) r = s;
        
        
    }
    
    return r;
    
    
}

void _conv2( char *a, char *b, int *c ) {

    
    int N = (int) strlen( a );
    int ib = 0;
    
    b[ib] = a[0];
    c[ib] = 1;
    
    for( int i=1; i<N; i++ ) {
        
        if( a[i] == b[ib] ) {
            c[ib]++;
            continue;
        }
        
        ib++;
        
        b[ib] = a[i];
        c[ib] = 1;
        
    }
    
    ib++;
    b[ib] = 0;
    
}


void _conv1( char *a, char *b ) {
 
    int N = (int) strlen( a );
    int ib = 0;
    
    b[ib] = a[0];
    
    for( int i=1; i<N; i++ ) {
        
        if( a[i] == b[ib] ) continue;
        
        ib++;
        b[ib] = a[i];
        
    }
    
    ib++;
    b[ib] = 0;
    
}

void solve() {
    
    char s[kN][kN];
    
    N = get_i();
    
    for( int i=0; i<N; i++ ) {
        scanf( "%s", s[i] );
    }
    
    {
        char target[kN];
        char tmp[kN];
        
        for( int i=0; i<N; i++ ) {
        
            if( i == 0 ) {
                _conv1( s[i], target );
                
            }else {
                _conv1( s[i], tmp );
                
                if( strcmp( tmp, target ) != 0 ) {
                    printf("Fegla Won");
                    return;
                }
            }
        }
        
    }
    
    
    for( int i=0; i<N; i++ ) {
        
        _conv2( s[i], r[i], ri[i] );
        
//        int n = (int) strlen( r[i] );
//        for( int j=0; j<n; j++ ) {
//            printf("%c ", s[i][j]);
//        }
//        printf( "\n" );
//        
//        for( int j=0; j<n; j++ ) {
//            printf("%d ", ri[i][j] );
//        }
//        printf( "\n" );
        
        
    }


    int c = 0;
    
    for( int i=0; i<strlen( r[0] ); i++ ) {
        
        c += _clac( i );
        
    }
    
    printf("%d", c );
    
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
