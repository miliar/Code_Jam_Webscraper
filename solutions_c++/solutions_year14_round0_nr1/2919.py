#include<iostream>
#include<vector>
#include<climits>
#include<stack>

using namespace std;


//Magic Trick
int main( int argc, const char* argv[] ) {
    int t;
    cin >> t;
    
    for( int i = 1; i <= t; i++ ) {
        int q1, q2;
        vector<vector<int>> grille1( 4, vector<int>( 4 ) );
        vector<vector<int>> grille2( 4, vector<int>( 4 ) );

        cin >> q1;
        q1--;
        for( int j = 0; j < 4; j++ ) {
            for( int k = 0; k < 4; k++ ) {
                cin >> grille1[j][k];
            }
        }

        cin >> q2;
        q2--;
        for( int j = 0; j < 4; j++ ) {
            for( int k = 0; k < 4; k++ ) {
                cin >> grille2[j][k];
            }
        }

        int resultCount = 0;
        int lastResult;
        for( int j = 0; j < 4; j++ ) {
            for( int k = 0; k < 4; k++ ) {
                if( grille1[q1][j] == grille2[q2][k] ) {
                    resultCount++;
                    lastResult = grille1[q1][j];
                }
            }
        }
        if(resultCount == 0)
            cout << "Case #" << i << ": Volunteer cheated!" << endl;
        else if(resultCount == 1)
            cout << "Case #" << i << ": " << lastResult << endl;
        else
            cout << "Case #" << i << ": Bad magician!" << endl;
    }

    return 0;
}