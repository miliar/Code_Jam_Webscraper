#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[])
{
   
   long testCases;

   cin >> testCases;

   for(long n = 1; n <= testCases; ++n)
   {
      long r;
      long t;

      cin >> r;
      cin >> t;
   

      long curRad = r;
      long count = 0;
      while(t >= 0)
      {
         ++curRad;
         t = t - (( curRad * curRad) - ((curRad-1) * (curRad-1)));
         ++count;
         ++curRad;
         //cout << "t " << t << endl;
      }

      cout << "Case #" << n << ": " << count-1 << endl;


   }

   return 0;
}
