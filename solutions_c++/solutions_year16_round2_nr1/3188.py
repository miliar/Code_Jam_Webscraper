#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define INF 1023123123
#define EPS 1e-11
#define LSOne(S) (S & (-S))

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FORB(X,Y) for (int (X) = (Y);(X) >= 0;--(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define REPB(X,Y,Z) for (int (X) = (Y);(X) >= (Z);--(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

void print_case(int i)
{
   cout << "Case #" << i + 1 << ": ";
}

int main()
{
   int ntc;
   cin >> ntc;
   
   FORN(kk, ntc)
   {
      print_case(kk);
      string s;
      cin >> s;
      vi lkp(300);
      FORN(i, s.size())
      {
         lkp[s[i]]++;
      }
      vi ans;
      vector<string> nums{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
      vector<pair<char, int>> first{ { 'Z', 0 }, { 'W', 2 }, { 'G', 8 }, { 'U', 4 }, { 'X', 6 } };
      vector<pair<char, int>> second{ { 'R', 3 }, { 'O', 1 }, { 'F', 5 }, { 'S', 7 } };
      vector<pair<char, int>> third{ { 'E', 9 } };
      auto all = std::vector<vector<pair<char, int>>>{ first, second, third };
      FORN(k, all.size())
      {
         auto dd = all[k];
         FORN(i, dd.size())
         {
            while (lkp[dd[i].first] > 0)
            {
               ans.push_back(dd[i].second);
               FORN(j, nums[dd[i].second].size())
               {
                  lkp[nums[dd[i].second][j]]--;
               }
            }
         }
      }
      sort(ans.begin(), ans.end());
      FORN(i, ans.size())
      {
         cout << ans[i];
      }
      cout << endl;
   }
}
