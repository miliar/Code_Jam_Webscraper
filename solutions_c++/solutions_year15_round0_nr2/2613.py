#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int max(const vector<int>& diner_array)
{
     int to_return = -1;
     for(int i=0; i<diner_array.size(); i++)
          if(diner_array[i] > to_return)
               to_return = diner_array[i];
     return to_return;
}

int maxpos(const vector<int>& diner_array)
{
     int to_return = -1;
     int maxval = -1;
     for(int i=0; i<diner_array.size(); i++)
          if(diner_array[i] > maxval)
          {
               to_return = i;
               maxval = diner_array[i];
          }
     return to_return;
}

//Idiotically exhaustively search the array
int idiot_recurse(vector<int> diner_array, int penalty)
{
     int maxval = max(diner_array);
     if(maxval < 4)
          return maxval + penalty;

     int current_best = maxval + penalty;
     int maxidx = maxpos(diner_array);
     diner_array.push_back(0);
     int finalidx = diner_array.size()-1;

     //Half split
     diner_array[maxidx] = maxval / 2 + maxval % 2;
     diner_array[finalidx] = maxval / 2;
     int halfsplitbest = idiot_recurse(diner_array,penalty+1);

     //Third split
     int third = maxval/3;
     diner_array[maxidx] = third*2;
     diner_array[finalidx] = third;
     if(maxval%3==2)
          diner_array[maxidx]++;
     if(maxval%3)
          diner_array[finalidx]++;
     int thirdsplitbest = idiot_recurse(diner_array,penalty+1);

     if(halfsplitbest < current_best)
          current_best = halfsplitbest;
     if(thirdsplitbest < current_best)
          current_best = thirdsplitbest;

     return current_best;
}

int main()
{
     int testcases;
     cin >> testcases;
     for(int i=0; i<testcases; i++)
     {
          //Input
          int active_diners;
          cin >> active_diners;
          vector<int> diner_array;
          diner_array.reserve(active_diners);
          for(int j=0; j<active_diners; j++)
          {
               int temp;
               cin >> temp;
               diner_array.push_back(temp);
          }

          cout << "Case #" << (i+1) << ": " << idiot_recurse(diner_array,0) << endl;
     }
     
     return 0;
}
