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

int a[2005], b[2005], ca[2005], cb[2005], x[2005];
int pa[2005], pb[2005];
int n;
   
bool go(int i)
{
   if (i==n) return 1;
 //  cout << "i=" << i << endl;
 //  for (int j = 0; j < n; j++) cout << x[j] << ' ';
 //     cout << endl;
      
   bool ok = 0;
   for (int j = 0; j < n; j++)
   {
      if (x[j] != 0) continue;
      pa[0] = ca[0];
      for (int k = 1; k < n; k++) pa[k] = max(pa[k-1], ca[k]);
      pb[n-1] = cb[n-1];
      for (int k = n-2; k >= 0; k--) pb[k] = max(pb[k+1], cb[k]);
      
      int ma = (j==0?0:pa[j-1]) + 1;
      int mb = (j==n-1?0:pb[j+1]) + 1;
      if (ma == a[j] && mb == b[j])
      {                    
         x[j] = i+1;
         ca[j] = ma;
         cb[j] = mb;
         if (go(i+1)) return 1;
         x[j] = 0;
         ca[j] = 0;
         cb[j] = 0;      
      }
   }
   return 0;
}


void solve(int t)
{
   cin >> n;
   for (int i = 0; i < n; i++) cin >> a[i];
   for (int i = 0; i < n; i++) cin >> b[i];
   for (int i = 0; i < n; i++) ca[i] = cb[i] = x[i] = 0;
 /*  for (int i = 0; i < n; i++)
   {
      for (int j = 0; j < n; j++) cout << x[j] << ' ';
      cout << endl;
      bool ok = 0;
      pa[0] = ca[0];
      for (int j = 1; j < n; j++) pa[j] = max(pa[j-1], ca[j]);
      pb[n-1] = cb[n-1];
      for (int j = n-2; j >= 0; j--) pb[j] = max(pb[j+1], cb[j]);
      for (int j = 0; j < n; j++)
      {
         if (x[j] != 0) continue;
         int ma = (j==0?0:pa[j-1]) + 1;
         int mb = (j==n-1?0:pb[j+1]) + 1;
         if (ma == a[j] && mb == b[j])
         {                    
            x[j] = i+1;
            ca[j] = ma;
            cb[j] = mb;
            ok = 1;
            break;
         }
      }
      assert(ok);
   }   */
   assert(go(0));
   cerr << t << endl;
   cout << "Case #" << t << ": ";
   for (int i = 0; i < n; i++) cout << x[i] << " \n"[i==n-1];
}

int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++) solve(i);
}