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

   string s;
   cin >> s;

   int totalLevel = 0, invited = 0;
   for (int level = 0; level < n + 1; ++level)
   {
      int curLevelCnt = s[level] - '0';
      if (curLevelCnt > 0 && totalLevel < level)
      {
         invited += level - totalLevel;
         totalLevel = level;
      }
      totalLevel += curLevelCnt;
   }

   printf("Case #%d: %d\n", test + 1, invited);
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
