#include <stdio.h>
#include <stdint.h>
#include <cstring>
#include <iostream>
#include <math.h>

using namespace std;

int status(char game[5][5])
{
  int winner = -1;
  bool board_filled = true;
  
  for (int i=0; i<4; ++i)
  {
    for (int j=0; j<4; ++j)
    {
      char s = game[i][j];
      if (s == '.')
      {
        board_filled = false;
        continue;
      } else if (i==0 || j==0)
      {
        int xcount=0, ocount=0, scount=0;
        
        //Horizontally
        if (i == 0)
          for (int k=0; k<4; ++k)
            if (game[i+k][j] == 'X')
              xcount++;
            else if (game[i+k][j] == 'O')
              ocount++;
            else if (game[i+k][j] == '.')
              scount++;
         if (scount == 0 && ocount == 0 && xcount>0)
         {
           winner = 0;
           break;
         } else if (scount == 0 && ocount > 0 && xcount==0)
         {
            winner = 1;
            break;
         }
         
        //Vertically
        xcount=0, ocount=0, scount=0;
        if (j == 0)
          for (int k=0; k<4; ++k)
            if (game[i][j+k] == 'X')
              xcount++;
            else if (game[i][j+k] == 'O')
              ocount++;
            else if (game[i][j+k] == '.')
              scount++;
         if (scount == 0 && ocount == 0 && xcount>0)
         {
           winner = 0;
           break;
         } else if (scount == 0 && ocount > 0 && xcount==0)
         {
            winner = 1;
            break;
         }
         
        //Diagonally
        xcount=0, ocount=0, scount=0;
        if (i==0 && j == 0)
          for (int k=0; k<4; ++k)
            if (game[i+k][j+k] == 'X')
              xcount++;
            else if (game[i+k][j+k] == 'O')
              ocount++;
            else if (game[i+k][j+k] == '.')
              scount++;
         if (scount == 0 && ocount == 0 && xcount>0)
         {
           winner = 0;
           break;
         } else if (scount == 0 && ocount > 0 && xcount==0)
         {
            winner = 1;
            break;
         }
         
         //Diagonally
        xcount=0, ocount=0, scount=0;
        if (i==0 && j == 3)
          for (int k=0; k<4; ++k)
            if (game[i+k][j-k] == 'X')
              xcount++;
            else if (game[i+k][j-k] == 'O')
              ocount++;
            else if (game[i+k][j-k] == '.')
              scount++;
         if (scount == 0 && ocount == 0 && xcount>0)
         {
           winner = 0;
           break;
         } else if (scount == 0 && ocount > 0 && xcount==0)
         {
            winner = 1;
            break;
         }

      }
     }
     
     if (winner >=0) break;
    }
  
  if (winner == 0)
    return 0;
  else if (winner == 1)
    return 1;
  else if (board_filled)
    return 2;
  
  return 3;
}

int main(int argc, char **argv)
{
  int ncases = 0;
  cin >> ncases;
  
  for (int c=1; c<=ncases; ++c)
  {
    char game[5][5];
    for (int k=0; k<4; ++k)
      cin >> game[k];
    
    int res = status(game);
    
    if (res==0) printf("Case #%d: X won\n", c);
    else if (res==1) printf("Case #%d: O won\n", c);
    else if (res==2) printf("Case #%d: Draw\n", c);
    else if (res==3) printf("Case #%d: Game has not completed\n", c);
  }
}
