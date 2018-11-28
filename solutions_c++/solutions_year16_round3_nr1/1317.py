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

int takeOne(vector<int>& arr)
{
   vector<int>::iterator it = max_element(all(arr));
   if (*it == 0)
   {
      return -1;
   }
   *it = *it - 1;
   return int(it - arr.begin());
}

string convert(int x)
{
   return string(1, char('A' + x));
}

void solve(int test)
{
   int n;
   cin >> n;

   vector<int> arr(n, 0);
   int sum = 0;
   for (int i = 0; i < n; ++i)
   {
      cin >> arr[i];
      sum += arr[i];
   }

   string ans;

   if (sum % 2 == 1)
   {
      ans += convert(takeOne(arr)) + " ";
   }

   while (true)
   {
      int a = takeOne(arr);
      int b = takeOne(arr);
      if (a == -1 && b == -1)
      {
         break;
      }
      if (a != -1 && b != -1)
      {
         ans += convert(a) + convert(b);
      }
      else
      {
         ans += convert(a);
      }
      ans += " ";
   }

   printf("Case #%d: %s\n", test + 1, ans.c_str());
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
