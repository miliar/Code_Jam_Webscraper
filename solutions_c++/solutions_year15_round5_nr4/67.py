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
#define N 10010
int n , k , p[ N ] , f[ N ] , sum;
map<int,int> M;
typedef map<int,int>::iterator mi;
void build(){

}
void init(){
    k = getint(); M.clear();
    n = sum = 0;
    for( int i = 0 ; i < k ; i ++ )
        p[ i ] = getint();
    for( int i = 0 ; i < k ; i ++ ){
        f[ i ] = getint();
        sum += f[ i ];
        M[ p[ i ] ] = f[ i ];
    }
    while( sum > 1 ) n ++ , sum >>= 1;
}
vector<int> ans;
vector<int> tmp;
void solve(){
    ans.clear();
    tmp.clear();
    int got = 0; bool gotnon = false;
    for( mi it = M.begin() ; it != M.end() ; it ++ )
        while( it->second ){
            if( !gotnon ){
                it->second --;
                gotnon = true;
                tmp.PB( 0 );
                continue;
            }
            got ++;
            int vl = it->first;
            ans.PB( vl );
            int tsz = (int)tmp.size();
            for( int i = 0 ; i < tsz ; i ++ ){
                M[ tmp[ i ] + vl ] --;
                tmp.PB( tmp[ i ] + vl );
            }
            if( got == n ) break;
        }
    printf( "Case #%d:" , ++ cs );
    for( int i = 0 ; i < n ; i ++ )
        printf( " %d" , ans[ i ] );
    puts( "" );
}
int main(){
    build();
    __ = getint();
    while( __ -- ){
        init();
        solve();
    }
}



