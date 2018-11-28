#include <iostream>

using namespace std;

const int ROWS = 4;
const int COLS = 4;
const char EMPTY = '.';
const char O = 'O';
const char X = 'X';
const char T = 'T';
const int OWIN = 1;
const int XWIN = -1;
const int NA = 0;

void readfile(char board[ROWS][COLS]);
void runCommandLoop(char board[ROWS][COLS]);
bool checkDraw(char board[ROWS][COLS]);
void print(char board[ROWS][COLS], int outputNum);
int checkHoriz(char board[ROWS][COLS]);
int checkWin(char board[ROWS][COLS]);
int checkVert(char board[ROWS][COLS]);
int checkNegDiag(char board[ROWS][COLS]);
int checkPosDiag(char board[ROWS][COLS]);

int main()
{
  char board[ROWS][COLS]; 
  runCommandLoop(board);
}

void runCommandLoop(char board[ROWS][COLS])
{
  int numInput, outputNum = 1;
  
  cin >> numInput;
  for(int i = 0; i < numInput; i++)
  {
    readfile(board);
    print(board, outputNum++);
  }
  
}

void readfile(char board[ROWS][COLS])
{
  char input;
  
  for(int i = 0; i < ROWS; i++)
  {
    for(int j = 0; j < COLS; j++)
    {
      cin >> input;
      board[i][j] = input;
    }
  }
  
}

bool checkDraw(char board[ROWS][COLS])
{
  for(int i = 0; i < ROWS; i++)
  {
    for(int j = 0; j < COLS; j++)
    {
      if(board[i][j] == EMPTY)
      {
        return false;
      }
    }
  }
  return true;
}

int checkWin(char board[ROWS][COLS])
{
  if(checkHoriz(board) == OWIN || checkVert(board) == OWIN || checkNegDiag(board) == OWIN || checkPosDiag(board) == OWIN)
  {
    return OWIN;
  }
  else if(checkHoriz(board) == XWIN || checkVert(board) == XWIN || checkNegDiag(board) == XWIN || checkPosDiag(board) == XWIN)
  {
    return XWIN;
  }
  else
  {
    return NA;
  }
}

int checkVert(char board[ROWS][COLS])
{
  int o, x;
  
  for(int j = 0; j < COLS; j++)
  {
    o = 0;
    x = 0;
    for(int i = 0; i < ROWS; i++)
    {
      if(board[i][j] == EMPTY)
      {
        break;
      }
      if(board[i][j] == O || board[i][j] == T)
      {
        o++;
      }
      else if(o != 0 && board[i][j] == X)
      {
        break;
      }
      if(board[i][j] == X || board[i][j] == T)
      {
        x++;
      }
      else if(x != 0 && board[i][j] == O)
      {
        break;
      }
      if(o == ROWS)
      {
        return OWIN;
      }
      else if(x == ROWS)
      {
        return XWIN;
      }
    }
  }
  return NA;  
}

int checkHoriz(char board[ROWS][COLS])
{
  int o, x;
  
  for(int i = 0; i < ROWS; i++)
  {
    o = 0;
    x = 0;
    for(int j = 0; j < COLS; j++)
    {
      if(board[i][j] == EMPTY)
      {
        break;
      }
      if(board[i][j] == O || board[i][j] == T)
      {
        o++;
      }
      else if(o != 0 && board[i][j] == X)
      {
        break;
      }
      if(board[i][j] == X || board[i][j] == T)
      {
        x++;
      }
      else if(x != 0 && board[i][j] == O)
      {
        break;
      }
      if(o == COLS)
      {
        return OWIN;
      }
      else if(x == COLS)
      {
        return XWIN;
      }
    }
  }
  return NA;
}

int checkPosDiag(char board[ROWS][COLS])
{
  int i = 0, j = 3;
  int oCount = 0, xCount = 0;
  
  while(true)
  {
    if(i >= 4 || j <= -1)
    {
      break;
    }
    if(board[i][j] == O || board[i][j] == T)
    {
      oCount++;
    }
    else if(board[i][j] == X || board[i][j] == T)
    {
      xCount++;
    }
    if(oCount == 4)
    {
      return OWIN;
    }
    else if(xCount == 4)
    {
      return XWIN;
    }
    i++;
    j--;
  }
  
  return NA;
}

int checkNegDiag(char board[ROWS][COLS])
{
  int i = 0, j = 0;
  int oCount = 0, xCount = 0;
  
  while(true)
  {
    if(i >= 4 || j >= 4)
    {
      break;
    }
    if(board[i][j] == O || board[i][j] == T)
    {
      oCount++;
    }
    else if(board[i][j] == X || board[i][j] == T)
    {
      xCount++;
    }
    if(oCount == 4)
    {
      return OWIN;
    }
    else if(xCount == 4)
    {
      return XWIN;
    }
    i++;
    j++;
  }
  
  return NA;
}

void print(char board[ROWS][COLS], int outputNum)
{
  if(checkWin(board) == OWIN)
  {
    cout << "Case #" << outputNum << ": O won" << endl;
  }
  else if(checkWin(board) == XWIN)
  {
    cout << "Case #" << outputNum << ": X won" << endl;    
  }
  else if(checkDraw(board))
  {
    cout << "Case #" << outputNum << ": Draw" << endl;
  }
  else
  {
    cout << "Case #" << outputNum << ": Game has not completed" << endl;
  }
}