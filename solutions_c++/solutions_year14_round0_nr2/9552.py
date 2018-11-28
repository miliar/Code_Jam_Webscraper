#include<iostream>
using namespace std;
int T;
double c, f, x, Left, Right, mid;
double ret;
bool Check( double time ) {
    double ability = 2.0;
    while ( true ) {
        double buf = c / ability;
        if ( time * ability >= x ) return true;
        if ( ( time - buf ) * f >= c )
            time -= buf, ability += f;
        else
            break;
    }
    
    return time * ability - x >= 0;
}

int main(){
    freopen( "BB.in", "r", stdin );
    freopen( "BB.out", "w", stdout );
    
    cin >>T;
    for ( int cas = 1; cas <= T; cas ++ ) {
        cin  >>c>>f>>x;    
            
        Left = 0, Right = 10000000; 
        for ( int i = 0; i < 500; i ++ ) {
            mid = ( Left + Right ) / 2.0;
            if ( Check( mid ) ) {
                ret = mid;
                Right = mid; 
            } else {
                Left = mid; 
            }
        }
        
        cout <<"Case #"<<cas<<": ";
        printf( "%.7f\n", ret );
    }
    
    return 0;    
}







