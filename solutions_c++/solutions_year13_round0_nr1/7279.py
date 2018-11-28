#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;
char l[4][5];
ifstream lire("input.in", ios::in);
ofstream ecrire("output.txt", ios::out);

bool check_line(char p)
{
   for (int i = 0; i < 4; i++)
   {
      int s = 0;
      for (int j = 0; j < 4; j++)
         if (l[i][j] == 'T' || l[i][j] == p)
            s += 1;
      if (s == 4)
         return true;
   }
   return false;
}

bool check_row(char p)
{
   for (int i = 0; i < 4; i++)
   {
      int s = 0;
      for (int j = 0; j < 4; j++)
         if (l[j][i] == 'T' || l[j][i] == p)
            s += 1;
      if (s == 4)
         return true;
   }
   return false;
}

bool check_diag(char p)
{
   int s = 0;
   for (int i = 0; i < 4; i++)
      if (l[i][i] == 'T' || l[i][i] == p)
         s += 1;
   if (s == 4)
      return true;
   s = 0;
   for (int i = 0; i < 4; i++)
      if (l[3 - i][i] == 'T' || l[3 - i][i] == p)
         s += 1;
   if (s == 4)
      return true;
   return false;
}

bool check_end()
{
   for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
         if (l[i][j] == '.')
            return false;
   return true;
}

int main()
{
   int N;
   lire >> N;
   for (int k = 1; k <= N; k++)
   {
      for (int i = 0; i < 4; i++)
         lire >> l[i];
      bool x = false;
      bool o = false;
      bool e = check_end();
      if (check_line('X')) x = true;
      if (check_row('X'))  x = true;
      if (check_diag('X')) x = true;
      if (check_line('O')) o = true;
      if (check_row('O'))  o = true;
      if (check_diag('O')) o = true;
      if (x)
         ecrire << "Case #" << k << ": X won" << endl;
      else if (o)
         ecrire << "Case #" << k << ": O won" << endl;
      else if (e)
         ecrire << "Case #" << k << ": Draw" << endl;
      else
         ecrire << "Case #" << k << ": Game has not completed" << endl;
   }
}
