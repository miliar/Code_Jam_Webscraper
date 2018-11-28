#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string.h>

using namespace std;

void error( const char *str)
{
    cout << str;

    exit( 1);
}

int main()
{
    ifstream input( "input.txt");

    if ( !input )
        error( "Cannot open input file");

    ofstream output( "output.txt");

    if ( !output )
        error( "Cannot open output file");

    int num_cases;

    input >> num_cases;

    for ( int i = 0; i < num_cases; i++ )
    {
        int first_ans = -1, second_ans = -1;
        int first[4][4], second[4][4];

        memset( first, 0, sizeof( first));
        memset( second, 0, sizeof( second));
        input >> first_ans;

        for ( int j = 0; j < 4; j++ )
            for ( int k = 0; k < 4; k++ )
                input >> first[j][k];

        input >> second_ans;

        for ( int j = 0; j < 4; j++ )
            for ( int k = 0; k < 4; k++ )
                input >> second[j][k];

        int result = 0;

        output << "Case #" << i + 1 << ": ";

        for ( int j = 0; j < 4; j++ )
            for ( int k = 0; k < 4; k++ )
                if ( first[first_ans - 1][j] == second[second_ans - 1][k] )
                {
                    if ( result )
                        result = -1;
                    else
                        result = first[first_ans - 1][j];
                }

        if ( result == -1 )
            output << "Bad magician!";
        else if ( !result )
            output << "Volunteer cheated!";
        else
            output << result;

        output << "\n";
    }
    return 0;
}
