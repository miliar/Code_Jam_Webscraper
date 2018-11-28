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
#include <array>
#include <cmath>
#include <cassert>

using namespace std;
using namespace tr1;

#define REP(i,n) for (int i=0, _n=(n); i < _n; ++i)
#define REPD(i,n) for (int i=(n)-1; i >= 0; --i)
#define FOR(i,a,b) for (int _n=(b), i=(a); i < _n; ++i)
#define FORD(i,a,b) for (int i=(a), _n=(b); i >= _n; --i)
#define all(c) (c).begin(), (c).end()

#define CLEAR(x) memset(x,0,sizeof x);

int X, Y;

struct pogo 
{
   int x;
   int y;
   int d;
   vector<char> p;
};

void SolveB()
{
   ifstream fin("input.txt");
   ofstream fout("output.txt");

   int tests;
   fin >> tests;

   for (int tc = 0; tc < tests; ++tc)
   {
      fin >> X >> Y;

      vector<char> ans;
      int x = 0;
      int d = 1;
      int i = 0;
      while (x != X)
      {
         if (i % 2 == 0)
         {
            x += d;
            ans.push_back('E');
         }
         else
         {
            x -= d;
            ans.push_back('W');
         }
         ++d;
         ++i;
      }

      int y = 0;
      i = Y > 0 ? 1 : 0;
      while (y != Y)
      {
         if (i % 2 == 0)
         {
            y += d;
            ans.push_back('N');
         }
         else
         {
            y -= d;
            ans.push_back('S');
         }
         ++d;
         ++i;
      }

      fout << "Case #" << tc + 1 << ": ";
      REP(i, ans.size())
         fout << ans[i];
      fout << endl;
   }
}
