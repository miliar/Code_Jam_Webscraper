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

set<int> readRow(int rowNum)
{
   set<int> row;
   for (int i = 0; i < 4; ++i)
   {
      for (int j = 0; j < 4; ++j)
      {
         int x;
         cin >> x;
         if (i == rowNum)
         {
            row.insert(x);
         }
      }
   }
   return row;
}

void solve(int test)
{
   int n1;
   cin >> n1;
   set<int> r1 = readRow(n1 - 1);

   int n2;
   cin >> n2;
   set<int> r2 = readRow(n2 - 1);

   vector<int> intersect;
   set_intersection(all(r1), all(r2), back_inserter(intersect));
   
   ostringstream oss;
   if (intersect.empty())
      oss << "Volunteer cheated!";
   else if (intersect.size() > 1)
      oss << "Bad magician!";
   else
      oss << intersect.front();

   printf("Case #%d: %s\n", test + 1, oss.str().c_str());
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
