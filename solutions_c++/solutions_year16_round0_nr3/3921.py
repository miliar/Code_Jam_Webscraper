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
#include <bitset>
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

ll isPrime(ll x)
{
   for (ll i = 2; i * i <= x; ++i)
   {
      if (x % i == 0)
      {
         return i;
      }
   }

   return 0;
}

void solve(int test)
{
   int n, j;
   cin >> n >> j;

   const int baseCount = 10;

   ll powers[baseCount + 1][16] = {};
   for (int i = 2; i < baseCount + 1; ++i)
   {
      powers[i][0] = 1;
      for (int j = 1; j < 16; ++j)
      {
         powers[i][j] = i * powers[i][j - 1];
      }
   }

   printf("Case #%d: \n", test + 1);

   int founded = 0;
   for (int mask = (1 << (n - 1)) + 1; mask < (1 << n) && founded < j; mask += 2)
   {
      ll bases[baseCount + 1] = {};
      for (int k = 0; k < n; ++k)
      {
         if ((1 << k) & mask)
         {
            for (int i = 2; i < baseCount + 1; ++i)
            {
               bases[i] += powers[i][k];
            }
         }
      }

      bool good = true;
      ll divisors[baseCount + 1] = {};
      for (int i = 2; i < baseCount + 1; ++i)
      {
         divisors[i] = isPrime(bases[i]);
         if (divisors[i] == 0)
         {
            good = false;
            break;
         }
      }

      if (good)
      {
         ++founded;

         cout << bases[baseCount];
         for (int i = 2; i < baseCount + 1; ++i)
         {
            cout << " " << divisors[i];
         }
         cout << endl;
      }
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
