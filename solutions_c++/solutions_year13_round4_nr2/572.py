#include <algorithm>
#include <iostream>
#include <map>
using namespace std;

typedef long long int64;

std::map<int64, std::map<int64, bool>> dpWillWin[51];
std::map<int64, std::map<int64, bool>> dpMayWin[51];

bool willWinReal(int64 better, int games, int64 prices);
bool willWin(int64 better, int games, int64 prices)
{
   auto it = dpWillWin[games].find(better);
   if (it != dpWillWin[games].end())
   {
      auto jt = it->second.find(prices);
      if (jt != it->second.end())
         return jt->second;
   }
   bool ret = willWinReal(better, games, prices);
   dpWillWin[games][better][prices] = ret;
   return ret;
}

bool willWinReal(int64 better, int games, int64 prices)
{
   if (prices <= better)
      return false;
   int64 worse = (1LL<<games)-better-1;
   if (games == 1)
   {
      if (better < prices)
         return true;
      return false;
   }
   int64 nextCount = 1LL << (games-1);
   if (worse > 0)
   {
      // Win this game
      int64 b2 = min(better, nextCount-1);
      int64 p2 = min(prices, nextCount);
      if (!willWin(b2, games-1, p2))
         return false;
   }
   if (better > 0)
   {
      // Loose this game
      if (prices <= nextCount)
         return false;
      int64 b2 = min((better-1)/2, nextCount-1);
      int64 p2 = prices-nextCount;
      if (!willWin(b2, games-1, p2))
         return false;
   }
   return true;
}


bool mayWinReal(int64 better, int games, int64 prices);
bool mayWin(int64 better, int games, int64 prices)
{
   auto it = dpMayWin[games].find(better);
   if (it != dpMayWin[games].end())
   {
      auto jt = it->second.find(prices);
      if (jt != it->second.end())
         return jt->second;
   }
   bool ret = mayWinReal(better, games, prices);
   dpMayWin[games][better][prices] = ret;
   return ret;
}

bool mayWinReal(int64 better, int games, int64 prices)
{
   int64 worse = (1LL<<games)-better-1;
   if (games == 1)
   {
      if (better < prices)
         return true;
      return false;
   }
   int64 nextCount = 1LL << (games-1);
   if (worse > 0)
   {
      // Win this game
      int64 b2 = (better+1)/2;
      int64 p2 = min(prices, nextCount);
      if (mayWin(b2, games-1, p2))
         return true;
   }
   if (better > 0)
   {
      // Loose this game
      if (prices > nextCount)
      {
         int64 b2 = max(0LL, better-nextCount);
         int64 p2 = prices-nextCount;
         if (worse == 0)
         {
            if (p2 == nextCount)
               return true;
         }
         else
         {
            if (mayWin(b2, games-1, p2))
               return true;
         }
      }
   }
   return false;
}

int main()
{
   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
   {
      int n;
      int64 p;
      cin >> n >> p;
      int64 y, z;
      {
         int64 mi = 0;
         int64 ma = (1LL<<n) - 1;
         while (mi < ma)
         {
            int64 mid = (mi+ma+1)/2;
            if (willWin(mid, n, p))
               mi = mid;
            else
               ma = mid-1;
         }
         y = mi;
      }
      {
         int64 mi = 0;
         int64 ma = (1LL<<n) - 1;
         while (mi < ma)
         {
            int64 mid = (mi+ma+1)/2;
            if (mayWin(mid, n, p))
               mi = mid;
            else
               ma = mid-1;
         }
         z = mi;
      }

      cout << "Case #" << (t+1) << ": " << y << ' ' << z << endl;
   }
   return 0;
}
