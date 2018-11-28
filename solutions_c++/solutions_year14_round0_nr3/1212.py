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

typedef vector<vector<int>> Grid;

int r, c, m;

bool checkCeil(const Grid& g, int x, int y)
{
   return x >= 0 && y >= 0 && x < r && y < c && g[x][y] == 0;
}

void print(const Grid& g)
{
   bool once = true;
   for (int i = 0; i < r; ++i)
   {
      for (int j = 0; j < c; ++j)
      {
         if (g[i][j] == 1)
            cout << "*";
         else if (once)
            cout << "c", once = false;
         else
            cout << ".";
      }
      cout << endl;
   }
}

bool place(Grid g, int x, int y)
{
   g[x][y] = 0;

   if (r * c == m + 1)
   {
      print(g);
      return true;
   }

   for (int i = 0; i < r; ++i)
   {
      for (int j = 0; j < c; ++j)
      {
         if (g[i][j] != 1)
            continue;
         if (checkCeil(g, i, j + 1)) g[i][j] = -1;
         if (checkCeil(g, i + 1, j + 1)) g[i][j] = -1;
         if (checkCeil(g, i - 1, j + 1)) g[i][j] = -1;
         if (checkCeil(g, i, j - 1)) g[i][j] = -1;
         if (checkCeil(g, i + 1, j - 1)) g[i][j] = -1;
         if (checkCeil(g, i - 1, j - 1)) g[i][j] = -1;
         if (checkCeil(g, i + 1, j)) g[i][j] = -1;
         if (checkCeil(g, i - 1, j)) g[i][j] = -1;
      }
   }

   int mineCnt = 0;
   for (int i = 0; i < r; ++i)
      for (int j = 0; j < c; ++j)
         if (g[i][j] == 1)
            ++mineCnt;

   if (mineCnt == m)
   {
      print(g);
      return true;
   }

   if (mineCnt < m)
      return false;

   for (int i = 0; i < r; ++i)
      for (int j = 0; j < c; ++j)
         if (g[i][j] == -1 && place(g, i, j))
            return true;

   return false;
}

void solve(int test)
{
   printf("Case #%d: \n", test + 1);

   cin >> r >> c >> m;
   for (int i = 0; i < r; ++i)
   {
      for (int j = 0; j < c; ++j)
      {
         Grid g(r, vector<int>(c, 1));
         if (place(g, i, j))
         {
            return;
         }
      }
   }
   
   cout << "Impossible\n";
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
