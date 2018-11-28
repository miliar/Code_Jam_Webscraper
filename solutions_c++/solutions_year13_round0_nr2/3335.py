/*
 * Author:  chlxyd
 * Created Time:  2013/4/13 17:58:37
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
int n , m ;
int s[200][200] ;
int r[200] , c[200] ;
string solve() {
    repf( i , 1 , n ) 
        repf( j , 1 , m )
            if ( s[i][j] < min( r[i] , c[j] ) )
                return "NO" ;
    return "YES" ;
}
int main(){
    int T ;
    freopen("B.out","w",stdout) ;
    scanf("%d" , &T ) ;
    repf( t , 1 , T  ){
        scanf("%d %d" , &n , &m );
        clr(r) ; clr(c) ;
        repf( i , 1 , n )
            repf( j , 1 , m ) 
                scanf("%d" , &s[i][j] ) ;
        repf( i , 1 , n ) {
            r[i] = 0 ;
            repf( j , 1 , m )
                r[i] = max( r[i] , s[i][j] ) ;
        }
        repf( i , 1 , m ) {
            c[i] = 0 ;
            repf( j , 1 , n )
                c[i] = max( c[i] , s[j][i] ) ;
        }
        printf("Case #%d: %s\n" , t , solve().c_str() ) ;
    }
}

