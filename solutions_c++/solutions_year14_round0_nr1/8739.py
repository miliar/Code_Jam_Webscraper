#include <iostream>
#include <cstdio>
using namespace std;

int ans[2];
int matrix[4][4][2];

int main () {
    freopen("test.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    cin >> t;
    for( int tc=1; tc<=t; tc++ ) {
        // leo input
        for( int i = 0; i < 2; i++ ) {
            cin >> ans[i];
            for( int f = 0; f < 4; f++ )
                for( int c = 0; c < 4; c++ )
                    cin >> matrix[f][c][i];
        }
        
        // hallo posibles soluciones
        int res;
        int cantSols = 0;
        for( int c = 0; c < 4; c++ ) {
            for( int d = 0; d < 4; d++ ) {
                if( matrix[ans[0]-1][c][0] == matrix[ans[1]-1][d][1] ) {
                    cantSols++;
                    res = matrix[ans[0]-1][c][0];
                }
            }
        }
        
        cout << "Case #" << tc << ": ";
        if( cantSols == 0 )
            cout << "Volunteer cheated!" << endl;
        else if ( cantSols == 1 )
            cout << res << endl;
        else
            cout << "Bad magician!" << endl;
    }
    return 0;
}
