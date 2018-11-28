#include <iostream>

using namespace std;

int main() {
    int t, T, n,m, i,j;
    int max_r[100], max_c[100];
    int height[100][100];
    bool possible;

    cin >> T;
    for( t = 1; t <= T; t++ ) {
        cin >> n >> m;

        for( i = 0; i < n; i++ ) {
            for( j = 0; j < m; j++ ) {
                cin >> height[i][j];
            }
        }

        for( j = 0; j < m; j++ ) {
            max_c[j] = 0;
        }
        for( i = 0; i < n; i++ ) {
            max_r[i] = 0;
            for( j = 0; j < m; j++ ) {
                max_r[i] = max( max_r[i], height[i][j] );
                max_c[j] = max( max_c[j], height[i][j] );
            }
        }
        possible = true;
        for( i = 0; i < n && possible; i++ ) {
            for( j = 0; j < m; j++ ) {
                if( height[i][j] < max_r[i] && height[i][j] < max_c[j] ) {
                    possible = false;
                    break;
                }
            }
        }
        if( possible ) {
            cout << "Case #" << t << ": YES\n";
        } else {
            cout << "Case #" << t << ": NO\n";
        }
    }
    return 0;
}
