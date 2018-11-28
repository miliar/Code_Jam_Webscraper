
#include <iostream>
using namespace std;


/*
Idea: it's doable IFF each square is the highest in either its row or col
*/


static int board[1000][1000];
static int nrows;
static int ncols;


// Read board
static void process_board(){

  for(int i = 0; i < nrows; i++)
    for(int j=0; j< ncols; j++){
      cin >> board[i][j];
    }
  
}


static bool compute(){

  int highest_for_row[nrows];
  int highest_for_col[ncols];


  // Initiate two arrays
  for(int row = 0; row < nrows; row++){
    int highest = 0;
    for(int col = 0; col < ncols; col++){
      int hh = board[row][col];
      if(hh > highest) highest = hh;
    }
    highest_for_row[row] = highest;
  }
  for(int col = 0; col < ncols; col++){
    int highest = 0;
    for(int row = 0; row < nrows; row++){
      int hh = board[row][col];
      if(hh > highest) highest = hh;
    }
    highest_for_col[col] = highest;
  }


  /*
  // Test correctness
  for(int row = 0; row < nrows; row++){
    cout << highest_for_row[row];
  }
  */


  for(int row = 0; row < nrows; row++){
    for(int col = 0; col < ncols; col++){
      
      int this_sq = board[row][col];

      // Check whether highest(row) > this_sq and highest(col) > this_sq
      // If both of these are true, then NO.

      if(highest_for_row[row] > this_sq &&
         highest_for_col[col] > this_sq) return false;


    }
  }

  return true;


}



int main(){
  int ncases;
  cin >> ncases;

  for(int i=0; i<ncases; i++){


    cin >> nrows;
    cin >> ncols;

    process_board();
    bool result = compute();

    cout << "Case #" << i+1 << ": " << (result?"YES":"NO") << endl;



  }

}

