#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string isPatternPossible( int** pattern, int rows, int cols );

int main( int argc, char* argv[] ) {
    ifstream infile( "small.txt" );
    int num_cases;

    infile >> num_cases;
    for ( int i = 0; i < num_cases; i++ ) {
        int rows;
        int cols;
        int** lawn;
        
        infile >> rows;
        infile >> cols;
        // Allocate memory and read file into said memory
        lawn = (int**) malloc( sizeof(int*) * rows );
        for ( int j = 0; j < rows; j++ ) {
            lawn[j] = (int*) malloc( sizeof(int) * cols );
            for ( int k = 0; k < cols; k++ )
                infile >> lawn[j][k];
        }
        // Compute and print results
        cout << "Case #" << ( i + 1 ) << ": " << isPatternPossible( lawn, rows, cols ) << endl;
        // Free memory
        for ( int j = 0; j < rows; j++ ) {
            free( lawn[j] );
        }
        free( lawn );
    }
    
    return 0;
}

// By... uh... finding matching rows or columns, incrementing those numbers until i have some more matching columns or rows until either the whole board is (all rows/cols match) number OR nothing matches
// OH I got it, match rows and columns, replacing them with 0 as a wildcard -- after going through it all, see if the whole thang is 0s
// If it is, great, if not boooo
// I can't prove this works, but it sounds good to me
string isPatternPossible( int** pattern, int rows, int cols ) {
    for ( int cur_height = 1; cur_height <= 100; cur_height++ ) {
        // Try to match rows...
        for ( int i = 0; i < rows; i++ ) {
            bool isRowMatch = true;
            for ( int j = 0; j < cols; j++ ) {
                if ( pattern[i][j] != 0 && pattern[i][j] != cur_height )
                    isRowMatch = false;
            }
            if ( isRowMatch ) {
                for ( int k = 0; k < cols; k++ ) pattern[i][k] = 0;
            }
        }
        // Then try to match columns!
        for ( int j = 0; j < cols; j++ ) {
            bool isColMatch = true;
            for ( int i = 0; i < rows; i++ ) {
                if ( pattern[i][j] != 0 && pattern[i][j] != cur_height )
                    isColMatch = false;
            }
            if ( isColMatch ) {
                for ( int k = 0; k < rows; k++ ) pattern[k][j] = 0;
            }
        }
        // Did we clear the whole thing?
        int sum = 0;
        for ( int i = 0; i < rows; i++ )
            for ( int j = 0; j < cols; j++ ) 
                sum += pattern[i][j];
        if ( sum == 0 )
            return "YES";
    }

    return "NO";
}
