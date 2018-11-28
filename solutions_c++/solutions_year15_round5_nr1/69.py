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
#define N 1000010
int n , d;
int s[ N ] , m[ N ];
vector<int> v[ N ];
ll as , cS , rs;
ll am , cm , rm;
int psum[ N ];
void build(){

}
void init(){
    n = getint(); d = getint();
    s[ 0 ] = getint(); as = getint(); cS = getint(); rs = getint();
    m[ 0 ] = getint(); am = getint(); cm = getint(); rm = getint();
    for( int i = 1 ; i < n ; i ++ ){
        s[ i ] = ( (ll)s[ i - 1 ] * as + cS ) % rs;
        m[ i ] = ( (ll)m[ i - 1 ] * am + cm ) % rm;
        v[ m[ i ] % i ].PB( i );
        v[ i ].PB( m[ i ] % i );
    }
//    for( int i = 0 ; i < n ; i ++ )
//        printf( "%d %d\n" , s[ i ] , m[ i ] );
}
void DFS( int now , int prt , int tmin , int tmax ){
    int lbdr = max( tmin - d , tmax - d );
    int rbdr = min( tmin , tmax );
    if( lbdr > rbdr ) return;
    lbdr = max( lbdr , 0 );
    rbdr = min( rbdr , s[ 0 ] );
//    printf( "%d : %d %d %d %d\n" , now , lbdr , rbdr , tmin , tmax );
    psum[ lbdr ] ++;
    psum[ rbdr + 1 ] --;
    for( int i = 0 ; i < (int)v[ now ].size() ; i ++ )
        if( v[ now ][ i ] != prt )
            DFS( v[ now ][ i ] , now , min( tmin , s[ v[ now ][ i ] ] ) ,
                                    max( tmax , s[ v[ now ][ i ] ] ) );
}
void solve(){
    DFS( 0 , -1 , s[ 0 ] , s[ 0 ] );
    int ans = psum[ 0 ];
    for( int i = 1 ; i <= s[ 0 ] ; i ++ ){
        psum[ i ] += psum[ i - 1 ];
        ans = max( ans , psum[ i ] );
    }
    printf( "Case #%d: %d\n" , ++ cs , ans );
}
void out(){
    for( int i = 0 ; i <= n ; i ++ ) v[ i ].clear();
    for( int i = 0 ; i <= s[ 0 ] + 1 ; i ++ ) psum[ i ] = 0;
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


