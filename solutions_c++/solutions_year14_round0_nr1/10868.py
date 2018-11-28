#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main( int argc, char *argv[] ) {
    ifstream infile( "input.txt" );
    string line;                // for reading the file
    int num_cases;              // for reading the cases
    stringstream stream;        // for parsing the cases
    int before[4][4];           // first board
    int before_row;             // first row choice
    int after[4][4];            // second board
    int after_row;              // second row choice
    int i;                      // index over num cases
    int j;                      // index over num rows
    int k;                      // index over num columns
    int num_similar;            // for computing answer
    int magic_guess;            // for computing answer

    num_cases = 0;

    if ( infile.is_open() ) {
        getline( infile, line );
        stream.clear();
        stream.str( line );
        stream >> num_cases;
        //cout << "there are " << num_cases << " cases!" << endl;
        for ( i = 0; i < num_cases; i++ ) {
            // first choice
            getline( infile, line );
            //cout << "read line " << line << endl;
            stream.clear();
            stream.str( line );
            stream >> before_row;
            before_row--;   // zero-indexing
            //cout << "read before_row " << before_row << endl;
            // first board layout 
            for ( j = 0; j < 4; j++ ) {
                getline( infile, line );
                //cout << "read line " << line << endl;
                stream.clear();
                stream.str( line );
                for( k = 0; k < 4; k++ ) {
                    stream >> before[j][k];
                    //cout << "read " << before[j][k] << endl;
                }
            }
            // second choice
            getline( infile, line );
            //cout << "read line " << line << endl;
            stream.str( line );
            stream.clear();
            stream >> after_row;
            after_row--;    // zer-indexing
            //cout << "read after_row " << after_row << endl;
            // second choice layout
            for ( j = 0; j < 4; j++ ) {
                getline( infile, line );
                //cout << "read line " << line << endl;
                stream.clear();
                stream.str( line );
                for( k = 0; k < 4; k++ ) {
                    stream >> after[j][k];
                    //cout << "read " << after[j][k] << endl;
                }
            }
            // COMPUTER, GO!
            num_similar = 0;
            for ( j = 0; j < 4; j++ )
                for ( k = 0; k < 4; k++ ) {
//cout << "comparing " << before[before_row][j] << " to " << after[after_row][k] << endl;
                    if ( before[before_row][j] == after[after_row][k] ) {
                        num_similar++;
                        magic_guess = before[before_row][j];
                    }
                }

//cout << num_similar << endl;

            // results
            if ( num_similar == 0 ) {
                cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
            } else if ( num_similar == 1 ) {
                cout << "Case #" << i+1 << ": " << magic_guess << endl;
            } else {
                cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
            }
        }
    } else {
        //cout << "unable to open file" << endl;
    }

    return 0;
}
