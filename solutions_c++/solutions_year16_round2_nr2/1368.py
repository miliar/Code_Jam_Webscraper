#define _CRT_SECURE_NO_WARNINGS

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
#include <limits>
#include <cassert>
#include <math.h>
#include <memory.h>

//#pragma comment(linker, "/STACK:134217728")

using namespace std;
using namespace tr1;

#define all(c) (c).begin(), (c).end()
#define CLEAR(x) memset(x,0,sizeof x)

typedef long long ll;
typedef unsigned long long ull;

string convert(int i, int n)
{
   stringstream ss;
   ss << setw(n) << setfill('0') << i;
   return ss.str();
}

bool check(string s, string orig)
{
   for (int i = 0; i < s.length(); ++i)
   {
      if (s[i] != orig[i] && orig[i] != '?')
      {
         return false;
      }
   }
   return true;
}

void solve(int test)
{
   string s1, s2;
   cin >> s1 >> s2;

   int n = s1.length();
   int base = (int)pow((double)10, (double)n);

   int bestDiff = 1000;
   string ans1, ans2;
   for (int i = 0; i < base; ++i)
   {
      string t1 = convert(i, n);
      if (!check(t1, s1))
      {
         continue;
      }

      for (int j = 0; j < base; ++j)
      {
         string t2 = convert(j, n);
         if (check(t2, s2))
         {
            int curDiff = abs(i - j);
            if (bestDiff > curDiff)
            {
               bestDiff = curDiff;
               ans1 = t1;
               ans2 = t2;
            }
         }
      }
   }

   printf("Case #%d: %s %s\n", test + 1, ans1.c_str(), ans2.c_str());
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 0; test < tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test + 1, tests);
      solve(test);
   }

   return 0;
}
