#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int a[1100];

int main() {
    int i, j, k;
    int t, T;
    int n;
    freopen( "A-large (1).in", "r", stdin);
    freopen( "A-l.out", "w", stdout);
    cin >> T;
    for( t = 1; t <= T; t++ ){
        int x, y, ret = 0;
        cin >> n;
        x = 0, y = 0;
        for( i = 0; i < n; i++ )
            cin >> a[i];
        for( i = 1; i < n; i++ )
            if( a[i] < a[i-1] )
                x += a[i-1] - a[i];
        for( i = 0; i < n - 1; i++)
            if( a[i] - a[i+1]  >= 0)
                ret = max( ret, a[i] - a[i+1] );
        for( i = 0; i < n - 1; i++)
            y += min( ret, a[i] );
        printf( "Case #%d: %d %d\n", t, x, y);
    }
    

    return 0;
}
