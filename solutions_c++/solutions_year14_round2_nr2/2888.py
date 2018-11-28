#include <iostream>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
   int nrOfCases;
   cin >> nrOfCases;
   for (int i = 1; i <= nrOfCases; ++i)
   {
      int ctr = 0;
      int a, b, k;
      cin >> a >> b >> k;
      for (int x = 0; x < a; ++x)
      {
         for (int y = 0; y < b; ++y)
         {
            if ((x&y) < k)
            {
               ++ctr;
            }
         }
      }

      cout << "Case #" << i << ": " << ctr << endl;
   }

   return 0;
}