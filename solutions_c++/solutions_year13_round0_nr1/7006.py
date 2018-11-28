#include <string.h>
#include <stdio.h>

bool checkVerticalWin(char (*gameBoard)[4][4], char player) {
  bool win = false;

  for (int i=0; i<4; i++) {
    if (((*gameBoard)[i][0] == 'T' || (*gameBoard)[i][0] == player) &&
        ((*gameBoard)[i][1] == 'T' || (*gameBoard)[i][1] == player) &&
        ((*gameBoard)[i][2] == 'T' || (*gameBoard)[i][2] == player) &&
        ((*gameBoard)[i][3] == 'T' || (*gameBoard)[i][3] == player))
    {
      return true;
    }
  }
  return false;
}

bool checkHorizontalWin(char (*gameBoard)[4][4], char player) {
  for (int i=0; i<4; i++) {
    if (((*gameBoard)[0][i] == 'T' || (*gameBoard)[0][i] == player) &&
        ((*gameBoard)[1][i] == 'T' || (*gameBoard)[1][i] == player) &&
        ((*gameBoard)[2][i] == 'T' || (*gameBoard)[2][i] == player) &&
        ((*gameBoard)[3][i] == 'T' || (*gameBoard)[3][i] == player))
    {
      return true;
    }
  }
  return false;
}

bool checkDiagonalWin(char (*gameBoard)[4][4], char player) {
  bool win = false;

  if (((*gameBoard)[0][0] == 'T' || (*gameBoard)[0][0] == player) &&
      ((*gameBoard)[1][1] == 'T' || (*gameBoard)[1][1] == player) &&
      ((*gameBoard)[2][2] == 'T' || (*gameBoard)[2][2] == player) &&
      ((*gameBoard)[3][3] == 'T' || (*gameBoard)[3][3] == player))
  {
    return true;
  }
  if (((*gameBoard)[3][0] == 'T' || (*gameBoard)[3][0] == player) &&
      ((*gameBoard)[2][1] == 'T' || (*gameBoard)[2][1] == player) &&
      ((*gameBoard)[1][2] == 'T' || (*gameBoard)[1][2] == player) &&
      ((*gameBoard)[0][3] == 'T' || (*gameBoard)[0][3] == player))
  {
    return true;
  }
  return false;
}

int main(int argc, char* argv[])
{
  int testCases = 0;
  char gameBoard[4][4];
  char lineBuffer[512];

  gets(lineBuffer);
  sscanf(lineBuffer, "%d", &testCases);

  for (int t=0; t < testCases; t++) {
    for (int i=0; i < 4; i++) {
      gets(lineBuffer);
      strncpy(gameBoard[i], lineBuffer, sizeof(gameBoard[i]));
    }
    gets(lineBuffer);

    bool o_win = checkHorizontalWin(&gameBoard, 'O') ||
                 checkVerticalWin(&gameBoard, 'O') ||
                 checkDiagonalWin(&gameBoard, 'O'); 

    bool x_win = checkHorizontalWin(&gameBoard, 'X') ||
                 checkVerticalWin(&gameBoard, 'X') ||
                 checkDiagonalWin(&gameBoard, 'X'); 

    bool game_complete = true;
    for (int i=0; i < 4; i++)
      for (int j = 0; j<4; j++)
        if (gameBoard[i][j] == '.')
          game_complete = false;
    

    printf("Case #%d: ", t+1);
    if (o_win && x_win) printf("Draw\n");
    else if (o_win && !x_win) printf("O won\n");
    else if (!o_win && x_win) printf("X won\n");
    else if (game_complete) printf("Draw\n");
    else printf("Game has not completed\n");
  }
  
  return 0;
}

