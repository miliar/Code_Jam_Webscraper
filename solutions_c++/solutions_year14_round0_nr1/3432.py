#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;

int T;
int cards_1[10][10];
int cards_2[10][10];
int row_1, row_2;

int main(){

   ifstream in("A.in");
   ofstream out("Solution A.out");

   in >> T;

   for (int t=1; t <= T; t++){
      in >> row_1;

      for (int i=1; i <= 4; i++)
         for (int j=1; j <= 4; j++)
            in >> cards_1[i][j];

      in >> row_2;

      for (int i=1; i <= 4; i++)
         for (int j=1; j <= 4; j++)
            in >> cards_2[i][j];

      int R = 0, rep = 0; //rep = cant de repetidos


      for (int i=1; i <= 4; i++)
         for (int j=1; j <= 4; j++)
            if (cards_1[row_1][i] == cards_2[row_2][j]){
               R = cards_1[row_1][i];
               rep++;
            }

      if (rep == 1)
         out << "Case #" << t << ": " << R << endl;
      else if (rep > 1)
         out << "Case #" << t << ": " << "Bad magician!" << endl;
      else
         out << "Case #" << t << ": " << "Volunteer cheated!" << endl;

   }

   in.close();
   out.close();

return 0;
}//FIN
