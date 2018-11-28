#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#pragma warning(disable:4996)

using namespace std;
typedef long long ll;


int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int nTests;
   cin >> nTests;
   for (int test = 1; test <= nTests; ++test)
   {
      string s;
      cin >> s;
      char curC = s[0];
      int res = 0;
      for (int i = 1; i < s.length(); i++)
      {
         if (curC != s[i])
         {
            res++;
            curC = s[i];
         }
      }
      if (s.back() == '-')
         res++;
      printf("Case #%d: %d\n", test, res);
   }
   return 0;
}