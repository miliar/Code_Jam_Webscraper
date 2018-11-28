//
//  TicTacToe.cpp
//  
//
//  Created by Laszlo Majer on 4/13/13.
//
//


#include <iostream>
#include <string>


using namespace std;


// Global variables
string resultStrings[] = {"X won", "O won", "Draw", "Game has not completed"};
int xTable[4][4];
int oTable[4][4];


bool CheckTable(int table[][4])
{
    // Check diagonal:
    int res = 0;
    for (int i = 0; i < 4; ++i)
        res += table[i][i];
    if (res == 4)
        return true;
    
    res = 0;
    for (int i = 0; i < 4; ++i)
        res += table[i][3 - i];
    if (res == 4)
        return true;
    
    for (int j = 0; j < 4; ++j)
    {
        res = 0;
        for (int i = 0; i < 4; ++i)
            res += table[j][i];
        if (res == 4)
            return true;
    }
    
    for (int j = 0; j < 4; ++j)
    {
        res = 0;
        for (int i = 0; i < 4; ++i)
            res += table[i][j];
        if (res == 4)
            return true;
    }

    return false;
};


int main()
{
    int T = 0;

    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        bool isCompleted = true;
        for (int row = 0; row < 4; ++row)
        {
            for (int col = 0; col < 4; ++col)
            {
                char nextChar;
                cin >> nextChar;
                if (nextChar == 'X')
                {
                    xTable[row][col] = 1;
                    oTable[row][col] = 0;
                }
                else if (nextChar == 'O')
                {
                    xTable[row][col] = 0;
                    oTable[row][col] = 1;
                }
                else if (nextChar == 'T')
                {
                    xTable[row][col] = 1;
                    oTable[row][col] = 1;
                }
                else
                {
                    xTable[row][col] = 0;
                    oTable[row][col] = 0;
                    isCompleted = false;
                }
            }
        }
        
        int result = 0;
        if (CheckTable(xTable))
            result = 0;
        else if (CheckTable(oTable))
            result = 1;
        else if (isCompleted)
            result = 2;
        else
            result = 3;

        cout << "Case #" << i + 1 << ": " << resultStrings[result] << endl;
    }
}
