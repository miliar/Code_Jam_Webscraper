#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#pragma warning(disable:4996)

using namespace std;
typedef long long ll;


void addMaxChecks(int k, int c, int& curK, set<ll>& res, ll curPos = 0)
{
   if (c == 0)
   {
      res.insert(curPos + 1);
      return;
   }
   if (curK != k)
      ++curK;
   curPos *= k;
   curPos += (curK - 1);

   addMaxChecks(k, c - 1, curK, res, curPos);
}


int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int nTests;
   scanf("%d", &nTests);
   for (int test = 1; test <= nTests; ++test)
   {
      int k, c, s;
      scanf("%d %d %d", &k, &c, &s);

      set<ll> result;

      int curK = 0;
      while (curK < k && result.size() < s)
         addMaxChecks(k, c, curK, result);
      
      printf("Case #%d:", test);      
      if (s == result.size() && curK != k)
         printf(" IMPOSSIBLE");
      else
         for (const auto a : result)
            printf(" %lld", a);
      puts("");
   }
   return 0;
}