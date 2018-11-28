#include <fstream>
#include <cstdlib>
#include <iostream>
using namespace std;

bool isSpaceOfPlayer( char space, char player )
{
  if( space == 'T' )
  {
    return true;
  }
  if( space == player )
  {
    return true;
  }
  return false;
}

char wins( char a, char b, char c, char d )
{
  char player = 'X';
  for( int i = 0; i < 2; i++ )
  {
    if( isSpaceOfPlayer( a, player ) && isSpaceOfPlayer( b, player ) &&
      isSpaceOfPlayer( c, player ) && isSpaceOfPlayer( d, player ) )
    {
      return player;
    }
    player = 'O';
  }
  return '\0';
}

int main()
{
  ifstream fin("largeInput.in");
  ofstream fout("largeOutput.txt");
  char board[4][4];
  unsigned long T;
  fin >> T;

  for( unsigned long i = 1; i <= T; i++ )
  {
    bool gameOver = true;
    for( int j = 0; j < 4; j++ )
    {
      for( int k = 0; k < 4; k++ )
      {
        fin >> board[j][k];
        if( board[j][k] == '.' )
        {
          gameOver = false;
        }
      }
    }
    fout << "Case #" << i << ": ";

    bool done = false;
    for( int j = 0; j < 4 && !done; j++ )
    {
      char winner = wins( board[j][0], board[j][1], board[j][2], board[j][3] );
      if( winner != '\0' )
      {
        done = true;
        fout << winner << " won";
      }
      else
      {
        winner = wins( board[0][j], board[1][j], board[2][j], board[3][j] );
        if( winner != '\0' )
        {
          done = true;
          fout << winner << " won";
        }
      }
    }
    if(!done)
    {
      char winner = wins( board[0][0], board[1][1], board[2][2], board[3][3] );
      if( winner != '\0' )
      {
        done = true;
        fout << winner << " won";
      }
      else
      {
        winner = wins( board[3][0], board[2][1], board[1][2], board[0][3] );
        if( winner != '\0' )
        {
          done = true;
          fout << winner << " won";
        }
      }
    }
    if(!gameOver && !done)
    {
      fout << "Game has not completed";
    }
    else if(gameOver && !done)
    {
      fout << "Draw";
    }
    if( i != T )
    {
      fout << endl;
    }
  }
  fin.close();
  fout.close();
  return 0;
}