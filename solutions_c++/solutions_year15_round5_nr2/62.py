// eddy1021
#include <bits/stdc++.h>
using namespace std;
typedef double D;
typedef long long ll;
typedef pair<int,int> PII;
#define mod9 1000000009ll
#define mod7 1000000007ll 
#define INF 1023456789ll
#define INF16 10000000000000000ll
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define MT make_tuple
#define eps 1e-7
ll getint(){
    ll _x=0,_tmp=1; char _tc=getchar();
    while( (_tc<'0'||_tc>'9')&&_tc!='-' ) _tc=getchar();
    if( _tc == '-' ) _tc=getchar() , _tmp = -1;
    while(_tc>='0'&&_tc<='9') _x*=10,_x+=(_tc-'0'),_tc=getchar();
    return _x*_tmp;
}
ll mypow( ll _a , ll _x , ll _mod ){
    if( _x == 0 ) return 1ll;
    ll _tmp = mypow( _a , _x / 2 , _mod );
    _tmp = ( _tmp * _tmp ) % _mod;
    if( _x & 1 ) _tmp = ( _tmp * _a ) % _mod;
    return _tmp;
}
bool equal( D _x ,  D _y ){
    return _x > _y - eps && _x < _y + eps;
}
int __ = 1 , cs;
/*********default*********/
#define N 2010
ll n , k , a[ N ] , h[ N ];
vector<ll> v[ N ];
void build(){

}
void init(){
    n = getint(); k = getint();
    for( int i = 1 ; i <= n - k + 1 ; i ++ )
        a[ i ] = getint();
    for( int i = 0 ; i < k ; i ++ )
        v[ i ].PB( 0 );
    for( int i = 1 ; i < n - k + 1 ; i ++ ){
// x[ i + k ] = x[ i ] + ( a[ i + 1 ] - a[ i ] );
        v[ i % k ].PB( v[ i % k ].back() + ( a[ i + 1 ] - a[ i ] ) );
    }
}
void solve(){
    ll cst = 0 , maxh = 0;
    for( int i = 0 ; i < k ; i ++ ){
        ll tmin = 0 , tmax = 0;
        for( int j = 0 ; j < (int)v[ i ].size() ; j ++ ){
            if( v[ i ][ j ] > tmax ) tmax = v[ i ][ j ];
            if( v[ i ][ j ] < tmin ) tmin = v[ i ][ j ];
            //printf( "%d " , v[ i ][ j ] );
        }
        //puts( "" );
        h[ i ] = tmax - tmin;
        cst -= tmin;
        maxh = max( maxh , h[ i ] );
    }
    cst = a[ 1 ] - cst;
//    cst -= a[ 1 ];
    cst = ( cst % k + k ) % k;
    ll tmp = 0;
    for( int i = 0 ; i < k ; i ++ ) tmp += maxh - h[ i ];
    printf( "Case #%d: %I64d\n" , ++ cs , maxh + ( tmp < cst ? 1ll : 0ll ) );
}
void out(){
    for( int i = 0 ; i < k ; i ++ ) v[ i ].clear();
}
int main(){
    build();
    __ = getint();
    while( __ -- ){
        init();
        solve();
        out();
    }
}



