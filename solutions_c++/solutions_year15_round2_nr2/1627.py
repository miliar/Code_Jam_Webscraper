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
   int r, c, k; // r, c, n
   cin >> r >> c >> k;

   int n = r * c;
   int best = 987654321;
   for (int mask = 0; mask < (1 << n); ++mask)
   {
      vector<vector<int>> grid(r, vector<int>(c, 0));
      int cnt = 0;
      for (int i = 0; i < n; ++i)
      {
         if ((1 << i) & mask)
         {
            ++cnt;
            grid[i / c][i % c] = 1;
         }
      }
      if (cnt != k)
      {
         continue;
      }
      int cur = 0;
      for (int i = 0; i < r; ++i)
      {
         for (int j = 0; j < c; ++j)
         {
            if (j < c - 1 && grid[i][j] == 1 && grid[i][j + 1] == 1)
            {
               ++cur;
            }
            if (i < r - 1 && grid[i][j] == 1 && grid[i + 1][j] == 1)
            {
               ++cur;
            }
         }
      }
      best = min(best, cur);
   }

   printf("Case #%d: %d\n", test + 1, best);
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
