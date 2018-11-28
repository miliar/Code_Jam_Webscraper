#include <iostream>
#include <stdio.h>

char board[4][4], dummy;
char* res[] = {"X won", "O won", "Draw", "Game has not completed"};
char* checkTTT()
{
  int result = -1;
  scanf("%c", &dummy);
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0 ; j < 4; j++)
    {
      scanf("%c", &board[i][j]);
      if (board[i][j] == '.')
        result = 1;
    }
    scanf("%c", &dummy);
  }
  /*//  verify input boards
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0 ; j < 4; j++)
    {
      printf("%c", board[i][j]);
    }
    printf ("\n");
  }*/
  // check rows
  for (int i = 0; i < 4; i++)
  {
    char ch = board[i][0];
    if (ch == 'T')
      ch = board[i][1];
    int j = 0;
    for (; j < 4; j++)
    {
      if ((board[i][j] != ch && board[i][j] != 'T') || board[i][j] == '.')
        break;
    }
    if ( j == 4)
      {
        if (ch == 'X')
          {
            return res[0];
          }
        else
          {
            return res[1];
          }
      }
  }

  // check columns
  for (int i = 0; i < 4; i++)
  {
    char ch = board[0][i];
    if (ch == 'T')
      ch = board[1][i];
    int j = 0;
    for (; j < 4; j++)
    {
      if ((board[j][i] != ch && board[j][i] != 'T') || board[j][i] == '.')
        break;
    }
    if ( j == 4)
      {
        if (ch == 'X')
          {
            return res[0];
          }
        else
          {
            return res[1];
          }
      }
  }

  // check diagonal1
  char ch = board[0][0];
  if (ch == 'T')
    ch = board[1][1];
  int i = 0;
  for (; i < 4; i++)
    {
      if ((board[i][i] != ch && board[i][i] != 'T') || board[i][i] == '.')
        break;
    }
  if (i == 4)
    {
        if (ch == 'X')
          {
            return res[0];
          }
        else
          {
            return res[1];
          }
    }

  // check diagonal2
  ch = board[0][3];
  if (ch == 'T')
    ch = board[1][3];
  for (i = 0; i < 4; i++)
    {
      if ((board[i][3-i] != ch && board[i][3-i] != 'T') || board[i][3-i] == '.')
        break;
    }
  if (i == 4)
    {
      if (ch == 'X')
        {
          return res[0];
        }
      else
        {
          return res[1];
        }
    }

  if (result == -1)
    {
      return res[2];
    }
  return res[3];
}

int main()
{
        int num_cases = 0;
        scanf("%d", &num_cases);


        for (int i = 0; i < num_cases; i++)
        {
            printf ("Case #%d: ", i+1);
            printf("%s\n",checkTTT());
        }
        return 0;
}

