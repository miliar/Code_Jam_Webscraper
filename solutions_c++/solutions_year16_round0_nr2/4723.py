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

void solve(int test)
{
   string s;
   cin >> s;

   const int n = s.length();

   int ans = 0;
   for (int i = 0; i < n; ++i)
   {
      if (s[i] == '-')
      {
         if (i == 0)
         {
            ans += 1;
         }
         else
         {
            ans += 2;
         }
         while (s[i] == '-' && i < n) ++i;
      }
   }

   printf("Case #%d: %d\n", test + 1, ans);
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
