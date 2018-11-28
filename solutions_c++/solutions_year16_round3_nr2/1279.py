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

ll myPow(int base, int exp)
{
   ll ans = 1;
   for (int i = 0; i < exp; ++i)
   {
      ans *= base;
   }
   return ans;
}

void solve(int test)
{
   int n;
   ll m;
   cin >> n >> m;

   ll maxWays = myPow(2, n - 2);

   if (m > maxWays)
   {
      printf("Case #%d: IMPOSSIBLE\n", test + 1);
      return;
   }

   typedef vector<vector<int>> Matrix;
   Matrix ans(n, vector<int>(n, 0));

   ans[0][n - 1] = 1;
   --m;

   int k = 1;
   while (m)
   {
      ans[0][k] = 1;
      ans[k][n - 1] = 1;
      --m;
      
      ll mask = (1 << (k - 1)) - 1;
      if (m < mask)
      {
         mask = m;
      }
      m -= mask;
      ll base = 1;
      for (int i = 0; i < k - 1; ++i)
      {
         if (mask & base)
         {
            ans[k][i + 1] = 1;
         }
         base *= 2;
      }
      ++k;
   }

   printf("Case #%d: POSSIBLE\n", test + 1);
   for (int i = 0; i < n; ++i)
   {
      for (int j = 0; j < n; ++j)
      {
         cout << ans[i][j];
      }
      cout << endl;
   }
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
