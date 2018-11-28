#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
using namespace std;

/***********************/
void outputResult (int inTestCaseNum, ofstream& res)
{
   res << "Case #" << inTestCaseNum+1 << ": ";
}

void outputResult (int inTestCaseNum, char result, ofstream& res)
{
   res << " " << result;
}

void outputResult (int inTestCaseNum, char result1, char result2, ofstream& res)
{
   res << " " << result1 << result2;
}

bool myfunction (pair<char,int> i,pair<char,int> j) 
{ 
    return (i.second > j.second); 
}
/***********************/
int main()
{
   int n = 0;

    ifstream inp;
//   inp.open ("/Users/gloria/Downloads/A-large.in");
   inp.open ("/Users/gloria/Downloads/A-small-attempt0.in");
   ofstream res;
   res.open ("res1.txt");

   inp >> n;

   for (int i = 0; i < n; ++i)
   {
      int testCase;
      inp >> testCase;

      vector<std::pair<char, int> > sen;
      for (int j = 0; j < testCase; ++j)
      {
        int num;
        inp >> num;
        sen.push_back(make_pair(j+'A', num));
      }
      sort(sen.begin(), sen.end(), myfunction);

      outputResult (i, res);
//      cout << "testcase " << i << ": ";
      int a = 0;
      int b = 1;
      while (sen.size())
      {  
         if (sen.size() < 4)
         {
            if (sen.size() == 3 && sen[0].second == 1 && sen[1].second== 1 && sen[2].second == 1)
            {
               outputResult(i, sen[0].first, res);
               outputResult(i, sen[1].first, sen[2].first, res);

           //    cout << " " << sen[0].first;
           //    cout << " " << sen[1].first << sen[2].first;
               break;
            }
      	      // cout << endl << "We are here 5 " << sen.size();
            sort(sen.begin(), sen.end(), myfunction);
         }
  //    	 cout << endl << sen.size();
         int c = b+1;
         int d = b+2;
         if (sen[a].second > sen[b].second)
         {
            sen[a].second--;
            outputResult(i, sen[a].first, res);
      	 //   cout << " " << sen[a].first;
            if (!sen[a].second) sen.erase(sen.begin()+a), b--, c--, d--;
            
         }
         else
         { 
            sen[a].second--; sen[b].second--;
            outputResult(i, sen[a].first, sen[b].first, res);
      	   // cout << " " << sen[a].first << sen[b].first;
            if (a > b)
            {
               c = a + 1;
               d = a + 2;
  //    	       cout << endl << "We are here";
               if (!sen[a].second) sen.erase(sen.begin()+a), c--, d--;
               if (!sen[b].second) sen.erase(sen.begin()+b), c--, d--;
            }
            else if (a != b)
            {
//      	       cout << endl << "We are here 2";
               if (!sen[b].second) sen.erase(sen.begin()+b), c--, d--;
               if (!sen[a].second) sen.erase(sen.begin()+a), c--, d--;
            }
         }
//      	       cout << endl << "We are here 2";
         
         if (sen.size() < 4)
         {
            if (sen.size() == 3 && sen[0].second == 1 && sen[1].second== 1 && sen[2].second == 1)
            {
               outputResult(i, sen[0].first, res);
               outputResult(i, sen[1].first, sen[2].first, res);

           //    cout << " " << sen[0].first;
           //    cout << " " << sen[1].first << sen[2].first;
               break;
            }
      	      // cout << endl << "We are here 5 " << sen.size();
            sort(sen.begin(), sen.end(), myfunction);
         }
         else
         {
      	     //  cout << endl << "We are here 3";
            if(sen[c].second > sen[b].second)
            {
               a = c;
               if (sen[d].second > sen[b].second)
                  b = d;
               else
               {
                  a = 0;
                  b = 1;
               }
            } 
            else
            {
               a = c;
               b = d;
            }
      	      // cout << endl << "We are here 4";
        }
      }
      res << endl;
   //   cout << endl;
   }

   return 0;
}
