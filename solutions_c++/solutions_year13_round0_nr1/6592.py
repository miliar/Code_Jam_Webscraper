#include <iostream>
#include <string>

using namespace std;

enum State
{
  X, O, EMPTY, T
};

void getField(State field[4][4])
{
  char c;
  
  for(int i=0; i < 4; ++i)
  {
    for(int j=0; j < 4; ++j)
    {
      cin >> c;
      
      switch(c)
      {
      case 'X':
        field[i][j] = X;
        break;
        
      case 'O':
        field[i][j] = O;
        break;
        
      case '.':
        field[i][j] = EMPTY;
        break;
        
      case 'T':
        field[i][j] = T;
        break;
        
      default:
        --j;
        continue;
      }
    }
  }
}

bool checkWin(State s, State field[4][4])
{
  // horizontal
  for(int i=0; i < 4; ++i)
  {
    bool win = true;
    
    for(int j=0; j < 4; ++j)
    {
      if(field[i][j] != s && field[i][j] != T)
      {
        win = false;
      }
    }
    
    if(win)
    {
      return true;
    }
  }
  
  // vertical
  for(int j=0; j < 4; ++j)
  {
    bool win = true;
    
    for(int i=0; i < 4; ++i)
    {
      if(field[i][j] != s && field[i][j] != T)
      {
        win = false;
      }
    }
    
    if(win)
    {
      return true;
    }
  }
  
  // diagonal 1
  if((field[0][0] == s || field[0][0] == T)
      && (field[1][1] == s || field[1][1] == T)
      && (field[2][2] == s || field[2][2] == T)
      && (field[3][3] == s || field[3][3] == T))
  {
    return true;
  }
  
  // diagonal 2
  if((field[0][3] == s || field[0][3] == T)
      && (field[1][2] == s || field[1][2] == T)
      && (field[2][1] == s || field[2][1] == T)
      && (field[3][0] == s || field[3][0] == T))
  {
    return true;
  }
  
  return false;
}

bool hasEmpty(State field[4][4])
{
  for(int i=0; i < 4; ++i)
  {
    for(int j=0; j < 4; ++j)
    {
      if(field[i][j] == EMPTY)
      {
        return true;
      }
    }
  }
  
  return false;
}

int main()
{
  int T;
  cin >> T;
  
  for(int t=0; t < T; ++t)
  {
    State field[4][4];
    getField(field);
    
    string output;
    
    if(checkWin(X, field))
    {
      output = "X won";
    }
    else if(checkWin(O, field))
    {
      output = "O won";
    }
    else if(hasEmpty(field))
    {
      output = "Game has not completed";
    }
    else
    {
      output = "Draw";
    }
    
    
    cout << "Case #" << t+1 << ": " << output << endl;
  }

  return 0;
}
