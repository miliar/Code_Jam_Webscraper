#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <iomanip>

using namespace std;

bool solve(const vector<vector<int>>& lawn, const vector<int>& mrow, const vector<int>& mcolumn)
{
   for (int i = 0; i < lawn.size(); ++i)
   {
      for (int j = 0; j < lawn[i].size(); ++j)
      {
         if (lawn[i][j] < mrow[i] && lawn[i][j] < mcolumn[j])
         {
            return false;
         }
      }
   }
   return true;
}

void SolveB()
{
   ifstream fin("input.txt");
   ofstream fout("output.txt");

   int tests = 0;
   fin >> tests;

   for (int tc = 0; tc < tests; ++tc)
   {
      int n, m;
      fin >> n >> m;

      vector<vector<int>> lawn;
      for (int i = 0; i < n; ++i)
      {
         lawn.push_back(vector<int>(m, 0));
         for (int j = 0; j < m; ++j)
         {
            int a;
            fin >> a;
            lawn[i][j] = a;
         }
      }

      vector<int> mrow;
      for (int i = 0; i < n; ++i)
      {
         int maxRow = 00;
         for (int j = 0; j < m; ++j)
         {
            maxRow = max(maxRow, lawn[i][j]);
         }
         mrow.push_back(maxRow);
      }
      vector<int> mcolumn;
      for (int i = 0; i < m; ++i)
      {
         int maxColumn = 0;
         for (int j = 0; j < n; ++j)
         {
            maxColumn = max(maxColumn, lawn[j][i]);
         }
         mcolumn.push_back(maxColumn);
      }

      fout << "Case #" << tc + 1 << ": ";
      if (solve(lawn, mrow, mcolumn))
      {
         fout << "YES";
      }
      else
      {
         fout << "NO";
      }
      fout << endl;
   }
}
