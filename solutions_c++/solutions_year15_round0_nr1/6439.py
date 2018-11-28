#include <bits/stdc++.h>
using namespace std;

#define MAX 205
#define MOD 1000000007
#define all( x ) x.begin() , x.end()
#define unique( c ) ( c ).resize( unique( all( c ) ) - ( c ).begin() )
#define debug( a ) cerr << #a << ": " << a << endl;

int main (){
    freopen("D:/CodeBlocks/in.txt","r",stdin);
    freopen("D:/CodeBlocks/out.txt","w",stdout);
    int t; cin >> t;
    for ( int tc = 0 ; tc < t ; tc++ ){
        int n; cin >> n;
        string s; cin >> s;
        int persons = 0 , ans = 0;
        if( s[ 0 ] == '0' ) ans = persons = 1;
        else persons += ( s[ 0 ] - '0' );
        for ( int i = 1 ; i < n + 1 ; i++ ){
            int cnt = s[ i ] - '0';
            if( persons < i ) {
                ans += ( i - persons );
                persons += ( i - persons );
            }
            persons += ( s[ i ] - '0' );
        }
        printf( "Case #%d: %d\n" , tc + 1 , ans );
    }
    return 0;
}
