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
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0, _n=(n); i < _n; ++i)
#define REPD(i,n) for (int i=(n)-1; i >= 0; --i)
#define FOR(i,a,b) for (int _n=(b), i=(a); i < _n; ++i)
#define FORD(i,a,b) for (int i=(a), _n=(b); i >= _n; --i)

#define CLEAR(x) memset(x,0,sizeof x);


int diff(int& x, int y)
{
   int res = 0;
   while (x <= y)
   {
      x += x-1;
      ++res;
   }
   x += y;
   return res;
}

void SolveA()
{
   ifstream fin("input.txt");
   ofstream fout("output.txt");

   int tests;
   fin >> tests;

   for (int tc = 0; tc < tests; ++tc)
   {
      int A, N;
      vector<int> motes;

      fin >> A >> N;
      REP(i, N)
      {
         int m;
         fin >> m;
         motes.push_back(m);
      }

      sort(motes.begin(), motes.end());
      int k = 0;
      REP(i, N)
      {
         if (A > motes[i])
         {
            A += motes[i];
         }
         else if (A == 1)
         {
            k += N-i;
            break;
         }
         else
         {
            int d = diff(A, motes[i]);
            if (d < N-i)
            {
               k += d;
            }
            else
            {
               k += N-i;
               break;
            }
         }
      }

      fout << "Case #" << tc + 1 << ": ";
      fout << k;
      fout << endl;
   }
}
