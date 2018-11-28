// NATHAN LOIKA
// CodeJam 2013 -  Qualifier
// 4/12/2013

#include <iostream>
#include <fstream>

using namespace std;

const char X = 'X';
const char O = 'O';
const char COMMON = 'T';
const char EMPTY = '.';
ofstream out("out.txt");
ifstream in("in.txt");

int main()
{
  int cases;

  in >> cases;


  for( int i = 0; i < cases; i++ )
  {
    string line;
    char board[4][4];
    char winner = EMPTY;

    in.ignore( 500, '\n' );
    for( int j = 0; j < 4; j++ )
    {
      getline( in, line, '\n' );
      for( int k = 0; k < 4; k++ )
        board[k][j] = line[k];
    }
    //in.ignore( 500, '\n' );

    for( int j = 0; j < 4; j++ )
    {
      for( int k = 0; k < 4; k++ )
        cout << board[k][j];
      cout << endl;
    }

    // check horizontial
    for( int j = 0; j < 4 && winner == EMPTY; j++ )
    {
      bool valid = true;
      char player = board[0][j];

      if( player != EMPTY )
      {
        if( player == COMMON && board[1][j] == EMPTY )
        {
          valid = false;
        }
        else if( player == COMMON )
        {
          player = board[1][j];
        }

        for( int k = 1; k < 4 && valid; k++ )
        {
          if( board[k][j] != player && board[k][j] != COMMON )
            valid = false;
        }

        if( valid )
        {
          winner = player;
        }
      }
    }

    // check vertical
    for( int j = 0; j < 4 && winner == EMPTY; j++ )
    {
      bool valid = true;
      char player = board[j][0];

      if( player != EMPTY )
      {
        if( player == COMMON && board[j][1] == EMPTY )
        {
          valid = false;
        }
        else if( player == COMMON )
        {
          player = board[1][j];
        }

        for( int k = 1; k < 4 && valid; k++ )
        {
          if( board[j][k] != player && board[j][k] != COMMON )
            valid = false;
        }

        if( valid )
          winner = player;
      }
    }

    // check diagonal
    for( int j = 0; j < 2 && winner == EMPTY; j++ )
    {
      if( !j )
      {
        // top left to bottom right
        bool valid = true;
        char player = board[0][0];

        if( player != EMPTY )
        {
          if( player == COMMON && board[1][1] == EMPTY )
          {
            valid = false;
          }
          else if( player == COMMON )
          {
            player = board[1][1];
          }

          for( int k = 1; k < 4 && winner == EMPTY && valid; k++ )
          {
            if( board[k][k] != player && board[k][k] != COMMON )
              valid = false;
          }

          if( valid )
            winner = player;
        }
      }
      else
      {
        // top right to bottom left
        bool valid = true;
        char player = board[3][0];

        if( player != EMPTY )
        {
          if( player == COMMON && board[2][1] == EMPTY )
          {
            valid = false;
          }
          else if( player == COMMON )
          {
            player = board[2][1];
          }

          for( int k = 1; k < 4 && winner == EMPTY && valid; k++ )
          {
            if( board[3-k][k] != player && board[3-k][k] != COMMON )
              valid = false;
          }

          if( valid )
            winner = player;
        }
      }
    }

    out << "Case #" << i+1 << ": ";
    switch(winner)
    {
    case(X):
        out << "X won" << endl;
        break;
    case(O):
        out << "O won" << endl;
        break;
    default:
      bool fail = false;
      for( int j = 0; j < 4 && !fail; j++ )
        for( int k = 0; k < 4 && !fail; k++ )
          if( board[j][k] == '.' )
            fail = true;
      if( !fail )
        out << "Draw" << endl;
      else
        out << "Game has not completed" << endl;
      break;
    }

  }

  out.close();
  in.close();

  return 0;
}
