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
   ull d;
   cin >> d;

   if (d == 0)
   {
      printf("Case #%d: INSOMNIA\n", test + 1);
      return;
   }

   int i = 1;
   set<int> digits;
   while (true)
   {
      ull t = d * i;
      assert(t <= ULLONG_MAX);
      while (t > 0)
      {
         digits.insert(t % 10);
         t /= 10;
      }

      if (digits.size() == 10)
      {
         break;
      }

      ++i;
   }

   printf("Case #%d: %d\n", test + 1, d * i);
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
