#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int pancakeCnt(string n)
{
   if(n.size() == 0)
      return 0;
   char prev = n[0]; int swap = 0;
   int cnt = 0;
   for(int i = 0; i < n.size(); ++i)
   {
      char prev = n[0]; swap = 0;
      for(int j = 1; j < n.size(); ++j)
      {
         if(prev != n[j])
         {
            for(int k = 0; k < j; ++k)
            {
               if(n[k] == '+')
                  n[k] = '-';
               else
                  n[k] = '+';
            }
            ++cnt;
            swap = 1;
            break;
         }
      }
      if(!swap)
         break;
   } 
   if(n[0] == '-')
      return cnt+1;
   else
      return cnt;
}

int main()
{
   ifstream file("input.txt");
   string line;   

   if(file.is_open())
   {
      getline(file,line);
      int cnt = 1;
      while(getline(file,line))
      {
         cout << "Case #" << cnt << ": " << pancakeCnt(line) << endl;
         cnt++;
      }
   }
}
