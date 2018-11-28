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

bool reduce(const vector<int>& arr, int depth)
{
   if (depth == 0)
   {
      return false;
   }

   int maximal = arr.back();

   if (maximal == depth)
   {
      return true;
   }

   for (int k = 1; k <= maximal / 2; ++k)
   {
      vector<int> newArr = arr;
      newArr.back() -= k;
      newArr.push_back(k);
      sort(all(newArr));
      if (reduce(newArr, depth - 1))
      {
         return true;
      }
   }

   return false;
}

void solve(int test)
{
   int n;
   cin >> n;

   vector<int> values(n, 0);
   for (int i = 0; i < n; ++i)
   {
      cin >> values[i];
   }

   sort(all(values));

   int ans = 0;
   for (int depth = 1; depth <= 9; ++depth)
   {
      if (reduce(values, depth))
      {
         ans = depth;
         break;
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
