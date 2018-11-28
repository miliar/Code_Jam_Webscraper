/*
 * Author:  Eyelids
 * Created Time:  2014/4/12 23:09:49
 * File Name: B.cpp
 */
#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<ctime>
using namespace std;
const double eps(1e-8);
typedef long long lint;
#define clr(x) memset( x , 0 , sizeof(x) )
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clrs( x , y ) memset( x , y , sizeof(x) )
int T;
double c, f, x;
int Sgn( double x ) {
    if ( x > eps ) return 1;
    if ( x < -eps ) return -1;
    return 0;
}

double Calc( double t ) {
    double a = 2.0; 
    while ( true ) {
        double tmp = c / a;
        if ( Sgn( t * a - x ) >= 0 ) return true;
        if ( t >= tmp && ( t - tmp ) * f >= c ) {
            t -= tmp;
            a += f; 
        } else 
            break;
    }

    return Sgn( t * a - x ) >= 0;
}

int main(){
    freopen( "BB.in", "r", stdin );
    freopen( "B.out", "w", stdout );
    
    int T;
    scanf( "%d", &T );
    int cas = 0;
    while ( T -- ) {
        scanf( "%lf%lf%lf", &c, &f, &x );
        
        double l = 0, r = 100000.0;
        double m;
        double ans;
        for ( int i = 0; i < 200; i ++ ) {
            m = ( l + r ) / 2.0;
            if ( Calc( m ) ) {
                ans = m;               
                r = m;
            } else {
                l = m; 
            }
        }
       
        printf( "Case #%d: ", ++ cas );
        printf( "%.7f\n", ans );
    }
    
    return 0;
}








