//
//  Google Code Jam - 2013
//  Problem: Tic-Tac-Toe-Tomek
//  main.cpp
//  Created by Fielding Johnston on 4/13/13.

#include <iostream>
#include <assert.h>
#include <vector>

bool didPlayerWin( char c, char board[4][4] );
bool hasEmptySpace( char board[4][4] );


int main( int argc, const char * argv[] )
{
  int  n_test_cases;     // the number of test cases
  char newline;          // janky way to eat the newline char

  // get the number of test cases
  scanf("%d", &n_test_cases);  
  //std::cout<<"Test Cases: "<<n_test_cases<<std::endl;
  
  // create game board for each test case that represents the 4x4 board grid
  char board[n_test_cases][4][4];
  
  //std::cout<<"Input:"<<std::endl;
  // load each case data in to a 3d array
  for ( int i = 0; i < n_test_cases; i++ )
  {
    //std::cout<<std::endl<< "Case "<< i <<": "<<std::endl<<std::endl;
    
    scanf("%c", &newline);  // eat the new line character
    for ( int row = 0; row < 4; row++ )
    {
      for ( int col = 0; col < 4; col++)
      {
        char c;
        scanf("%c", &c );
        board[i][row][col] = c;
      }
      scanf("%c", &newline);  // eat the new line character
      // std::cout<<board[i][row][0]<<board[i][row][1]<<board[i][row][2]<<board[i][row][3]<<std::endl;
    }
  }
  
  // std::cout<<std::endl<<"Output:"<<std::endl;
  for ( int test_case = 0; test_case < n_test_cases; test_case++ )
  {
    std::cout<<"Case #"<<(test_case + 1)<<": ";
    
    if ( didPlayerWin( 'X', board[test_case] ) )          // test if X won
    {
      std::cout<<"X won"<<std::endl;
    }
    else if ( didPlayerWin( 'O', board[test_case] ) )     // test if 0 won
    {
      std::cout<<"O won"<<std::endl;
    }
    else            // neither side has won yet, test if the game has completed
    {
      if ( hasEmptySpace( board[test_case] ) )  // check if there are any open slots left
      {
      std::cout<<"Game has not completed"<<std::endl;
      } else  // no spots left, it was a draw
      {
      std::cout<<"Draw"<<std::endl;
      }
    }
  }
  return 0;
}


bool didPlayerWin ( char c, char board[4][4] )
{
  // test for horizontal line win
  for ( int row = 0; row < 4; row++ )
  {
    int count = 0;
    for ( int col = 0; col < 4; col++ )
    {
      if ( board[row][col] == 'T' || board[row][col] ==  c ) count++;
    }

    if ( count == 4)  return true;
  }
  
  // test for vertical line win
  for ( int col = 0; col < 4; col++ )
  {
    int count = 0;
    for( int row = 0; row < 4; row++ )
    {
      if( board[row][col] == 'T' || board[row][col] == c ) count++;
    }
    
    if ( count == 4 ) return true;
  }

  // test for diagonal from top left to bottom right
  
    if ( board[0][0] == 'T' || board[0][0] == c )
    {
      if ( board[1][1] == 'T' || board[1][1] == c )
      {
        if ( board[2][2] == 'T' || board[2][2] == c )
        {
          if ( board[3][3] == 'T' || board[3][3] == c ) return true;
        }
      }
    }
  
  // test for diagonal from bottom left to top right
  if ( board[3][0] == 'T' || board[3][0] == c )
  {
    if ( board[2][1] == 'T' || board[2][1] == c )
    {
      if ( board[1][2] == 'T' || board[1][2] == c )
      {
        if ( board[0][3] == 'T' || board[0][3] == c ) return true;
      }
    }
  }
  
  // if we haven't returned true at this point, then neither player has won
  return false;
}

bool hasEmptySpace( char board[4][4] )
{
  for ( int row = 0; row < 4; row++ )
  {
    for ( int col = 0; col < 4; col++ )
    { 
      if ( board[row][col] == '.') return true; // we found an empty space return true
    }
  }
  return false; // we haven't found an empty space return false
}

