#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#define x first
#define y second
using namespace std;
int n, m;
char s[110][110];
pair <int, int> getDir( int a, int b ) {
    int dx = 0, dy = 0;
    if ( s[a][b] == '^' ) dx --;
    if ( s[a][b] == 'v' ) dx ++;
    if ( s[a][b] == '<' ) dy --;
    if ( s[a][b] == '>' ) dy ++;
    return make_pair( dx, dy );
}
int check( int a, int b ) {
    if ( getDir( a, b ) == make_pair( 0, 0 ) ) return false;
    pair <int, int> p = getDir( a, b );

    int A = a, B = b;
    while ( true ) {
        a += p.x;
        b += p.y;
        if ( a < 0 || a >= n || b < 0 || b >= m ) break;
        if ( getDir( a, b ) != make_pair( 0, 0 ) ) {
            return false; 
        }
    }
    int sum = 0;
    a = A, b = B;
    for ( int i = 0; i < n; i ++ ) {
        if ( s[i][b] == '^' ) sum ++;
        if ( s[i][b] == '<' ) sum ++;
        if ( s[i][b] == '>' ) sum ++;
        if ( s[i][b] == 'v' ) sum ++;
    }
    for ( int i = 0; i < m; i ++ ) {
        if ( s[a][i] == '^' ) sum ++;
        if ( s[a][i] == '<' ) sum ++;
        if ( s[a][i] == '>' ) sum ++;
        if ( s[a][i] == 'v' ) sum ++;
    } 

    //cout <<a<<" "<<b<<" "<<" "<<s[a][b]<<" "<<sum<<endl;
    //cout <<a<<" "<<b<<" "<<sum<<endl;
    if ( sum == 2 ) return 2;

    return 1;
}

int main() {
    freopen( "A.in", "r", stdin );
    freopen( "A.out", "w", stdout );

    int T;
    scanf( "%d", &T );
    for ( int cas = 1; cas <= T; cas ++ ) {
        scanf( "%d%d", &n, &m );
        for ( int i = 0; i < n; i ++ ) {
            scanf( "%s", s[i] );
        }
        int ret = 0;
        bool flag = true;
        for ( int i = 0; i < n; i ++ ) {
            for ( int j = 0; j < m; j ++ ) {
                int tmp = check( i, j );
                if ( tmp == 2 ) flag = false;
                ret += tmp;
            }
        }
        if ( flag ) {
            printf( "Case #%d: %d\n", cas, ret );
        } else {
            printf( "Case #%d: IMPOSSIBLE\n", cas );
        }
    }

    return 0; 
}





