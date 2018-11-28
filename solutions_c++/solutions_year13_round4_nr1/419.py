
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;

int l[100005], r[100005], p[100005];
ll n;
int m;
ll mod = 1000002013ll;


ll cost (int L)
{
  ll ans = n*(ll)L - (ll)L*(ll)(L-1)/2ll;
  return ans % mod;
}
void solve(int t)
{
   cin >> n >> m;
   for (int i = 0; i < m; i++)
   {
      cin >> l[i] >> r[i] >> p[i];
   }

   ll ans = 0ll;
   for (int it = 0; ; it++)
   {
      cerr << "it=" << it << endl;
      bool ok = 0;
      for (int i = 0; i < m; i++)
         for (int j = i+1; j < m; j++)
            if (p[i] > 0 && p[j] > 0)
            {
               if (l[i] <= l[j] && r[i] >= r[j]) continue;
               if (l[j] <= l[i] && r[j] >= r[i]) continue;
               if (max(l[i], l[j]) > min(r[i], r[j])) continue;
               l[m] = min(l[i], l[j]);
               r[m] = max(r[i], r[j]);
               p[m] = min(p[i], p[j]);
               m++;
               l[m] = max(l[i], l[j]);
               r[m] = min(r[i], r[j]);
               p[m] = min(p[i], p[j]);
               m++;
               ans -= cost(r[i]-l[i])*(ll)p[m-1] % mod;
               ans += mod;
               ans -= cost(r[j]-l[j])*(ll)p[m-1] % mod;
               ans += mod;
               ans %= mod;
               ans += cost(r[m-1]-l[m-1])*(ll)p[m-1] % mod;
               ans %= mod;
               ans += cost(r[m-2]-l[m-2])*(ll)p[m-1] % mod;
               ans %= mod;             

               p[i] -= p[m-1];
               p[j] -= p[m-1];
               ok = 1;
               
            }
      if (!ok) break;
   }
   ans = mod - ans;
   ans %= mod;
   cout << "Case #" << t << ": " << ans << endl;
}


int main()
{
   int t;
   cin >> t;
   for (int i = 1; i <= t; i++) solve(i);
}
