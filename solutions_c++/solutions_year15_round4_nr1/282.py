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
#define N 110
char ch[ N ][ N ];
int r , c , ans;
void build(){

}
void init(){
    ans = 0;
    r = getint(); c = getint();
    for( int i = 1 ; i <= r ; i ++ )
        scanf( "%s" , ch[ i ] + 1 );
}
bool badr[ N ] , badc[ N ];
void solve(){
    for( int i = 0 ; i < N ; i ++ )
        badr[ i ] = badc[ i ] = false;
    for( int i = 1 ; i <= r ; i ++ ){
        int got = 0;
        for( int j = 1 ; j <= c ; j ++ )
            if( ch[ i ][ j ] != '.' )
                got ++;
        if( got == 1 ) badr[ i ] = true;
    }
    for( int i = 1 ; i <= c ; i ++ ){
        int got = 0;
        for( int j = 1 ; j <= r ; j ++ )
            if( ch[ j ][ i ] != '.' )
                got ++;
        if( got == 1 ) badc[ i ] = true;
    }
    bool flag = true;
    for( int i = 1 ; i <= r ; i ++ )
        for( int j = 1 ; j <= c ; j ++ )
            if( ch[ i ][ j ] != '.' && badr[ i ] && badc[ j ] )
                flag = false;
    if( !flag ){
        printf( "Case #%d: IMPOSSIBLE\n" , ++ cs );
        return;
    }
    ans = 0;
    for( int i = 1 ; i <= r ; i ++ ){
        for( int j = 1 ; j <= c ; j ++ )
            if( ch[ i ][ j ] != '.' ){
                if( ch[ i ][ j ] == '<' ) ans ++;
                break;
            }
        for( int j = c ; j >= 1 ; j -- )
            if( ch[ i ][ j ] != '.' ){
                if( ch[ i ][ j ] == '>' ) ans ++;
                break;
            }
    }
    for( int j = 1 ; j <= c ; j ++ ){
        for( int i = 1 ; i <= r ; i ++ )
            if( ch[ i ][ j ] != '.' ){
                if( ch[ i ][ j ] == '^' ) ans ++;
                break;
            }
        for( int i = r ; i >= 1 ; i -- )
            if( ch[ i ][ j ] != '.' ){
                if( ch[ i ][ j ] == 'v' ) ans ++;
                break;
            }
    }
    printf( "Case #%d: %d\n" , ++ cs , ans );
}
int main(){
    build();
    __ = getint();
    while( __ -- ){
        init();
        solve();
    }
}

