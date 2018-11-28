/********************************************************
 * Compiler: gcc version 3.2.3
 * To compile: g++ tictac_large.cc -o tictac_large
 * To run: ./tictac_large <input file>
 ********************************************************/

#include <iostream>
#include <fstream>

using namespace std;

char board[4][4];

void initialize()
{
   for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
         board[i][j] = '.';
}

int analyze()
{
   int X = 0, Y = 0, T = 0, dot = 0;

   for (int i = 0; i < 4; ++i)
   {
      for (int j = 0; j < 4; ++j)
      {
         if (board[i][j] == 'X')
            ++X;
         else if (board[i][j] == 'O')
            ++Y;
         else if (board[i][j] == 'T')
            ++T;
         else if (board[i][j] == '.')
            ++dot;
      }
      if ( (X == 4) || ((X == 3) && (T == 1)))
         return 0;
      else if ( (Y == 4) || ((Y == 3) && (T == 1)))
         return 1;

      X = 0, Y = 0, T = 0;
    }

    for (int j = 0; j < 4; ++j)
    {
       for (int i = 0; i < 4; ++i)
       {
          if (board[i][j] == 'X')
            ++X;
         else if (board[i][j] == 'O')
            ++Y;
         else if (board[i][j] == 'T')
            ++T;
       }
       if ( (X == 4) || ((X == 3) && (T == 1)))
         return 0;
       else if ( (Y == 4) || ((Y == 3) && (T == 1)))
         return 1;

       X = 0, Y = 0, T = 0;
    }

    for (int i = 0, j = 0; i < 4; ++i, ++j)
    {
       if (board[i][j] == 'X')
          ++X;
       else if (board[i][j] == 'O')
          ++Y;
       else if (board[i][j] == 'T')
          ++T;
    }
    if ( (X == 4) || ((X == 3) && (T == 1)))
      return 0;
    else if ( (Y == 4) || ((Y == 3) && (T == 1)))
      return 1;

    X = 0, Y = 0, T = 0;
    for (int i = 0,j = 3; i < 4; ++i, --j)
    {
       if (board[i][j] == 'X')
          ++X;
       else if (board[i][j] == 'O')
          ++Y;
       else if (board[i][j] == 'T')
          ++T;
    }
    if ( (X == 4) || ((X == 3) && (T == 1)))
      return 0;
    else if ( (Y == 4) || ((Y == 3) && (T == 1)))
      return 1;

    if (dot == 0)
       return 2;
    else
       return 3;

}


main(char argsc, char *argv[])
{
   int tc = 0, result = -1;

   ifstream in_file;
   in_file.open(argv[1]);

   in_file >> tc;

   if (tc < 1 || tc > 1000)
      exit (0);

   int line = 0;
   while (line < tc)
   {
     initialize();
     for (int i = 0;i < 4;++i)
        for (int j = 0;j < 4;++j)
           in_file >> board[i][j];
     ++line;

     result = analyze();
     if (result == 0)
        cout << "Case #" << line << ": X won" << endl;
     else if (result == 1)
        cout << "Case #" << line << ": O won" << endl;
     else if (result == 2)
        cout << "Case #" << line << ": Draw" << endl;
     else if (result == 3)
        cout << "Case #" << line << ": Game has not completed" << endl;
     result = -1;
   }
   in_file.close();
}
