#include <iostream>
#include <stack>
#include <cstdio>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <iterator>
using namespace std;

#define A first
#define B second

int i, j, k, R, C, M, T;
char board[50][50];

int main()
{
  cin >> T;
  for (int t=1; t<=T; ++t)
  {
    cin >> R >> C >> M;
    int nEmpty = R*C - M;
    bool possible = false;
    bool rotate = false;
    if (R > C)
    {
      rotate = true;
      k = R;
      R = C;
      C = k;
    }
    int minN = R;
    for (i=0; i<R; ++i)
      for (j=0; j<C; ++j)
        board[i][j] = '*';
    cout << "Case #" << t << ":" << endl;
    k = nEmpty-1;
    if (nEmpty == 1)
    {
      possible = true;
      board[0][0] = 'c';
    }
    else if (minN == 1)
    {
      possible = true;
      board[0][0] = 'c';
      for (j=0; j<k; )
        board[0][++j] = '.';
    }
    else
    {
      if ((nEmpty & 1) == 0)
      {
        if (minN > 1 && nEmpty > 2)
        {
          possible = true;
          board[0][0] = 'c';
          if (nEmpty == 4)
            board[0][1] = board[1][1] = board[1][0] = '.';
          else
          {
            for (i=0; i<R; ++i)
              for (j=0; j<(C&254); ++j)
                if ((i != 0 || j != 0) && k-- >  0)
                  board[i][j] = '.';
            if (nEmpty == 6 && C > 3)
            {
              board[0][3] = '*';
              board[1][2] = '.';
            }
            if (k > 0)
            {
              for (i=0; i<R; ++i)
                if (k-- > 0)
                  board[i][C-1] = '.';
            }
          }
        }
      }
      else
      {
        if (nEmpty == 9)
        {
          if (minN > 2)
          {
            possible = true;
            board[0][0] = 'c';
            for (i=0; i<3; ++i)
              for (j=0; j<3; ++j)
                if ((i != 0 || j != 0) && k-- > 0)
                  board[i][j] = '.';
          }
        }
        else if (nEmpty > 10)
        {
          possible = true;
          board[0][0] = 'c';
          for (i=0; i<3; ++i)
            for (j=0; j<3; ++j)
              if ((i != 0 || j != 0) && k-- > 0)
                board[i][j] = '.';
          for (i=3; i<(R&254); ++i)
            for (j=0; j<3; ++j)
              if (board[i][j] != '.' && k-- > 0)
                board[i][j] = '.';
          for (i=0; i<3; ++i)
            for (j=3; j<(C&254); ++j)
              if (board[i][j] != '.' && k-- > 0)
                board[i][j] = '.';
          i = (R&254)-1;
          j = (C&254)-1;
          if (board[i][j] != '.' && k-- > 0)
                board[i][j] = '.';
          for (i=0; i<R; ++i)
            for (j=(C&254); j<C; ++j)
              if (board[i][j] != '.' && k-- > 0)
                board[i][j] = '.';
          for (i=(R&254); i<R; ++i)
            for (j=0; j<C; ++j)
              if (board[i][j] != '.' && k-- > 0)
                board[i][j] = '.';
          if (nEmpty == 13)
          {
            if (R == 3)
            {
              board[2][3] = '*';
              board[1][4] = '.';
            }
            else
            {
              board[3][2] = '*';
              board[1][3] = '.';
            }
          }
          else if (nEmpty == 17)
          {
            board[3][3] = '*';
            board[1][C-1] = '.';
          }
          else if (nEmpty == 21)
          {
            board[3][0] = '*';
            board[4][3] = '.';
          }
          else if (nEmpty == 23)
          {
            board[4][4] = '*';
            board[4][2] = '.';
          }
        }
      }
    }
    if (possible)
    {
      if (rotate)
      {
        for (i=0; i<C; ++i)
        {
          for (j=0; j<R; ++j)
            cout << board[j][i];
          cout << endl;
        }
      }
      else
      {
        for (i=0; i<R; ++i)
        {
          for (j=0; j<C; ++j)
            cout << board[i][j];
          cout << endl;
        }
      }
    }
    else
      cout << "Impossible\n";
  }
	return 0;
}
