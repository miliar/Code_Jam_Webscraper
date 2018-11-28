#include <iostream>

using namespace std;

int main()
{
    int cardOne[4][4];
    int cardTwo[4][4];

    int testCases = 0;

    cin >> testCases;

    int *grid = new int[testCases];
    int *solutions = new int[testCases];

    for ( int i = 0; i < testCases; ++i )
    {
        grid[i] = 0;
        solutions[i] = 0;
    }

    for ( int i = 0; i < testCases; ++i )
    {
        int rowOne = 0, rowTwo = 0;
        cin >> rowOne;
        for ( int j = 0; j < 4; ++j )
            for ( int k = 0; k < 4; ++k )
                cin >> cardOne[j][k];

        cin >> rowTwo;
        for ( int j = 0; j < 4; ++j )
            for ( int k = 0; k < 4; ++k )
                cin >> cardTwo[j][k];

        unsigned int counter = 0;

        int s = 0, p = 0;
        bool firstOc = false;
        for ( int j = 0; j < 4; ++j )
        {
            for ( int k = 0; k < 4; ++k )
            {
                if ( cardOne[rowOne - 1][j] == cardTwo[rowTwo - 1][k] )
                    counter++;


                if ( counter == 1 )
                {
                    if ( firstOc == false )
                    {
                        s = j;
                        p = k;
                        firstOc = true;
                    }
                }
                else
                {
                    s = 0;
                    p = 0;
                }
            }
        }

        grid[i] = counter;
        if ( counter == 1 )
            solutions[i] = cardOne[rowOne - 1][s];
    }

    for ( int i = 0; i < testCases; ++i )
    {
        cout << "Case #" << i+1 << ": ";
        if ( grid[i] == 0 )
            cout << "Volunteer cheated!" << endl;

        if ( grid[i] == 1 )
            cout << solutions[i] << endl;

        if ( grid[i] > 1 )
            cout << "Bad magician!" << endl;
    }

    return 0;
}
