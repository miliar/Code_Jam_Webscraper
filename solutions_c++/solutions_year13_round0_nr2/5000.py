#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

const int MAXN = 128;

int n, m, mx;
int a[MAXN][MAXN];
int h[MAXN], v[MAXN];

void read() {
    int i, j;

    mx = 0;

    scanf ( "%d %d", &n, &m );

    for ( i = 0; i < n; ++ i ) {
        for ( j = 0; j < m; ++ j ) {
            scanf ( "%d", &a[i][j] );
            mx = max ( a[i][j], mx );
        }
    }

}

bool solve() {
    int i, j;

    memset ( h, 0, sizeof h );
    memset ( v, 0, sizeof v );

    for ( i = 0; i < n; ++ i ) {
        bool l = 0;
        for ( j = 1; j < m; ++ j ) {
            if ( a[i][j - 1] != a[i][j] ) {
                l = 1;
                break;
            }
        }

        if ( !l ) h[i] = a[i][0];
    }

    for ( i = 0; i < m; ++ i ) {
        bool l = 0;
        for ( j = 1; j < n; ++ j ) {
            if ( a[j - 1][i] != a[j][i] ) {
                l = 1;
                break;
            }
        }

        if ( !l ) v[i] = a[0][i];
    }

    for ( i = 0; i < n; ++ i ) {
        for ( j = 0; j < m; ++ j ) {
            if ( a[i][j] < mx )
            if ( h[i] != a[i][j] && v[j] != a[i][j] ) return 0;
        }
    }

    return 1;

}

int main() {
    int i, tests;

    scanf ( "%d", &tests );

    for ( i = 1; i <= tests; ++ i ) {
        read();
        bool ret = solve();

        if ( ret == 1 ) printf ( "Case #%d: YES\n", i );
        else printf ( "Case #%d: NO\n", i );
    }

    return 0;

}
