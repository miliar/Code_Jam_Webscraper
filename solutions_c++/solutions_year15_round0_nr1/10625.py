#include <iostream>

using namespace std;

int main()
{
   int T = 0;
   int SMax = 0;
   int testCase = 1;
   int A[1000];
   int S = 0;
   int count = 0;
   int q = 0;
       int total = 0;
  
   cin >> T ;
   for(;T > 0; --T)
   {
       cin >> SMax >> S;
       total = 0;
       count = 0;
       for(int a = 0; a <= SMax; a++)
       {
            A[SMax-a] = S%10;
            S = S/10;
       }
       
       for(int i = 0; i <=SMax; i++)
       {
            total += A[i];
            if(total < i+1)
            {
                count += (i+1) - total;
                total += (i+1) - total;
            }
            //cout << "i = " << i << " A[i] = " << A[i] << " count = " << count << " total = " << total << endl;
       }
       cout << "Case #"<<testCase <<": " << count << endl;
       ++testCase;
   }
   
   return 0;
}
