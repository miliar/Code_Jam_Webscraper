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

   vector<string> collapsed(n, string());
   vector<vector<int>> nums(n, vector<int>());

   for (int i = 0; i < n; ++i)
   {
      string s;
      cin >> s;
      collapsed[i] += s[0];
      nums[i].push_back(1);
      for (int k = 1; k < s.length(); ++k)
      {
         if (s[k] == s[k - 1])
         {
            ++nums[i].back();
         }
         else
         {
            collapsed[i] += s[k];
            nums[i].push_back(1);
         }
      }
   }

   set<string> checker(all(collapsed));
   if (checker.size() > 1)
   {
      printf("Case #%d: Fegla Won\n", test + 1);
      return;
   }

   int ans = 0;
   int m = nums.front().size();
   for (int k = 0; k < m; ++k)
   {
      vector<int> temp;
      for (int i = 0; i < n; ++i)
         temp.push_back(nums[i][k]);

      int best = 987654321;
      for (int i = 0; i < n; ++i)
      {
         int cur = 0;
         for (int j = 0; j < n; ++j)
            cur += abs(temp[i] - temp[j]);
         best = min(best, cur);
      }

      ans += best;
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
