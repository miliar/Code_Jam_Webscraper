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
#define eps 1e-11
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
#define N 110
int n;
D v , x;
vector< pair<D,D> > vv;
void build(){

}
void init(){
    n = getint(); vv.clear();
    int r1 , r2 , c1 , c2;
    //scanf( "%lf%lf" , &v , &x );
    r1 = getint();
    r2 = getint();
    c1 = getint();
    c2 = getint();
    v = r1 * 10000 + r2;
    x = c1 * 10000 + c2;
    for( int i = 0 ; i < n ; i ++ ){
        r1 = getint();
        r2 = getint();
        c1 = getint();
        c2 = getint();
        int tr = r1 * 10000 + r2;
        int tc = c1 * 10000 + c2;
        vv.PB( MP( tc , tr ) );
//        scanf( "%lf%lf" , &r[ i ] , &c[ i ] );
    }
    sort( vv.begin() , vv.end() );
}
bool can( D now ){
    D suml = 0 , sumvl = 0;
    D sumr = 0 , sumvr = 0;
    for( int i = 0 ; i < n ; i ++ ){
        D tk = min( v - sumvl , now * vv[ i ].SE );
        suml += tk * vv[ i ].FI;
        sumvl += tk;
        if( equal( v , sumvl ) ) break;
    }
    if( !equal( v , sumvl ) ) return false;
    for( int i = n - 1 ; i >= 0 ; i -- ){
        D tk = min( v - sumvr , now * vv[ i ].SE );
        sumr += tk * vv[ i ].FI;
        sumvr += tk;
        if( equal( v , sumvr ) ) break;
    }
    if( !equal( v , sumvr ) ) return false;
    D lll = suml / sumvl;
    D rrr = sumr / sumvr;
    return lll - eps < x && x < rrr + eps;
}
void solve(){
    if( vv[ 0 ].FI > x + eps || vv[ n - 1 ].FI < x - eps ){
        printf( "Case #%d: IMPOSSIBLE\n" , ++ cs );
        return;
    }
    D l = 0 , r = 1e20 , mid;
    for( int i = 0 ; i < 1000 ; i ++ ){
        mid = ( l + r ) * 0.5;
        if( can( mid ) ) r = mid;
        else l = mid;
    }
    printf( "Case #%d: %.10f\n" , ++ cs , mid );
}
int main(){
    build();
    __ = getint();
    while( __ -- ){
        init();
        solve();
    }
}


