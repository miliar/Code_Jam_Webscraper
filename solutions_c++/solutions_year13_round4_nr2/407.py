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

ll f0(int i, ll j)
{
  if (j == 0ll) return 0;
  return (1ll << (i-1)) + f0(i-1, (j-1ll)/2ll);
}

ll f1(int i, ll j)
{
  if (j == (1ll<<i)-1ll) return (1ll<<i)-1ll;
  return f1(i-1, (j)/2ll+j%2ll);
}



void solve(int t)
{
   int n;
   cin >> n;
   ll p;
   cin >> p;
   ll lb = 0;
   ll rb = (1ll<<n)-1ll;
   ll ans0 = -1;
   while (lb <= rb)
   {
      ll mid = (lb + rb) >> 1;
    //  cout << "f0(" << mid << ") = " << f0(n, mid) << endl;
      if (f0(n, mid) < p)
      {
         ans0 = mid;
         lb = mid + 1ll;
      } else rb = mid - 1ll;
   }
   lb = 0;
   rb = (1ll<<n)-1ll;
   ll ans1 = -1;
   while (lb <= rb)
   {
      ll mid = (lb + rb) >> 1;
     // cout << "f1(" << mid << ") = " << f1(n, mid) << endl;
      if (f1(n, mid) < p)
      {
         ans1 = mid;
         lb = mid + 1ll;
      } else rb = mid - 1ll;
   }
   cout << "Case #" << t << ": " << ans0 << ' ' << ans1 << endl;
}


int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++) solve(i);
}