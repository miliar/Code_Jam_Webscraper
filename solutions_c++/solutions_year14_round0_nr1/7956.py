#include<iostream>
#include<algorithm>
#include<vector>
#include<sstream>

using namespace std;

int main()
{
   short int T;
   cin >> T;
   short int l1[4], l2[4], row1, row2, temp, cnt;
   vector<string> output;
   for(int i = 0; i < T; i ++)
   {
      cin >> row1;
      for(int j = 0; j < 4; j ++)
      {
         if( j == row1 - 1)
         {
            for(int k = 0; k < 4 ; k ++)
            {
               cin >> l1[k];
            }
         }
         else
         {
            for(int k = 0; k < 4 ; k ++)
            {
               cin >> temp;
            }
         }
      }
      sort(l1, l1 + 4);
      cin >> row2;
      for(int j = 0; j < 4; j ++)
      {
         if( j == row2 - 1)
         {
            for(int k = 0; k < 4 ; k ++)
            {
               cin >> l2[k];
            }
         }
         else
         {
            for(int k = 0; k < 4 ; k ++)
            {
               cin >> temp;
            }
         }
      }
      sort(l2, l2 + 4);
      int j, j_temp = -1;
      cnt = 0;
      for(j = 0; j < 4; j ++)
      {
         cnt += count(l2, l2 + 4, l1[j]);
         if(cnt == 1 && j_temp == -1)
            j_temp = j;
         if (cnt > 1)
            break;
      }
      ostringstream Convert;
      Convert << l1[j_temp];
      if(cnt == 1)
         output.push_back(Convert.str().append("\n"));
      else
         if(cnt > 1)
            output.push_back("Bad magician!\n");
         else
            output.push_back("Volunteer cheated!\n");
   }

   for(int i = 0; i < T; i ++)
      cout<<"Case #"<< i + 1 << ": "<< output[i];
   return 0;
}
