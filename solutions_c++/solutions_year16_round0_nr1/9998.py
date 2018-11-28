#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include "stdlib.h"

using namespace std;

int countingSheep(int n)
{
   if(n == 0)
      return 0;
   set<int> digits;
   long long int tmp;

   int cnt = 1;
   while(digits.size() != 10)
   {
     tmp = n * cnt;      
      while(tmp)
      {
         digits.insert(tmp%10);
         tmp /= 10;
      }
      ++cnt;
   }
   return n * --cnt;
}

int main()
{
   ifstream file("input.txt");
   string line;
   int t, ret;
   if (file.is_open())
   {
      getline(file,line);
      t = atoi(line.c_str());
      int cnt = 1;
      while(getline(file,line))
      {  
         int n;
         n = atoi(line.c_str());
         if ((ret = countingSheep(n)) == 0)
            cout << "Case #" << cnt << ": INSOMNIA" << endl;
         else
            cout << "Case #" << cnt << ": " << ret << endl;
         cnt++;
      }
   }
}
