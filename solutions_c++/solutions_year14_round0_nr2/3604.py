#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 



void solve() {


	double C = get_f();
   	double F = get_f();
   	double X = get_f();
    
	double g = 2.0f;
    
    double t=0;
    double r=DBL_MAX;
    
    for( ;; ) {
        
        double v = X / g + t;
        
        if( v > r ) {
            printf( "%0.7lf", r );
            return;
        }
        
        r = v;
        t += C / g;
        g += F;

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
