#include <iostream>

static char board[4][4];

bool check_line(int i, int j, char sign)
{
  if (i >= 4) {
    return true;
  } else if (board[i][j] == sign || board[i][j] == 'T') {      
    return check_line(i + 1, j, sign);
  }
  
  return false;
}

bool check_column(int i, int j, char sign)
{
  if (j >= 4) {
    return true;
  } else if (board[i][j] == sign || board[i][j] == 'T') {      
    return check_column(i, j + 1, sign);
  }
  
  return false;
}

bool check_diag_down(int i, int j, char sign)
{
  if (j >= 4) {
    return true;
  } else if (board[i][j] == sign || board[i][j] == 'T') {      
    return check_diag_down(i + 1, j + 1, sign);
  }
  
  return false;
}

bool check_diag_up(int i, int j, char sign)
{
  if (j >= 4) {
    return true;
  } else if (board[i][j] == sign || board[i][j] == 'T') {      
    return check_diag_up(i - 1, j + 1, sign);
  }
  
  return false;
}

int main(void)
{
  int n, t;
  std::cin >> n;

  for (t = 1; t <= n; t++) {
    /* fill the board */
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
	std::cin >> board[i][j];
      }    
    }
    
    bool x_won = false, o_won = false;

    /* check lines and columns */
    for (int k = 0; k < 4; k++) {
      if (check_line(0, k, 'O') || check_column(k, 0, 'O')) {
	std::cout << "Case #" << t << ": O won" << std::endl;
	o_won = true;
	break;
      } else if (check_line(0, k, 'X') || check_column(k, 0, 'X')) {
	std::cout << "Case #" << t << ": X won" << std::endl;
	x_won = true;
	break;
      }
    }

    if (!x_won && !o_won) {
      /* check diagonals */
      if (check_diag_down(0, 0, 'O') || check_diag_up(3, 0, 'O')) {
	std::cout << "Case #" << t << ": O won" << std::endl;
	o_won = true;
      } else if (check_diag_down(0, 0, 'X') || check_diag_up(3, 0, 'X')) {
	std::cout << "Case #" << t << ": X won" << std::endl;
	x_won = true;
      }
    }

    /* find draw or non terminated game */
    if (!x_won && !o_won) {
      bool is_completed = true;
      for (int i = 0; i < 4; i++) {
	for (int j = 0; j < 4; j++) {
	  if (board[i][j] == '.') {
	    is_completed = false;
	    i = 4;
	    break;
	  }
	}    
      }
      if (is_completed) {
	std::cout << "Case #" << t << ": Draw" << std::endl;
      } else {
	std::cout << "Case #" << t << ": Game has not completed" << std::endl;
      }
    }
    
  }

  return 0;
}
