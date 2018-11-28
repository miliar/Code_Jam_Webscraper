#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <assert.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);


int R, C, W;

int a[60];
bool area[60][60];
bool good[60][60];
bool ans[60][60];
bool found;
void go(int r, int sum)
{
   
   if (r == R)        
   {
      if (sum != R*C-W) return;
      
      for (int i = 0; i < R; i++)
      {
         for (int j = 0; j < C; j++)
            area[i][j] = j < a[i];

      }
      if (sum == 1)
      {
         assert(a[0] == 1);
         found = 1;
         for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++)
               ans[i][j] = area[i][j];
      }
      for (int i = 0; i < R; i++)
         for (int j = 0; j < C; j++)
         {
            good[i][j] = area[i][j];
            for (int k = i; k <= min(R-1, i+1); k++)
               for (int p = j; p <= min(C-1, j+1); p++)
                  good[i][j] &= area[k][p];
         }
     // for (int i = 0; i < R; i++, cout << endl)
     //    for (int j = 0; j < C; j++) cout << (good[i][j]?'x':(area[i][j]?'.':'*'));
     // cout << endl;
      
      for (int i = 0; i < R; i++)
         for (int j = 0; j < C; j++)
         {
            if (!area[i][j]) continue;
            bool ok = 0;
            for (int k = max(0,i-1); k <= i; k++)
               for (int p = max(0, j-1); p <= j; p++)
                  if (good[k][p]) ok = 1;

            if (!ok) 
            {
             // cout << i << ' ' << j << endl;
              return;
            }
         }
       found = 1;
       for (int i = 0; i < R; i++)
          for (int j = 0; j < C; j++)
             ans[i][j] = area[i][j];
       return;
   }
   if (found) return;
   for (int i = 0; i <= (r==0?C:a[r-1]); i++)
   {
       a[r] = i;
       go(r+1, sum + i);
       if (found) return;
   }
}


void solve(int test)
{                                    
   cin >> R >> C >> W; 
   found = 0;
   go(0,0);
   cout << "Case #" << test << ":" << endl;
   if (!found) cout << "Impossible" << endl;
   else
   {
     for (int i = 0; i < R; i++, cout << endl)
      for (int j = 0; j < C; j++)
        if (i==0&&j==0) cout << 'c';
        else if (area[i][j]) cout << '.';
        else cout << '*';
   }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
       solve(i);
}