//
//  main.cpp
//  Tic-Tac-Toe-Tomek
//
//  Created by Wojtek on 4/13/13.
//  Copyright (c) 2013 Wojtek. All rights reserved.
//

#define ARRAY_DIMENSION 4
#include <iostream>
#include <array>
#include <cmath>

int checkForWinner (std::array<std::array<char, ARRAY_DIMENSION>, ARRAY_DIMENSION> & table)
{
    int horizontalScore = 0, horizontalT = 0, verticalScore = 0, verticalT = 0, diagonalScore1 = 0, diagonalScore2 = 0, diagonalT1 = 0, diagonalT2 = 0;
    for (int i = 0; i < ARRAY_DIMENSION; i++)
    {
        for (int j = 0; j < ARRAY_DIMENSION; j++)
        {
            switch (table[i][j])
            {
                case 'X': horizontalScore++;
                    break;
                case 'O': horizontalScore--;
                    break;
                case 'T': horizontalT++;
            }
            
            switch (table[j][i])
            {
                case 'X': verticalScore++;
                    break;
                case 'O': verticalScore--;
                    break;
                case 'T': verticalT++;
            }
            
            if (i == j)
            {
                switch (table[i][j])
                {
                    case 'X': diagonalScore1++;
                        break;
                    case 'O': diagonalScore1--;
                        break;
                    case 'T': diagonalT1++;
                }
                
                switch (table[i][ARRAY_DIMENSION - j -1])
                {
                    case 'X': diagonalScore2++;
                        break;
                    case 'O': diagonalScore2--;
                        break;
                    case 'T': diagonalT2++;
                }
            }
        }
        
        if (abs(horizontalScore) + horizontalT == ARRAY_DIMENSION)
        {
            if (horizontalScore > 0)
            {
                return 1;
            }
            else
            {
                return -1;
            }
        }
        else if (abs(verticalScore) + verticalT == ARRAY_DIMENSION)
        {
            if (verticalScore > 0)
            {
                return 1;
            }
            else
            {
                return -1;
            }
        }
        horizontalScore = horizontalT = verticalScore = verticalT = 0;
    }
    
    if (abs(diagonalScore1) + diagonalT1 == ARRAY_DIMENSION)
    {
        if (diagonalScore1 > 0)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }
    else if (abs(diagonalScore2) + diagonalT2 == ARRAY_DIMENSION)
    {
        if (diagonalScore2 > 0)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

    
    return 0;
}

const std::string * checkForGameEnd (int winner, int boardCapacity)
{
    static const std::string output[] = {"X won", "O won", "Draw", "Game has not completed"};
    
    if (winner == 1)
    {
        return &output[0];
    }
    else if (winner == -1)
    {
        return &output[1];
    }
    else if (boardCapacity == 0)
    {
        return &output[2];
    }
    else
    {
        return &output[3];
    }
}


int main(int argc, const char * argv[])
{
    struct
    {
        std::array<std::array<char, ARRAY_DIMENSION>, ARRAY_DIMENSION> table;
        int freeSpaces;
    } gameBoard;
    
    int numberOfTests, caseNumber = 1;
    std::string input;
    const std::string * output = nullptr;
    std::cin >> numberOfTests;
    
    while (caseNumber <= numberOfTests)
    {
        gameBoard.freeSpaces = 0;
        
        for (int i = 0; i < ARRAY_DIMENSION; i++)
        {
            std::cin >> input;
            
            for (int j = 0; j < ARRAY_DIMENSION; j++)
            {
                if ((gameBoard.table[i][j] = input[j]) == '.') gameBoard.freeSpaces++;
            }
        }
        getchar();
        
        output = checkForGameEnd(checkForWinner(gameBoard.table), gameBoard.freeSpaces);
        
        std::cout << "Case #" << caseNumber << ": " << *output << std::endl;
        caseNumber++;
    }

    std::cout << std::endl;
    return 0;
}



