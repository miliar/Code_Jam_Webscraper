#include <set>
#include <map>
#include <queue>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
#define N 1010
#define ll long long
#define d double
int getint(){
    int x=0,tmp=1; char c=getchar();
    while( (c<'0'||c>'9')&&c!='-' ) c=getchar();
    if( c == '-' ) c=getchar() , tmp = -1;
    while(c>='0'&&c<='9') x*=10,x+=(c-'0'),c=getchar();
    return x*tmp;
}
int t , n , s , ans , cs;
multiset<int> S;
typedef multiset<int>::iterator si;
void init(){
    n = getint(); s = getint();
    ans = 0; S.clear();
    for( int i = 0 ; i < n ; i ++ )
        S.insert( getint() );
}
void solve(){
    while( S.size() ){
        si it = S.end(); it --;
        int x = *it; ans ++;
        S.erase( S.find( x ) );
        if( S.size() ){
            int nd = s - x;
//            printf( "%d %d\n" , x , nd );
            it = S.lower_bound( nd );
            if( it != S.end() && (*it) == nd )
                S.erase( it );
            else  if( it != S.begin() ){
                it --;
                S.erase( it );
            }
        }
    }
    printf( "Case #%d: %d\n" , ++ cs , ans );
}
int main(){

    freopen( "A-large.in" , "r" , stdin );
    freopen( "A-large.out" , "w" , stdout );

    t = getint(); while( t -- ){
        init();
        solve();
    }

    fclose( stdin );
    fclose( stdout );
}
