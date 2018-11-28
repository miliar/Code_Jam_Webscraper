#include <iostream>
#include <cstdio>
using namespace std;

int Case, n, m, cnt, A[105][105];


int main ( ) {
    freopen ( "B-large.in", "r", stdin );
    freopen ( "output.txt", "w", stdout );
    cin >> Case;
    for ( cnt = 1; cnt <= Case; ++cnt ) {
        cin >> n >> m;
        for ( int i = 1; i <= n; ++i )
            for ( int j = 1; j <= m; ++j )
                cin >> A[i][j];

        int tmp = 0;
        for ( int i = 1; i <= n; ++i ) {
            for ( int j = 1; j <= m; ++j ) {
                int row = 0, cul = 0;
                for ( int x = 1; x <= m; ++x )
                    if ( A[i][j] >= A[i][x] ) row++;
                for ( int y = 1; y <= n; ++y )
                    if ( A[i][j] >= A[y][j] ) cul++;
                if ( row == m || cul == n ) tmp++;
            }
        }
        cout << "Case #" << cnt << ": ";
        if ( tmp == n * m ) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}
