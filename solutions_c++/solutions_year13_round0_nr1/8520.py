#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    char grid[4][4], winner, toCompare;
    char blankChar;
    int caseNumber;
    int i, j, k;

    // Opens the input and output files
    ifstream input ("A-small-attempt0.in");
    ofstream output("output.txt");

    input >> caseNumber;
    input.get(blankChar);

    for (i = 0; i < caseNumber; i++)
    {
        output << "Case #" << caseNumber << ": ";
        winner = 0;

        // Copies the grid in memory
        for (j = 0; j < 4; j++)
        {
            for (k = 0; k < 4; k++)
            {
                input.get(grid[j][k]);
            }
            input.get(blankChar);
        }

        for(j = 0; (j < 4) && (winner == 0); j++)
        {
            if(grid[j][0] != '.')
            {
                if(grid[j][0] != 'T') toCompare = grid[j][0];
                else toCompare = grid[j][1];

                if(toCompare == '.') continue;

                for(k = 1; k < 4; k++)
                {
                    if((grid[j][k] != toCompare) && (grid[j][k] != 'T')) break;
                }
                if(k == 4) winner = toCompare;
            }
        }

        for(j = 0; (j < 4) && (winner == 0); j++)
        {
            if(grid[0][j] != '.')
            {
                if(grid[0][j] != 'T') toCompare = grid[0][j];
                else toCompare = grid[1][j];

                if(toCompare == '.') continue;

                for(k = 1; k < 4; k++)
                {
                    if((grid[k][j] != toCompare) && (grid[k][j] != 'T')) break;
                }
                if(k == 4) winner = toCompare;
            }
        }

        if((grid[0][0] != '.') && (winner == 0))
        {
            if(grid[0][0] != 'T') toCompare = grid[0][0];
            else toCompare = grid[1][1];

            if(toCompare == '.') continue;

            for(j = 1; j < 4; j++)
            {
                if((grid[j][j] != toCompare) && (grid[j][j] != 'T')) break;
            }
            if(j == 4) winner = toCompare;
        }


        if((grid[0][3] != '.') && (winner == 0))
        {
            if(grid[0][3] != 'T') toCompare = grid[0][3];
            else toCompare = grid[1][2];

            if(toCompare == '.') continue;

            for(j = 1; j < 4; j++)
            {
                if((grid[j][3 - j] != toCompare) && (grid[j][3 - j] != 'T')) break;
            }
            if(j == 4) winner = toCompare;
        }

        if(winner == 0)
        {
            for (j = 0; (j < 4) && (winner != '.'); j++)
            {
                for (k = 0; k < 4; k++)
                {
                    if (grid[j][k] == '.')
                    {
                        winner = '.';
                        break;
                    }
                }
            }
        }

        switch(winner)
        {
            case 'X':
                output << "X won" << endl;
                break;
            case 'O':
                output << "O won" << endl;
                break;
            case 0:
                output << "Draw" << endl;
                break;
            case '.':
                output << "Game has not completed" << endl;
                break;
        }

        input.get(blankChar);
    }


    return 0;
}
