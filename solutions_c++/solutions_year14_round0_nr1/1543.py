#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
   int t;
   cin >> t;
   for(int i = 1; i <= t; ++i){
      int la, ma[5][5];
      cin >> la;
      for(int j = 1; j <= 4; ++j)
         for(int k = 1; k <= 4; ++k)
            cin >> ma[j][k];
      bool cand[20] = {false};
      for(int j = 1; j <= 4; ++j)
         cand[ ma[la][j] ] = true;
      cin >> la;
      for(int j = 1; j <= 4; ++j)
         for(int k = 1; k <= 4; ++k)
            cin >> ma[j][k];
      int ans, ansc = 0;
      for(int j = 1; j <= 4; ++j)
         if(cand[ ma[la][j] ]){
            ans = ma[la][j];
            ++ansc;
         }
      cout << "Case #" << i << ": ";
      if(ansc == 1)
         cout << ans << endl;
      else if(ansc == 0)
         cout << "Volunteer cheated!" << endl;
      else
         cout << "Bad magician!" << endl;
   }
   
   
   return 0;
}

