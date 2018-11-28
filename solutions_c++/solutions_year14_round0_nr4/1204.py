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
   int n;
   cin >> n;

   vector<double> naomi(n, 0.);
   vector<double> ken(n, 0.);
   for (int i = 0; i < n; ++i)
      cin >> naomi[i];
   for (int i = 0; i < n; ++i)
      cin >> ken[i];

   sort(all(naomi));
   sort(all(ken));

   int scores1 = 0;
   for (int i = 0, j = n - 1, k = 0; i < n; ++i)
   {
      if (naomi[i] > ken[j])
      {
         scores1 += n - i;
         break;
      }
      if (naomi[i] > ken[k])
      {
         ++k;
         ++scores1;
      }
      else
      {
         --j;
      }
   }

   int scores2 = 0;
   for (int i = 0, j = 0; i < n; ++i, ++j)
   {
      while (j < n && naomi[i] > ken[j]) ++j;
      if (j == n)
      {
         scores2 = n - i;
         break;
      }
   }

   printf("Case #%d: %d %d\n", test + 1, scores1, scores2);
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
