#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

const int MAX = 100;

int X, Y, lawn[MAX][MAX];
int orig[MAX][MAX];

bool cut(int a)   {
   int m = 0;
   bool ret = false;
   for(int i = 0; i < Y; i++) {
      if(lawn[a][i] > m)   m = lawn[a][i];
   }

   for(int i = 0; i < Y; i++) {
      if(orig[a][i] > m)  {
         ret = true;
         orig[a][i] = m;
      }
   }
   return ret;
}

bool cut2(int a)  {
   int m = 0;
   bool ret = false;
   m = 0;
   for(int i = 0; i < X; i++) {
      if(lawn[i][a] > m)   m = lawn[i][a];
   }
   for(int i = 0; i < X; i++) {
      if(orig[i][a] > m)  {
         ret = true;
         orig[i][a] = m;
      }
   }
   return ret;
}

void findSol(int c)  {
   string print = "YES";
   for(int i = 0; i < X; i++)
      for(int j = 0; j < Y; j++)
         orig[i][j] = 100;

   bool again = true;
   bool tmp;
   while(again)   {
      again = false;
      for(int i = 0; i < X; i++) {
         tmp = cut(i);
         if(!again)  again = tmp;
      }
      for(int i = 0; i < Y; i++) {
         tmp = cut2(i);
         if(!again)  again = tmp;
      }
   }

   for(int i = 0; i < X; i++) {
      for(int j = 0; j < Y; j++) {
         if(orig[i][j] != lawn[i][j])
            print = "NO";
      }
   }
   cout <<"Case #" << c <<": " << print <<"\n";
}

int main(int argc, char* argv[]) {
   int tests;
   int i, j, k, l, m;

   cin >> tests;
   for(i = 0; i < tests; i++) {
      cin >> X >> Y;
      for(j = 0; j < X; j++)  {
         for(k = 0; k < Y; k++)  {
            cin >> lawn[j][k];
         }
      }
      findSol(i+1);
   }
   return 0;
}
