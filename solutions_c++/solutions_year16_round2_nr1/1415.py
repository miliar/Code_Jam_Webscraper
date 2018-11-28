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
   string encoded;
   cin >> encoded;

   map<char, int> m, m2;
   for (int i = 0; i < encoded.length(); ++i)
   {
      m[encoded[i]]++;
   }

   int nums[10] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
   string numbers[10] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", "FIVE", "SEVEN", "NINE"};

   stringstream ans;
   for (int i = 0; i < 10; ++i)
   {
      string s = numbers[i];
      bool good = true;
      while (good)
      {
         map<char, int> tm = m;
         for (int k = 0; k < s.length(); ++k)
         {
            if (tm[s[k]] == 0)
            {
               good = false;
               break;
            }
            else
            {
               tm[s[k]]--;
            }
         }
         if (good)
         {
            m = tm;
            ans << nums[i];
         }
      }
   }

   for (map<char, int>::iterator it = m.begin(), end = m.end(); it != end; ++it)
   {
      if (it->second > 0)
      {
         break;
      }
   }

   string tmp = ans.str();
   sort(all(tmp));

   printf("Case #%d: %s\n", test + 1, tmp.c_str());
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
