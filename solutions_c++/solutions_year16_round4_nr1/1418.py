#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
int main()
{
   int T;
   scanf("%d", &T);
   for(int _i=1; _i<=T; _i++)
   {
      int N, P, R, S;
      scanf("%d%d%d%d", &N, &R, &P, &S);
      printf("Case #%d: ",_i);

      string s[3][13];
      s[0][0] = string("P");
      s[1][0] = string("R");
      s[2][0] = string("S");

      for(int i=0; i<N; i++) {
         s[0][i+1] = min(s[0][i], s[1][i]) + max(s[0][i], s[1][i]);
         s[1][i+1] = min(s[2][i], s[1][i]) + max(s[2][i], s[1][i]);
         s[2][i+1] = min(s[0][i], s[2][i]) + max(s[0][i], s[2][i]);
      }
      bool b = true;
      /*
      cout << '\n';
      for(int i=0; i<3; i++)
            cout << s[i][N] << '\n';
      cout << '\n';
      */
      int nb[3][3];
      for(int i=0; i<3; i++)
         for(int j=0; j<3; j++)
            nb[i][j] = 0;
      for(int i=0; i<3; i++)
         for(char c : s[i][N]) {
            if(c == 'P')
              nb[i][0]++;
            if(c == 'R')
              nb[i][1]++;
            if(c == 'S')
              nb[i][2]++;
         }

      for(int i=0; i<3; i++)
         if(nb[i][0] == P && nb[i][1] == R && nb[i][2] == S){
            b = false;
            cout << s[i][N] << '\n';
         }
      if(b)
         cout << "IMPOSSIBLE\n";
   }
   return 0;
}
