#include <cstdio>

int T, t;
char board[4][10];

int check_row(int i, char p)
{
  int j;
  int count, tt;
  count = 0;
  tt = 0;
  for(j = 0; j < 4; ++j) {
    if(board[i][j] == p)
      count++;
    else if(board[i][j] == 'T')
      tt = 1;
  }
  return (count + tt) == 4;
}

int check_col(int i, char p)
{
  int j;
  int count, tt;
  count = 0;
  tt = 0;
  for(j = 0; j < 4; ++j) {
    if(board[j][i] == p)
      count++;
    else if(board[j][i] == 'T')
      tt = 1;
  }
  return (count + tt) == 4;
}

int check_dia_l(char p)
{
  int i;
  int count, tt;
  count = 0;
  tt = 0;
  for(i = 0; i < 4; ++i)
    if(board[i][i] == p)
      count ++;
    else if(board[i][i] == 'T')
      tt ++;

  return (count + tt) == 4;
}

int check_dia_r(char p)
{
  int i;
  int count, tt;
  count = 0;
  tt = 0;
  for(i = 0; i < 4; ++i)
    if(board[i][3-i] == p)
      count ++;
    else if(board[i][3-i] == 'T')
      tt ++;
  //  printf(">> %d %d\n", count, tt);
  return (count + tt) == 4;
}

int check_draw()
{
  int i, j;
  for(i = 0; i < 4; ++i)
    for(j = 0; j < 4; ++j)
      if(board[i][j] == '.')
	return 0;
  return 1;
}

main()
{
  int i, j, xx;
  scanf("%d", &T);
  for(t = 0; t < T; ++t) {
    xx = 0;

    for(i = 0; i < 4; ++i)
      scanf("%s", board[i]);
    
    printf("Case #%d: ", t+1);
    
    for(i = 0; i < 4; ++i)
      if(check_row(i, 'X')){
	printf("X won\n");
	break;
      }
      else if(check_row(i, 'O')){
	printf("O won\n");
	break;
      }
      else if(check_col(i, 'X')){
	printf("X won\n");
	break;
      }
      else if(check_col(i, 'O')){
	printf("O won\n");
	break;
      }
    
    if(i == 4) {
      if(check_dia_l('X'))
	printf("X won\n");
      else if(check_dia_l('O'))
	printf("O won\n");
      else if(check_dia_r('X'))
	printf("X won\n");
      else if(check_dia_r('O'))
	printf("O won\n");
      else 
	xx = 1;
    }    
    
    
    if(xx) {
      if(check_draw())
	printf("Draw\n");
      else
	printf("Game has not completed\n");
    }
  }
}
