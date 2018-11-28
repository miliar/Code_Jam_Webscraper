#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> dict;
const int minDiffFree = 5;
int dp[minDiffFree][4001];
string enc;
int n; // enc.size()

bool fitWord(int pos, const string &w, int &firstDiff, int &lastDiff, int &diffCount)
{
   firstDiff = minDiffFree;
   diffCount = 0;
   bool foundADiff = false;
   int diffPos = -minDiffFree;
   const int ws = (int)w.size();
   if (pos + ws > n)
      return false; // Past end of the string?
   for (int i = 0; i < ws; ++i)
   {
      if (w[i] != enc[pos+i])
      {
         if (!foundADiff)
         {
            foundADiff = true;
            firstDiff = i;
         }
         else
         {
            if (i - diffPos < minDiffFree)
               return false;
         }
         diffPos = i;
         ++diffCount;
      }
   }
   lastDiff = diffPos;
   return true;
}

int main()
{
   {
      ifstream f("garbled_email_dictionary.txt");
      if (!f)
      {
         cerr << "Could not open garbled_email_dictionary.txt." << endl;
         return 1;
      }
      while (f)
      {
         string s;
         getline(f, s);
         if (!s.empty())
            dict.push_back(s);
      }
      f.close();
   }
   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
   {
      cin >> enc;
      n = (int)enc.size();
      for (int i = 0; i < minDiffFree; ++i)
      {
         for (int j = 0; j <= n; ++j)
            dp[i][j] = 10000;
         dp[i][0] = 0;
      }
      int ds = dict.size();
      for (int pos = 0; pos < n; ++pos)
      {
         for (int w = 0; w < ds; ++w)
         {
            int firstDiff;
            int lastDiff;
            int diffCount;
            const int ws = (int)dict[w].size();
            if (fitWord(pos, dict[w], firstDiff, lastDiff, diffCount))
            {
               firstDiff = min(firstDiff, minDiffFree-1);
               const int diffFreeNextWord = max(lastDiff + minDiffFree - ws, 0);
               for (int diffFreeCount = 0; diffFreeCount <= firstDiff; ++diffFreeCount)
               {
                  int dfnw = max(diffFreeNextWord, diffFreeCount - ws);
                  int x = dp[diffFreeCount][pos] + diffCount;
                  if (x < dp[dfnw][pos + ws])
                     dp[dfnw][pos + ws] = x;
               }
            }
         }
      }
      int ret = 10000;
      for (int i = 0; i < minDiffFree; ++i)
      {
         if (dp[i][n] < ret)
            ret = dp[i][n];
      }
      cout << "Case #" << (t+1) << ": " << ret << endl;
   }
   return 0;
}
