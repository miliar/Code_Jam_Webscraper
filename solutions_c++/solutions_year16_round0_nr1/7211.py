#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define printFile(output_file,c,value) output_file << "Case #" << (c) << ": " <<  (value) << endl

int main()
{
	ifstream in("input.in");
	ofstream out("output.out");
	
	int T = 0;
	in >> T;

	for (int _case = 1; _case <= T;  _case++)
   {
      int N = 0;
      in >> N;
      printf("N = %d\n",N);
      if (N == 0)
      {
         printFile(out, _case, "INSOMNIA");
         continue;
      }

      vector<int> digits;
      int number = N;
      int count = 1;
      
      while(count)
      {
         number = N*count;

         bool isStop = false;
         int r = 0;
         int n = number;
         do
         {
            r = n%10;
            n = n/10;
 
            bool isNewDigit = true;
            for (int i = 0; i < digits.size(); i++)
            {
               if (r == digits[i])
               {
                  isNewDigit = false;
                  break;
               }
            }

            if (isNewDigit)
               digits.push_back(r);

            if (digits.size() == 10)
            {
               isStop = true;
               break;
            }
         
         }
         while(n>0);

         if (isStop)
         {
            printFile(out,_case,number);
            break;
         }
         count++;
      }
   }
   out.close();
}