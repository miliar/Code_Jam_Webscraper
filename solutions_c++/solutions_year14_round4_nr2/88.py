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

int a[1005];
pair<int,int> u[1005];

void solve(int test)
{
   int n;
   cin >> n;
   for (int i = 0; i < n; i++) 
   {
      cin >> a[i];
      u[i] = mp(a[i], i);
   }
   sort(u, u + n);
   reverse(u, u + n);
   int ans = 0;
   for (int i = 0; i < n; i++)
   {
      int cur = u[i].second;
      int maxpos = u[0].second;
      for (int j = min(cur,maxpos); j <= max(cur, maxpos); j++)
         if (a[j] < a[cur]) ans++;
    //  cout << "i=" << i << "(" << u[i].first <<  ")" << endl;
    //  cout << "ans=" << ans << endl;
      int shouldr = 0;
      for (int j = 0; j < i; j++)
         if (u[j].second < u[i].second) shouldr++;
      int shouldl = 0;
      for (int j = 0; j < i; j++)
         if (u[j].second > u[i].second) shouldl++;
      if (cur < maxpos) ans += min(0, (i-shouldr) - shouldr);
      else ans += min(0, i - 2 * shouldl);
     // cout << "ans=" << ans << endl;
   }
   cout << "Case #" << test << ": " << ans << endl;
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