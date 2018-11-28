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
#include <math.h>

using namespace std;

#define FOR(i, a, b) for (int _n(b), i(a); i < _n; ++i)
#define FORD(i, a, b) for (int i=(a), _b=(b); i>=_b; --i)
#define REP(i, n) FOR(i, 0, n)

bool ispal(const string& s)
{
   for (size_t i = 0; i < s.length() / 2; ++i)
   {
      if (s[i] != s[s.length() - i - 1])
      {
         return false;
      }
   }
   return true;
}

void SolveC()
{
   ifstream fin("input.txt");
   ofstream fout("output.txt");

   int ntests = 0;
   fin >> ntests;

   for (int tc = 0; tc < ntests; ++tc)
   {
      long long a, b;
      fin >> a >> b;

      int k = 0;
      FOR(i, (int)sqrt(double(a)) - 1, (int)sqrt(double(b)) + 1)
      {
         long long square = i * i;
         if (square < a || square > b)
         {
            continue;
         }

         char buf[20];
         sprintf(buf, "%d", i);
         if (ispal(buf))
         {
            sprintf(buf, "%d", square);
            if (ispal(buf))
            {
               ++k;
            }
         }
      }

      fout << "Case #" << tc + 1 << ": ";
      fout << k;
      fout << endl;
   }
}
