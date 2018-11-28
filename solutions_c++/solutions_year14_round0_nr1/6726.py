#include <iostream>

using namespace std;

void getNumbers ( int answered_in[], int ROWS, int COLS ) {
    int row, i, j;
    cin >> row;
    cin.ignore ( 4096, '\n' );
    for ( i = 1; i <= ROWS; i++ ) {
        if ( i == row ) {
            for ( j = 0; j < COLS; j++ ) {
                cin >> answered_in[j];
            }
            cin.ignore ( 4096, '\n' );
        } else {
            cin.ignore ( 4096, '\n' );
        }
    }
}

int main ( int argc, char **argv ) {
    const int ROWS = 4, COLS = 4;

    int T, c, i, j;
    int possible_numbers_n;
    int answered_in1[COLS], answered_in2[COLS], possible_numbers[COLS];

    cin >> T;
    for ( c = 1; c <= T; ++c ) {
        getNumbers(answered_in1,ROWS,COLS);
        getNumbers(answered_in2,ROWS,COLS);
        
        possible_numbers_n = 0;
        for( i = 0; i < COLS; i++ ) {
            for( j = 0; j < COLS; j++ ) {
                if(answered_in1[i] == answered_in2[j] ) {
                    possible_numbers[possible_numbers_n++] = answered_in1[i];
                    break;
                }
            }
        }
        
        cout << "Case #" << c << ": ";
        if( possible_numbers_n == 1 ) {
            cout << possible_numbers[0] << "\n";
        } else if( possible_numbers_n == 0 ) {
            cout << "Volunteer cheated!\n";
        } else {
            cout << "Bad magician!\n";
        }
    }

    return 0;
}
