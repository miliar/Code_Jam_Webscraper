#include <iostream>

using namespace std;

/*
 * 0 = No wins
 * 1 = O wins
 * 2 = X wins
 */

int check_diagonals(char** board){
  //Check top_left->bottom_right diagonal
  bool win = true;
  //Get the first element
  char element = 'N';
  for(int i=0, j=0; i<4; ++i, ++j){
    //If there's a dot, then surely no wins here
    if(board[i][j] == '.'){ 
      win = false;
      break;
    }

    //If it's a T, it doesn't concern us
    if(board[i][j] == 'T')
      continue;

    //If it's something else
    if(element == 'N')
      element = board[i][j];
    else
      if(board[i][j] == element)
	continue;
      else{
	win = false;
	break;
      }
  }

  //If there's a win there, return it
  if(win == true){
    if(element == 'O')
      return 1;
    else
      return 2;
  }

  //Check bottom_left->top_right diagonal
  win = true;
  //Get the first element
  element = 'N';
  for(int i=3, j=0; j<4; --i, ++j){
    //If there's a dot, then surely no wins here
    if(board[i][j] == '.'){ 
      win = false;
      break;
    }

    //If it's a T, it doesn't concern us
    if(board[i][j] == 'T')
      continue;

    //If it's something else
    if(element == 'N')
      element = board[i][j];
    else
      if(board[i][j] == element)
	continue;
      else{
	win = false;
	break;
      }
  }

  //If there's a win there, return it
  if(win == true){
    if(element == 'O')
      return 1;
    else
      return 2;
  }  
  else
    return 0;
}

int check_rows(char** board, bool &has_spots){
  bool win;
  char element;

  for(int i=0; i<4; ++i){
    win = true;
    element = 'N';
    for(int j=0; j<4; ++j){
      //If there's a dot, then surely no wins here
      if(board[i][j] == '.'){ 
	win = false;
	has_spots = true;
	break;
      }

      //If it's a T, it doesn't concern us
      if(board[i][j] == 'T')
	continue;

      //If it's something else
      if(element == 'N')
	element = board[i][j];
      else
	if(board[i][j] == element)
	  continue;
	else{
	  win = false;
	  break;
	}
    }
    //If we've found a win, return it
    if(win == true){
    if(element == 'O')
      return 1;
    else
      return 2;
    }  
  }

  //If we've found no wins, return 0
  return 0;
}

int check_cols(char** board, bool &has_spots){
  bool win;
  char element;

  for(int j=0; j<4; ++j){
    win = true;
    element = 'N';
    for(int i=0; i<4; ++i){
      //If there's a dot, then surely no wins here
      if(board[i][j] == '.'){ 
	win = false;
	has_spots = true;
	break;
      }

      //If it's a T, it doesn't concern us
      if(board[i][j] == 'T')
	continue;

      //If it's something else
      if(element == 'N')
	element = board[i][j];
      else
	if(board[i][j] == element)
	  continue;
	else{
	  win = false;
	  break;
	}
    }
    //If we've found a win, return it
    if(win == true){
    if(element == 'O')
      return 1;
    else
      return 2;
    }  
  }

  //If we've found no wins, return 0
  return 0;
}

int main(){
  //Number of test cases
  int T;
  cin >> T;
  
  //Whether it has empty spaces or not
  bool spots = false;

  //Board
  char** board = new char*[4];
  for(int i=0; i<4; ++i) board[i] = new char[4];

  //Results
  int result;

  //For each test case
  for(int i=0; i<T; ++i){
    cout << "Case #" << i+1 << ": ";
    //Read the board
    for(int j=0; j<4; ++j)
      for(int k=0; k<4; ++k)
	cin >> board[j][k];

    //Assume it doesn't have any empty spots
    spots = false;

    //Check for wins
    result = check_diagonals(board);
    if(result == 1){
      cout << "O won" << endl;
      continue;
    }
    if(result == 2){
      cout << "X won" << endl;
      continue;
    }
   
    result = check_rows(board, spots);
    if(result == 1){
      cout << "O won" << endl;
      continue;
    }
    if(result == 2){
      cout << "X won" << endl;
      continue;
    }    

    result = check_cols(board, spots);
    if(result == 1){
      cout << "O won" << endl;
      continue;
    }
    if(result == 2){
      cout << "X won" << endl;
      continue;
    }

    //If we haven't found a win yet, we're here, check if it's full
    if(spots == false)
      cout << "Draw" << endl;
    else
      cout << "Game has not completed" << endl;
    
  }

  //Free the memory
  for(int i=0; i<4; ++i) delete(board[i]);
  delete(board);
}
