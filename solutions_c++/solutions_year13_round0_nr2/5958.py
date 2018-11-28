#include <iostream>
#include <iomanip>
#include <string.h>

using namespace std;

bool checkRow(int lawn[100][100], int row, int m, int height)
{
   for(int i = 0; i < m; i++)
   {
      if(lawn[row][i] != height) return false;
   }
   return true;
}
bool checkColum(int lawn[100][100], int col, int n, int height)
{
   for(int i = 0; i < n; i ++)
   {
      if(lawn[i][col] != height) return false;
   }
   return true;
}

string checkBoard(int lawn[100][100], int n, int m)
{
   bool row, col;
   for(int x = 1; x < 2; x++)
   {
      for(int i = 0; i < n; i++)
      {
         for(int j = 0; j < m; j++)
         {
            if(lawn[i][j] == x)
            {
               row = checkRow(lawn, i, m, x);
               col = checkColum(lawn, j, n, x);
               if(row == false && col == false) return "NO";
            }
         }
      }
   }
   return "YES";
}

int main()
{
   int testCases = 0, n, m;
   cin >> testCases;
   string message;
   int lawn[100][100];
   for(int i = 0; i < testCases; i++)
   {
      cin >> n;
      cin >> m;
      for(int j = 0; j < n; j++)
      {
         for(int k = 0; k < m; k++)
         {
            cin >> lawn[j][k];
         }
      }
      message = checkBoard(lawn, n, m);

      cout << "Case #" << i+1 << ": " << message << endl;
   }

   return 0;
}
