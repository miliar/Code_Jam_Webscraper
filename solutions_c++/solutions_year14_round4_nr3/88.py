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

typedef pair<int,int> pii;
 #define L first
 #define R second
pii xes[1005];
pii yes[1005];

int d[1005][1005];

int r[1005], ok[1005];

void solve(int test)
{
   int w,h,n;
   cin >> w >> h >> n;
   for (int i = 0; i < n; i++)
   {
      cin >> xes[i].L >> yes[i].L >> xes[i].R >> yes[i].R;
   }
   for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
      {
          int d1 = 0, d2 = 0;
          if (xes[i].R < xes[j].L) d1 += xes[j].L - xes[i].R - 1;
          if (xes[j].R < xes[i].L) d1 += xes[i].L - xes[j].R - 1;
          if (yes[i].R < yes[j].L) d2 += yes[j].L - yes[i].R - 1;
          if (yes[j].R < yes[i].L) d2 += yes[i].L - yes[j].R - 1;
          d[i][j] = max(d1,d2);
      } 
   for (int i = 0; i < n; i++)
      r[i] = (int)1e8;
   for (int i = 0; i < n; i++)
   {
      d[i][n+1] = d[n+1][i] = xes[i].L;
      d[i][n] = d[n][i] = w-1-xes[i].R;
   }
   //for (int i = 0; i < n+2; i++, cout << endl)
   //   for (int j = 0; j < n+2; j++)
   //      cout << d[i][j] << ' ';
   r[n] = (int)1e8;
   r[n+1] = 0;
   d[n][n+1] = d[n+1][n] = w;
   for (int i = 0; i < n+2; i++) ok[i] = 0;
   for (int i = 0; i < n+2; i++)
   {
      int cur = -1;
      for (int j = 0; j < n+2; j++)
         if (!ok[j] && (cur==-1||r[cur] > r[j])) cur = j;
      ok[cur] = 1;
      for (int j = 0; j < n+2; j++)
         r[j] = min(r[j], r[cur] + d[cur][j]);
   }
   cout << "Case #" << test << ": " << r[n] << endl;
}

int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++)
   {
      solve(i);
   }
}