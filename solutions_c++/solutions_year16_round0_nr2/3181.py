#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;
/***********************/

/***********************/
void outputResult (int inTestCaseNum, int64_t result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": " << result << endl;
}
/***********************/
int main()
{
    ifstream inp;
   inp.open ("/Users/gloria/Downloads/B-large.in");
//   inp.open ("/Users/gloria/Downloads/B-small-attempt0.in");
   ofstream res;
   res.open ("res2_large.txt");

   int n = 0;

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      string testCase;
      inp >> testCase;
     
      int flips = 1;
      char c = testCase[0];
      for (int k = 1; k < testCase.length(); ++k)
      {
         if (testCase[k] != c)
         {
            c = testCase[k];
            ++flips;
         }
      }

      if (c == '+')
         flips -= 1;

      outputResult (i, flips, res);
   }

   return 0;
}
