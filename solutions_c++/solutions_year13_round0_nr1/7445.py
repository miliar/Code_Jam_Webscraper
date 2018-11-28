//
//  main.cpp
//  tic-tac-toe-tomek
//
//  Created by ivan on 4/12/13.
//  Copyright (c) 2013 ivan. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

#define BOARD_DIM    4
#define PLAYER_O    'O'
#define PLAYER_X    'X'
#define TOTEM_TOKEN 'T'
#define EMPTY_SLOT  '.'

enum DiagonalDirection {
    BottomLeftToTopRight,
    TopLeftToBottomRight,
};

string dumpBoard(const char board[BOARD_DIM][BOARD_DIM])
{
    string result = "";
    
    for(int i = 0; i < BOARD_DIM; i++)
    {
        for(int j = 0; j < BOARD_DIM; j++)
        {
            result += board[i][j];
        }
        
        result += "\n";
    }
    
    return result;
}

void readIntoBoard(char board[BOARD_DIM][BOARD_DIM])
{
    string line = "";
    for(int i = 0; i < BOARD_DIM; i++)
    {
        getline(cin, line, '\n');
        for(int j = 0; j < BOARD_DIM; j++ )
            board[i][j] = line[j];
    }
}

bool checkHorizontals(const char board[BOARD_DIM][BOARD_DIM], const char player_token)
{
    for(int row = 0; row < BOARD_DIM; row++)
    {
        int count = 0;
        for(int col = 0; col < BOARD_DIM; col++)
        {
            if(board[row][col] == player_token || board[row][col] == TOTEM_TOKEN)
                count++;
            else
                count = 0;
            
            if(count == BOARD_DIM)
                return true;
        }
    }
    
    return false;
}

bool checkVerticals(const char board[BOARD_DIM][BOARD_DIM], const char player_token)
{
    for(int col = 0; col < BOARD_DIM; col++)
    {
        int count = 0;
        for(int row = 0; row < BOARD_DIM; row++)
        {
            if(board[row][col] == player_token || board[row][col] == TOTEM_TOKEN)
                count++;
            else
                count = 0;
            
            if(count == BOARD_DIM)
                return true;
        }
    }
    
    return false;
}

bool checkDiagonalComponent(const char board[BOARD_DIM][BOARD_DIM], const char player_token, enum DiagonalDirection dir)
{
    int rowDir, colDir;
    int row, col;
    int count = 0;
    
    if(dir == DiagonalDirection::BottomLeftToTopRight)
    {
        rowDir = -1;
        colDir = 1;
        
        row = BOARD_DIM - 1;
        col = 0;
    }
    else //i.e. if(dir == DiagonalDirection::TopLeftToBottomRight)
    {
        rowDir = 1;
        colDir = 1;
        
        row = 0;
        col = 0;
    }
    
    while((row >= 0 && row < BOARD_DIM) && (col >= 0 && col < BOARD_DIM))
    {
        if(board[row][col] == player_token || board[row][col] == TOTEM_TOKEN)
            count++;
        else
            count = 0;
        
        if(count == BOARD_DIM)
            return true;
        
        row += rowDir;
        col += colDir;
    }
    
    return false;
}

bool checkDiagonals(const char board[BOARD_DIM][BOARD_DIM], const char player_token)
{
    return (checkDiagonalComponent(board, player_token, DiagonalDirection::TopLeftToBottomRight) ||
            checkDiagonalComponent(board, player_token, DiagonalDirection::BottomLeftToTopRight));
}

bool checkForWin(const char board[BOARD_DIM][BOARD_DIM], const char player_token)
{
    return (checkHorizontals(board, player_token) ||
            checkVerticals(board, player_token)   ||
            checkDiagonals(board, player_token));
}

bool checkDraw(const char board[BOARD_DIM][BOARD_DIM])
{
    for(int i = 0; i < BOARD_DIM; i++)
        for(int j = 0; j < BOARD_DIM; j++)
            if(board[i][j] == EMPTY_SLOT)
                return false;
    
    return true;
}


int main(int argc, const char * argv[])
{
    //First get number of test cases
    string strT;
    int T;
    
    getline(cin, strT, '\n');
    T = stoi(strT);
    
    for(int i = 0; i < T; i++)
    {
        string msg;
        char board[BOARD_DIM][BOARD_DIM];
        readIntoBoard(board);
        
        // Get next empty line
        if(i < T - 1)
            getline(cin, msg, '\n');
        
        bool pO = checkForWin(board, PLAYER_O);
        bool pX = checkForWin(board, PLAYER_X);
        
        if(pO && !pX)
            msg = "O won";
        else if(!pO && pX)
            msg = "X won";
        else if(checkDraw(board))
            msg = "Draw";
        else
            msg = "Game has not completed";
        
        printf("Case #%i: %s\n", i+1, msg.c_str());
    }
    
    return 0;
}


