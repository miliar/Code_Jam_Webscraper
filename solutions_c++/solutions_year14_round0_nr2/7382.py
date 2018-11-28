#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

double c, f, x;
double lim = 0;

double dyn( double speed ) {
    double res = 0;
    res = min(1.0*x/speed, 1.0*c/speed + dyn(speed + f));
    
    return res;
}

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int tc; scanf( "%d", &tc );

    for ( int _ = 0; _ < tc; _++ ) {
        printf( "Case #%d: ", _+1 );
        scanf( "%lf%lf%lf", &c, &f, &x );
        double speed = 2.0;
        double res = x / speed;
        double res2 = 0;
        while(true) {
            res2 += c / speed;
            speed += f;
            if ( res2+(x/speed) > res ) {
                break;
            }
            else {
                res = res2 + x/speed;
            }
        }
        printf( "%.7lf", res );
        printf( "\n" );
    }
    
    return 0;
}
