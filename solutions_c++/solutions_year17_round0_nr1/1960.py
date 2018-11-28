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
#include <math.h>
#include <cassert>
#include <limits>
#include <memory.h>

//#pragma comment(linker,"/STACK:102400000,102400000") // 100 mb

#pragma warning(disable : 4996)

using namespace std;

#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   string s;
   int k;
   cin >> s >> k;

   const int n = s.length();

   int ans = 0;
   for (int i = 0; i < n; ++i)
   {
      if (s[i] == '+')
         continue;
      if (i <= n - k)
      {
         ++ans;
         for (int j = i; j < i + k; ++j)
            s[j] = (s[j] == '-' ? '+' : '-');
      }
      else
      {
         printf("Case #%d: IMPOSSIBLE\n", test + 1);
         return;
      }
   }

   printf("Case #%d: %d\n", test + 1, ans);
}

int main()
{
   ios_base::sync_with_stdio(false);
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
