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


int a[1005], b[1005];

void solve(int test)
{
   cerr << test << endl;
   int n, x;
   cin >> n >> x;
   for (int i = 0; i <= x; i++) a[i] = 0;
   for (int i = 0; i < n; i++) 
   {
      int s;
      cin >> s;
      a[s]++;
   }
   int lb = 0;
   int rb = n/2;
   int ans = -1;
   while (lb <= rb)
   {
      int mid = (lb+rb)>>1;
      int rest = n - mid * 2;
      for (int i = 0; i <= x; i++) b[i] = a[i];
      int r = rest;
      for (int i = x; i >= 0 && r > 0; i--)
      {
         while (r > 0 && b[i] > 0) {b[i]--; r--;}
      }
      bool fail = 0;
      for (int i = x; i >= 0 && !fail; i--)
      {
          while (b[i] > 0 && !fail)
          {
              bool ok = 0;
              for (int j = x-i; j >= 0 && !ok; j--)
                 if (b[j])
                 {
                    b[j]--;
                    ok = 1;
                 }
              if (!ok) fail = 1;
              b[i]--;
          }
      }
      if (fail) {rb = mid - 1;}
      else
      {
         ans = mid; 
         lb = mid + 1;
      }
   }
   assert(ans != -1);
   cout << "Case #" << test << ": " << ans + (n - ans*2) << endl;
}


int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}