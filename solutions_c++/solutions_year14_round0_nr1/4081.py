#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      cout << "Case #" << test << ": ";
      bool t[17] = {0};
      int l;
      cin >> l;
      for(int i=1; i<=4; i++)
         for(int j=0; j<4; j++)
         {
            int n;
            cin >> n;
            if(i == l)
               t[n] = true;
         }
      int a = 0;
      cin >> l;
      for(int i=1; i<=4; i++)
         for(int j=0; j<4; j++)
         {
            int n;
            cin >> n;
            if(i == l && t[n])
               a = a == 0 ? n : -1;
         }
      if(a == -1)
         cout << "Bad magician!";
      else if(a == 0)
         cout << "Volunteer cheated!";
      else
         cout << a;
      cout << endl;
   }
   return 0;
}