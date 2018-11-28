#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using std::min;
const int N = 13;
int a[N][N], col[N], row[N];
int n, m;

bool check() {
    for ( int i = 0;i < n;++i ) {
        for ( int j = 0;j < m;++j ) {
            if ( min ( row[i], col[j] ) != a[i][j] )
                return false;
        }
    }
    return true;
}

void solve() {
    scanf ( "%d%d", &n, &m );
    for ( int i = 0;i < n;++i )
        for ( int j = 0;j < m;++j )
            scanf ( "%d", &a[i][j] );
    for ( int s = 0;s < ( 1 << n );++s ) {
        for ( int i = 0;i < n;++i ) {
            if ( s& ( 1 << i ) ) row[i] = 1;
            else row[i] = 2;
        }
        for ( int t = 0;t < ( 1 << m );++t ) {
            for ( int i = 0;i < m;++i ) {
                if ( t& ( 1 << i ) ) col[i] = 1;
                else col[i] = 2;
            }
            if ( check() ) {
                printf ( " YES\n" );
                return;
            }
        }
    }
    printf ( " NO\n" );
    return;
}

int main() {
    int T;
    scanf ( "%d", &T );
    for ( int t = 1;t <= T;++t ) {
        printf ( "Case #%d:", t );
        solve();
    }
    return 0;
}