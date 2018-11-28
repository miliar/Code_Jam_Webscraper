#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <iomanip> 

using namespace std;

long double calculateNext ( long double &oneStep, long double &stay, int i );
long double freq ( int x );

/*************** main ***************/
long double C, F, X;
int main () {
    freopen ( "input.in","r", stdin );
    freopen ( "output.out","w", stdout );
    
    int T;
    
    cin >> T;
    
    for ( int t=1; t<=T; t++ ) {
        int i=0;
        long double oneStep = 0.0, stay = 1.0, sum = 0.0;
    
        cin >> C >> F >> X;
              
        while ( stay >= oneStep ) {
            sum += calculateNext ( oneStep, stay, i );
            i++;
        }
        
        cout << setprecision (7) << fixed;
        cout << "Case #"<< t << ": " << sum << endl;
    
    }
    
    fclose ( stdin );
    fclose ( stdout );

    return 0;
}
/*************** ***** ***************/


/*************** calculateNext ***************/
long double calculateNext ( long double &oneStep, long double &stay, int i ) {
    long double Ctime;
    Ctime = C/freq (i);
    
    stay = X/freq (i);
    oneStep = Ctime + X/freq (i+1);
    
    if ( stay < oneStep ) {
        return stay;
    }
    else {
        return Ctime;
    }
}
/*************** ***** ***************/


/*************** freq ***************/
long double freq ( int x ) {
    long double ret;
    
    ret = 2.0 + ( long double ) x * F; 
    
    return ret;
}
