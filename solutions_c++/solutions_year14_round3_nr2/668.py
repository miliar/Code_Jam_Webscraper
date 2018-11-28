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

struct Item 
{
   string s;
   int pos;
   bool operator< (const Item& other) const { return pos < other.pos; }
};

void solve(int test)
{
   int n;
   cin >> n;
   vector<Item> v;
   map<char, int> stats;
   for (int i = 0; i < n; ++i)
   {
      string s, t;
      cin >> s;
      t += s[0];
      for (int j = 1; j < s.length(); ++j)
         if (s[j] != s[j - 1])
         {
            t += s[j];
            ++stats[s[j]];
         }
      Item item = {t, i};
      v.push_back(item);
   }

   sort(all(v));

   int ans = 0;
   do
   {
      string composed;
      for (int i = 0; i < n; ++i)
         composed += v[i].s;
   
      bool good = true;
      vector<char> used;
      for (int i = 0; i < composed.length(); ++i)
      {
         if (find(all(used), composed[i]) == used.end())
         {
            used.push_back(composed[i]);
         }
         else if (used.back() != composed[i])
         {
            good = false;
            break;
         }
      }
      if (good)
         ++ans;
   } while (next_permutation(all(v)));

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
