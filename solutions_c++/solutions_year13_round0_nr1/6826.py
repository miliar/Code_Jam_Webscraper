//Shreyas Garg
//Tic-Tac-Toe-Tomek
//Large Input
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
   char arrX[4][4];
   char arrO[4][4];
   using namespace std;
   int draw()
   {
      for(int x = 0; x < 4; x++)
         for(int y = 0; y < 4; y++)
            if(arrX[x][y] == '.')
               return 0;
      return 1;
   }
   int checkX()
   {
      int ans = 1;
      for(int x = 0; x < 4; x++)
      {
         for(int y = 0; y < 4; y++)
         {
            if(arrX[x][y] != 'X')
               ans = 0;
         }
         if(ans == 1)
            return 1;
         else
            ans = 1;
      }
      ans = 1;
      for(int x = 0; x < 4; x++)
      {
         for(int y = 0; y < 4; y++)
         {
            if(arrX[y][x] != 'X')
               ans = 0;
         }
         if(ans == 1)
            return 1;
         else
            ans = 1;
      }
      if(arrX[0][0] == 'X' && arrX[1][1] == 'X' && arrX[2][2] == 'X' && arrX[3][3] == 'X')
         return 1;
      if(arrX[0][3] == 'X' && arrX[1][2] == 'X' && arrX[2][1] == 'X' && arrX[3][0] == 'X')
         return 1;
      return 0;
   }
   int checkO()
   {
      int ans = 1;
      for(int x = 0; x < 4; x++)
      {
         for(int y = 0; y < 4; y++)
         {
            if(arrO[x][y] != 'O')
               ans = 0;
         }
         if(ans == 1)
            return 1;
         else
            ans = 1;
      }
      ans = 1;
      for(int x = 0; x < 4; x++)
      {
         for(int y = 0; y < 4; y++)
         {
            if(arrO[y][x] != 'O')
               ans = 0;
         }
         if(ans == 1)
            return 1;
         else
            ans = 1;
      }
      ans = 1;
      if(arrO[0][0] == 'O' && arrO[1][1] == 'O' && arrO[2][2] == 'O' && arrO[3][3] == 'O')
         return 1;
      if(arrO[0][3] == 'O' && arrO[1][2] == 'O' && arrO[2][1] == 'O' && arrO[3][0] == 'O')
         return 1;
      return 0;
      return 0;
   }
   int main()
   {
      ifstream fin ("input.in");
      ofstream fout("output.out");
      int N;
      fin >> N;
      for(int x = 1; x <= N; x++)
      {
         for(int y = 0; y < 4; y++)
            for(int z = 0; z < 4; z++)
            {
               char c;
               fin >> c;
               if(c == 'T')
               {
                  arrX[y][z] = 'X';
                  arrO[y][z] = 'O';
               }
               else
               {
                  arrX[y][z] = c;
                  arrO[y][z] = c;
               }
            }
      //          for(int y = 0; y < 4; y++)
      //          {
      //             for(int z = 0; z < 4; z++)
      //                cout << arrX[y][z];
      //             cout << "\n";
      //          }
         if(checkX() == 1)
            fout << "Case #" << x << ": X won" << "\n";
         else if(checkO() == 1)
            fout << "Case #" << x << ": O won" << "\n";
         else if(draw() == 1)
            fout << "Case #" << x << ": Draw" << "\n";
         else
            fout << "Case #" << x << ": Game has not completed" << "\n";
      }
   }