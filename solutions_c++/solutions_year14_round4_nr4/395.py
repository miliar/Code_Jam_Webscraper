#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cmath>
using namespace std ;
const int MAXN = 100001 ;
const int inf = 1000000000;
const int mod = 1000000007;

struct node {
    int next[27] ;
}x[MAXN] ;
int top = 0 ;
int n , m ;
char s[10][201];
int cost[1<<10] ;
int f[10][1<<10] ;
int g[10][1<<10] ;

void add( char* a ) {
    int now = 0 ;
    for ( int i = 0 ; a[i] ; ++i ) {
        if ( x[now].next[a[i]-'A'] == 0 )
            x[now].next[a[i]-'A'] = ++top ;
        now = x[now].next[a[i]-'A'] ;
    }
}

int ccc( int S  ) {

    for (int i = 0 ; i <= top ; ++i )
        memset( x[i].next , 0 , sizeof x[i].next ) ;
    top = 0 ;
    for ( int i = 0 ; i < n ; ++i ) {
        if ( S&(1<<i) ) {
            add(s[i]);
        }
    }
    return top+1 ;
}


int main() {

    int T ;
    int test = 1 ;

    cin >> T ;
    while ( T-- ) {

        cin >> n ;
        cin >> m ;
        for ( int i = 0 ; i < n ;++i ) {
            cin >> s[i];
        }
        for ( int i = 0 ; i < (1<<n) ; ++i ) {
            cost[i] = ccc(i);

        }

        for ( int i = 0 ; i <= m ; ++i )
            for ( int j = 0 ; j < (1<<n) ; ++j )
                f[i][j] = -inf ;
        f[0][0] = 0 ;
        g[0][0] = 1  ;

        for ( int i = 0 ; i < m ; ++i ) {
            for ( int j = 0 ; j < (1<<n) ; ++j ) {
                for ( int k = 1 ; k < (1<<n) ; ++k )
                if ( (j&k) == 0 ) {
                    int c = f[i][j] + cost[k] ;

                    if ( f[i+1][j|k] < c ) {
                        f[i+1][j|k] = c ;
                        g[i+1][j|k] = g[i][j] ;
                    }
                    else if ( f[i+1][j|k] == c ) {
                        g[i+1][j|k] += g[i][j] ;
                        g[i+1][j|k] %= mod ;
                    }
                }
            }
        }

        cout << "Case #" << test++ << ": ";
        cout << f[m][(1<<n)-1] << " " << g[m][(1<<n)-1] << endl ;
    }

    return 0;
}
