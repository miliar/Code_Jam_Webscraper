#include <iostream>
#include "board.h"
using namespace std;

// 'Val' appended to make code more readable
enum result_t {inconclusiveVal = 0, xVal, oVal, fullVal};

Board::Board(char data[4][4]){
  for(int i = 0 ; i < HEIGHT ; i++)
    for(int j = 0 ; j < WIDTH ; j++)
      board[i][j] = data[i][j];
}

Board::Board(){
}

void Board::printBoard(){
  for(int i = 0 ; i < HEIGHT ; i++){
    for(int j = 0 ; j < WIDTH ; j++)
      cout << board[i][j];
    cout << endl;
  }
}

void Board::buildBoard(char data[4][4]){
  for(int i = 0 ; i < HEIGHT ; i++)
    for(int j = 0 ; j < WIDTH ; j++)
      board[i][j] = data[i][j];
}

int Board::checkWin(){
  int result = checkCols();
  if(!result)
    result = checkRows();
  if(!result)
    result = checkDiags();
  if(!result && checkFull())
    result = fullVal;

  return result;
}

bool Board::checkFull(){
  for(int i = 0 ; i < HEIGHT ; i++)
    for(int j = 0 ; j < HEIGHT ; j++)
      if(board[i][j] == '.')
        return false;
  return true;
}

int Board::checkCols(){
  int val;
  for(int i = 0 ; i < WIDTH ; i++){
    val = checkOneCol(i);
    if(val > 0)
      return val;
  }
  return 0;
}

int Board::checkOneCol(int colNum){
  int xs = 0;
  int os = 0;

  for(int i = 0 ; i < HEIGHT ; i++){
    if(board[colNum][i] == '.')
      return inconclusiveVal;
    if(board[colNum][i] == 'X' || board[colNum][i] == 'T')
      xs++;
    if(board[colNum][i] == 'O' || board[colNum][i] == 'T')
      os++;
  }
  if (xs == 4)
    return xVal;
  if (os == 4)
    return oVal;
  return inconclusiveVal;
}

int Board::checkRows(){
  int val;
  for(int i = 0 ; i < HEIGHT; i++){
    val = checkOneRow(i);
    if (val > 0)
      return val;
  }
  return 0;
}

int Board::checkOneRow(int rowNum){
  int xs = 0;
  int os = 0;

  for(int i = 0 ; i < HEIGHT ; i++){
    if(board[i][rowNum] == '.')
      return inconclusiveVal;
    if(board[i][rowNum] == 'X' || board[i][rowNum] == 'T')
      xs++;
    if(board[i][rowNum] == 'O' || board[i][rowNum] == 'T')
      os++;
  }
  if (xs == 4)
    return xVal;
  if (os == 4)
    return oVal;
  return inconclusiveVal;
}

int Board::checkDiags(){
  int result = checkLeftDiag();
  if(!result)
    result = checkRightDiag();
  return result;
}

int Board::checkLeftDiag(){
  int xs = 0;
  int os = 0;

  for(int i = 0 ; i < HEIGHT ; i++){
    if(board[i][i] == '.')
      return inconclusiveVal;
    if(board[i][i] == 'X' || board[i][i] == 'T')
      xs++;
    if(board[i][i] == 'O' || board[i][i] == 'T')
      os++;
  }

  if (xs == 4)
    return xVal;
  if (os == 4)
    return oVal;
  return inconclusiveVal;
}

int Board::checkRightDiag(){
  int xs = 0;
  int os = 0;

  for(int i = 0 ; i < HEIGHT ; i++){
    if(board[i][3-i] == '.')
      return inconclusiveVal;
    if(board[i][3-i] == 'X' || board[i][3-i] == 'T')
      xs++;
    if(board[i][3-i] == 'O' || board[i][3-i] == 'T')
      os++;
  }
  if (xs == 4)
    return xVal;
  if (os == 4)
    return oVal;
  return inconclusiveVal;
}
