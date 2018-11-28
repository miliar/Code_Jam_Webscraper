#include <iostream>
#include <string>
using namespace std;

int main ()
{
    int testCases;
    int cardSetup[4][4];
    int firstRoundRow[4];
    int guessRow;
    int winner;
    int winnerCount;
    
    cin >> testCases;
    
    for (int k = 0; k < testCases; k++)
    {
        winnerCount = 0;
        cin >> guessRow;
        
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin >> cardSetup[i][j];
            }
        }
        
        for (int i = 0; i < 4; i ++)
        {
            firstRoundRow[i] = cardSetup[guessRow-1][i];
        }
        
        cin >> guessRow;
        
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin >> cardSetup[i][j];
            }
        }
        
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (firstRoundRow[j] == cardSetup[guessRow-1][i])
                {
                    winnerCount++;
                    winner = cardSetup[guessRow-1][i];
                }
            }
        }
        
        if (winnerCount == 0)
            cout << "Case #" << k+1 << ": " << "Volunteer cheated!" << endl;
        else if (winnerCount == 1)
            cout << "Case #" << k+1 << ": " << winner << endl;
        else
            cout << "Case #" << k+1 << ": " << "Bad magician!" << endl;
    }
    
    return 0;
}
    