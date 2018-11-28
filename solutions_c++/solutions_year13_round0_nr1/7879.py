#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {

  int T;
  char board[4][4], status[32];

  scanf("%d", &T); getchar();

  for(int t=1; t<=T; t++) {
    bool emptycells = false;

    //Read board
    for(int i=0; i<4; i++) {
      for(int j=0; j<4; j++) {
	board[i][j] = getchar();
	if( board[i][j] == '.' )
	  emptycells=true;
      }
      getchar(); //end of line '\n'
    }
    getchar(); //Skip the empty line after each test case

    /*for(int i=0; i<4; i++) {
      for(int j=0; j<4; j++)
	printf("%c",board[i][j]);
      printf("\n");
      }*/

    //Compute status
    status[0] = 0; //Flag

    //Diagonals
    if( (board[0][0] == 'X' || board[0][0] == 'T') &&
	(board[1][1] == 'X' || board[1][1] == 'T') &&
	(board[2][2] == 'X' || board[2][2] == 'T') &&
	(board[3][3] == 'X' || board[3][3] == 'T') )
      strcpy(status, "X won");

    if( (board[0][3] == 'X' || board[0][3] == 'T') &&
	(board[1][2] == 'X' || board[1][2] == 'T') &&
	(board[2][1] == 'X' || board[2][1] == 'T') &&
	(board[3][0] == 'X' || board[3][0] == 'T') )
      strcpy(status, "X won");

    if( (board[0][0] == 'O' || board[0][0] == 'T') &&
	(board[1][1] == 'O' || board[1][1] == 'T') &&
	(board[2][2] == 'O' || board[2][2] == 'T') &&
	(board[3][3] == 'O' || board[3][3] == 'T') )
      strcpy(status, "O won");

    if( (board[0][3] == 'O' || board[0][3] == 'T') &&
	(board[1][2] == 'O' || board[1][2] == 'T') &&
	(board[2][1] == 'O' || board[2][1] == 'T') &&
	(board[3][0] == 'O' || board[3][0] == 'T') )
      strcpy(status, "O won");

    //Rows
    for(int i=0; i<4 && !status[0]; i++) {
      int numx=0, numo=0;
      for(int j=0; j<4; j++) {
	if( board[i][j] == 'T' ) {
	  numx++;
	  numo++;
	} else if( board[i][j] == 'X' )
	  numx++;
	else if( board[i][j] == 'O' )
	  numo++;
      }

      if( numx == 4 )
	strcpy(status, "X won");
      else if( numo == 4 )
	strcpy(status, "O won");
    }

    //Columns
    for(int i=0; i<4 && !status[0]; i++) {
      int numx=0, numo=0;
      for(int j=0; j<4; j++) {
	if( board[j][i] == 'T' ) {
	  numx++;
	  numo++;
	} else if( board[j][i] == 'X' )
	  numx++;
	else if( board[j][i] == 'O' )
	  numo++;
      }
      
      if( numx == 4 )
	strcpy(status, "X won");
      else if( numo == 4 )
	strcpy(status, "O won");
    }

    if( !status[0] ) {
      if( emptycells )
	strcpy(status, "Game has not completed");
      else
	strcpy(status, "Draw");
    }

    //Print solution
    printf("Case #%d: %s\n", t, status);
  }

  return 0;
}
