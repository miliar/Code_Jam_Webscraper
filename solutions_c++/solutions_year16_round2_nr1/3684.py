#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

string gDigits[] = {"EORZ", "ENO", "OTW", "EEHRT", "FORU", "EFIV", "ISX", "EENSV", "EGHIT", "EINN"} ;
const int cDigits = 10;

void searchAndReplace(std::string& testCase, int numEnt, int digit, std::vector<int>& result)
{
      for (int j = 0; j < gDigits[digit].length(); ++j)
      {
         for (int k = 0; k < numEnt; ++k)
         {
            std::size_t found = testCase.find(gDigits[digit][j]);
            testCase.erase(found);
         }
      }
      for (int i = 0; i < numEnt; ++i)
         result.push_back(digit);
}

bool searchTheRest(std::string& testCase, vector<int>& result)
{
//   cout << "x=" << testCase << endl;
   if (testCase.length() == 0)
   {
//        cout << "      finished searching " << endl;
   	return true;
   }

   std::string x = testCase;
   int i = 0;
   for (i = 0; i < cDigits; ++i)
   {
//      cout << "   i=" << i << "x=" << x << endl;
      std::size_t foundAll = true;
      for (int j = 0; j < gDigits[i].length() && foundAll; ++j)
      {
         if (string::npos != x.find(gDigits[i][j]))
            x.erase(x.find(gDigits[i][j]),1);
         else
            foundAll = false;
      }
      if (!foundAll)
      {
//         cout << "      didn't found " << i << endl;
         x = testCase;
      }
      else
      {
//         cout << "      found " << i << endl;
         bool res = searchTheRest(x, result);
         if (res)
         {
            result.push_back(i);
            break;
         }
         else
         {
            x = testCase;
 //           result.clear();
         }
      }        
   }
   if (i == cDigits)
	return false;

   return true;
}

/***********************/
void outputResult (int inTestCaseNum, vector<int>& result, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": ";
   for (int i = 0; i < result.size(); ++i)
   {
      res << result[i];
   }
   res << endl;
}
/***********************/
int main()
{
   int n = 0;

    ifstream inp;
   inp.open ("/Users/gloria/Downloads/A-small-attempt0.in");
   ofstream res;
   res.open ("res1_small.txt");

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      std::string testCase;
      inp >> testCase;
/*
      std::sort (testCase.begin(), testCase.end());

      std::vector<int> result;
      size_t numEnt = std::count(testCase.begin(), testCase.end(), 'Z');
      searchAndReplace(numEnt, 0, result);
      numEnt = std::count(testCase.begin(), testCase.end(), 'W');
      searchAndReplace(numEnt, 2, result);
      numEnt = std::count(testCase.begin(), testCase.end(), 'X');
      searchAndReplace(numEnt, 6, result);
*/
      std::vector<int> result;
      searchTheRest(testCase, result);
      std::sort(result.begin(), result.end());
      outputResult (i, result, res);
   }

   return 0;
}
