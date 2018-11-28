#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <utility>
#include <vector>
#include <pthread.h>
#include <cstring>

#define DEB(x) std::cerr<<"TaChIdOk: "<<#x<<":("<<x<<")"<<std::endl
#include <typeinfo>
#define T_TYPE(x) DEB(typeid(x).name())
#define T_ERROR() std::cerr<<"TaChIdOk's error on"<<std::endl<<std::endl<<"\tFile: "<<std::endl<<std::endl<<"\t"<<__FILE__<<std::endl<<std::endl<<"\tLine: "<<std::endl<<std::endl<<"\t"<<__LINE__<<std::endl<<std::endl<<"\tFunction: "<<std::endl<<std::endl<<"\t"<<__PRETTY_FUNCTION__<<std::endl<<std::endl; terminate()
#define T_ERROR2(x) throw ("Error at function "+string(__PRETTY_FUNCTION__)+": "+string(x))
#define T_WARNING(x) cerr << (string("Warning at function ") + string(__PRETTY_FUNCTION__) + ": " + string(x))
#define T_SUCCESS(x) cerr<<(string(__PRETTY_FUNCTION__)+string(x))<<endl

int main(int argc, char *argv[])
{
 char filename[100];
 sprintf(filename, "output.txt");
 FILE *file_pt = fopen(filename, "w");

 unsigned ncases = 0;
 scanf("%d\n", &ncases);
 DEB(ncases);

 for (unsigned icase = 0; icase < ncases; icase++)
  {
   bool xwon = false;
   bool owon = false;
   bool draw = true;
   std::vector<std::vector<char> > board(4);
   for (unsigned i = 0; i < 4; i++)
    {
     board[i].resize(4);
     char t1,t2,t3,t4;
     // Fill the board
     scanf("%c%c%c%c\n",&t1,&t2,&t3,&t4);
     board[i][0] = t1;
     board[i][1] = t2;
     board[i][2] = t3;
     board[i][3] = t4;
    }

   // Create two different boards, one with the T changed by X and the other
   // with the T changed by O

   std::vector<std::vector<char> > boardX(4);
   std::vector<std::vector<char> > boardO(4);
   for (unsigned i = 0; i < 4; i++)
    {
     boardX[i].resize(4);
     boardO[i].resize(4);
     for (unsigned j = 0; j < 4; j++)
      {
       boardX[i][j] = board[i][j];
       boardO[i][j] = board[i][j];
       if (board[i][j] == 'T')
        {
         boardX[i][j] = 'X';
         boardO[i][j] = 'O';
        }
       else if (board[i][j] == '.')
        {
         // There is one position left, so the game is not yet finished
         draw = false;
        }
      }
    }

   // DEB("Case");
   // DEB(icase);
   // for (unsigned i = 0; i < 4; i++)
   //  {
   //   for (unsigned j = 0; j < 4; j++)
   //    {
   //     printf("%c",board[i][j]);
   //    }
   //   std::cout<<std::endl;
   //  }

   // DEB("XCase");
   // DEB(icase);
   // for (unsigned i = 0; i < 4; i++)
   //  {
   //   for (unsigned j = 0; j < 4; j++)
   //    {
   //     printf("%c",boardX[i][j]);
   //    }
   //   std::cout<<std::endl;
   //  }

   // DEB("OCase");
   // DEB(icase);
   // for (unsigned i = 0; i < 4; i++)
   //  {
   //   for (unsigned j = 0; j < 4; j++)
   //    {
   //     printf("%c",boardO[i][j]);
   //    }
   //   std::cout<<std::endl;
   //  }

   // After read the inputs then check if one of the players won
   // Check first for the "X"
   for (unsigned i = 0; i < 4; i++)
    {
     if (boardX[i][0]=='X'&&boardX[i][1]=='X'&&boardX[i][2]=='X'&&
         boardX[i][3]=='X')
      {
       xwon = true;
       break;
      }
     if (boardO[i][0]=='O'&&boardO[i][1]=='O'&&boardO[i][2]=='O'&&
         boardO[i][3]=='O')
      {
       owon = true;
       break;
      }
     if (boardX[0][i]=='X'&&boardX[1][i]=='X'&&boardX[2][i]=='X'&&
         boardX[3][i]=='X')
      {
       xwon = true;
       break;
      }
     if (boardO[0][i]=='O'&&boardO[1][i]=='O'&&boardO[2][i]=='O'&&
         boardO[3][i]=='O')
      {
       owon = true;
       break;
      }
    }

   // The diagonals
   if (boardX[0][0]=='X'&&boardX[1][1]=='X'&&boardX[2][2]=='X'&&
       boardX[3][3]=='X')
    {xwon = true;}

   if (boardX[0][3]=='X'&&boardX[1][2]=='X'&&boardX[2][1]=='X'&&
       boardX[3][0]=='X')
    {xwon = true;}

   if (boardO[0][0]=='O'&&boardO[1][1]=='O'&&boardO[2][2]=='O'&&
       boardO[3][3]=='O')
    {owon = true;}

   if (boardO[0][3]=='O'&&boardO[1][2]=='O'&&boardO[2][1]=='O'&&
       boardO[3][0]=='O')
    {owon = true;}

   if (xwon)
    {
     fprintf(file_pt,"Case #%d: X won\n",icase+1);
    }
   else if (owon)
    {
     fprintf(file_pt,"Case #%d: O won\n",icase+1);
    }
   else if (draw)
    {
     fprintf(file_pt,"Case #%d: Draw\n",icase+1);
    }
   else
    {
     fprintf(file_pt,"Case #%d: Game has not completed\n",icase+1);
    }
  }
 fclose(file_pt);
}
