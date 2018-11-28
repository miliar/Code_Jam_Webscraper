#include <stdio.h>
#include <stdlib.h>

using namespace std;

void printBoard (char board[][4])
{
  for (int r = 3; r >= 0; r--) {
    for (int c = 0; c < 4; c++) {
      printf("%c", board[r][c]);
    }
    printf("\n");
  }
}

char check_columns (char board[][4])
{
  char winner = '.';
  int o_count = 0, x_count = 0;
  
  for (int c = 0; c < 4; c++) {
    for (int r = 0; r < 4; r++) {
      switch (board[r][c]) {
        case 'X':
          x_count++;
          break;
        case 'O':
          o_count++;
          break;
        case 'T':
          o_count++;
          x_count++;
      }
    }
    
    if (x_count == 4 || o_count == 4) {
      winner = (x_count == 4) ? 'X' : 'O';
    }
    x_count = 0;
    o_count = 0;
  }

  return winner;
}

char check_rows (char board[][4])
{
  char winner = '.';
  int o_count = 0, x_count = 0;
  
  for (int r = 0; r < 4; r++) {
    for (int c = 0; c < 4; c++) {
      switch (board[r][c]) {
        case 'X':
          x_count++;
          break;
        case 'O':
          o_count++;
          break;
        case 'T':
          o_count++;
          x_count++;
      }
    }
    
    if (x_count == 4 || o_count == 4) {
      winner = (x_count == 4) ? 'X' : 'O';
    }
    x_count = 0;
    o_count = 0;
  }

  return winner;
}

void count_char (char item, int& o, int& x)
{
  switch (item) {
    case 'X':
      x++;
      break;
    case 'O':
      o++;
      break;
    case 'T':
      o++;
      x++;
  }
}

char check_diagonals (char board[][4])
{
  char winner = '.';
  int o_count = 0, x_count = 0;

  count_char (board[0][0], o_count, x_count);
  count_char (board[1][1], o_count, x_count);  
  count_char (board[2][2], o_count, x_count);
  count_char (board[3][3], o_count, x_count);
  
  if (x_count == 4 || o_count == 4) {
    winner = (x_count == 4) ? 'X' : 'O';
  }
  else {
    x_count = 0;
    o_count = 0;
    
    count_char (board[0][3], o_count, x_count);
    count_char (board[1][2], o_count, x_count);  
    count_char (board[2][1], o_count, x_count);
    count_char (board[0][3], o_count, x_count);
    
    if (x_count == 4 || o_count == 4) {
      winner = (x_count == 4) ? 'X' : 'O';
    }
  }

  return winner;
}

int main (void) {

  char board[4][4];
  char winner, tmp;
  bool ongoing = false;
  int num_cases = 0;
  
  scanf ("%d", &num_cases);
  
  for (int curr_case = 1; curr_case <= num_cases; curr_case++) {
    
    ongoing = false;

    for (int r = 3; r >= 0; r--) {
      for (int c = 0; c < 4; c++) {
        do {
          scanf("%c", &tmp);
        } while (tmp == '\n');
        
        board[r][c] = tmp;
        
        if (!ongoing && tmp == '.') {
          ongoing = true;
        }
      }
    }
    
//    printf ("curr_case = %d/%d\n", curr_case, num_cases);
//    printBoard (board);
    
    winner = check_rows (board);
    if (winner != '.') {
      printf ("Case #%d: %c won\n", curr_case, winner);
    }
    else {
      winner = check_columns (board);
      if (winner != '.') {
        printf ("Case #%d: %c won\n", curr_case, winner);
      }
      else {
        winner = check_diagonals (board);
        if (winner != '.') {
          printf ("Case #%d: %c won\n", curr_case, winner);
        }
        else if (ongoing) {
          printf ("Case #%d: Game has not completed\n", curr_case);
        }
        else {
          printf ("Case #%d: Draw\n", curr_case);
        }
      }
    }
  }

  return 0;
}











