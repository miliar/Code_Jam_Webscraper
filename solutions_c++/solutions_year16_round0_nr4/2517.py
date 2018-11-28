#include <iostream>
#include <vector>
#include <set>
using namespace std;

/***********************/
void outputResult (int inTestCaseNum, int64_t K)
{
   cout << "Case #" << inTestCaseNum+1 << ": ";
 
   for (int i = 0; i < K; ++i)
   {
      cout << " " << i+1;
   }
   cout << endl;
}
/***********************/
int main()
{
   int n = 0;

   cin >> n;

   for (int i = 0; i < n; ++i)
   {
      int64_t K, C, S = 0;
      cin >> K >> C >> S;
     
      outputResult (i, K);
   }

   return 0;
}
