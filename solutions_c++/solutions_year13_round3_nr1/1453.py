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

bool check(const string& s, int l, int r, int n)
{
   int c = 0;
   FOR(i, l, r+1)
   {
      if (s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u')
      {
         ++c;
      }
      else
      {
         c = 0;
      }
      if (c == n)
      {
         return true;
      }
   }
   return false;
}

void SolveA()
{
   ifstream fin("input.txt");
   ofstream fout("output.txt");

   int tests;
   fin >> tests;

   for (int tc = 0; tc < tests; ++tc)
   {
      string s;
      int n;
      fin >> s >> n;

      int ans = 0;
      int len = s.length();

      FOR(i, 0, len)
      {
         FOR(j, i, len)
         {
            if (check(s, i, j, n))
            {
               ++ans;
            }
         }
      }

      fout << "Case #" << tc + 1 << ": ";
      fout << ans;
      fout << endl;
   }
}
