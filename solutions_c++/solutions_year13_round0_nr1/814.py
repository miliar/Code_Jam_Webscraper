#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int delta[8][2] = { {-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1} };

char t[4][5];

bool cool(int i, int j, int dir)
{
   char c = t[i][j];
   for(int k=0; k<3; k++)
   {
      i += delta[dir][0];
      j += delta[dir][1];
      if( !(0 <= i && i < 4 && 0 <= j && j < 4 && (t[i][j] == c || t[i][j] == 'T')) )
         return false;
   }
   return true;      
}

bool gagne(char c)
{
   for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
         for(int dir=0; dir<8; dir++)
            if(t[i][j] == c && cool(i, j, dir))
               return true;
   return false;
}

bool fini()
{
   for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
         if(t[i][j] == '.')
            return false;
   return true;
}

int main()
{
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      for(int i=0; i<4; i++)
         scanf("%s", t[i]);
      cout << "Case #" << test << ": ";
      if(gagne('X'))
          cout << "X won";
      else if(gagne('O'))
         cout << "O won";
      else if(fini())
         cout << "Draw";
      else
         cout << "Game has not completed";
      cout << endl;
   }
   return 0;
}