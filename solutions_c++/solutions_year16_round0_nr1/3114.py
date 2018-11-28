#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;
/***********************/
inline bool containsAllNumbersNow (const vector<bool>& inSeenNumbers)
{
   for (int i = 0; i < inSeenNumbers.size(); ++i)
   {
      if (inSeenNumbers[i] != true)
       return false;
   }
   return true;
}
/***********************/
inline void parseNumber (int64_t inNumber, vector<bool>& inSeenNumbers)
{
/*   for (int i = 0; i < inSeenNumbers.size(); ++i)
      cout << inSeenNumbers[i] << ",";
   cout << endl;
*/
   int64_t n = inNumber;
   while (n)
   {
      inSeenNumbers[n % 10] = true;
      n /= 10;
   }
}
/***********************/
void outputResult (int inTestCaseNum, int64_t result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": ";
   if (result)
      res << result << endl;
   else
      res << "INSOMNIA" << endl; 
}
/***********************/
int main()
{
   ifstream inp;
   inp.open ("/Users/gloria/Downloads/A-large.in");
//   inp.open ("/Users/gloria/Downloads/A-small-attempt0.in");
   ofstream res;
   res.open ("res1_large.txt");

   int n = 0;

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      int64_t testCase = 0;
      inp >> testCase;
      if (testCase == 0)
      {
         outputResult (i, 0, res);
         continue;
      }
      
      vector<bool> seenNumbers(10,0);
      int j = 1;
      while (!containsAllNumbersNow (seenNumbers))
      {
         parseNumber (testCase*j++, seenNumbers);
      }
     
      outputResult (i, testCase*(--j), res);
   }

   return 0;
}
