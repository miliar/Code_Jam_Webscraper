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
#include <ctime>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);

ll arr[1000005];
ll sum[1000005];

ll S;
ll P;

inline ll F(int i)
{
   return max(sum[i]-P, S-sum[i]);
}

void solve(int test)
{
    int n, p,q,r,s;
    cin >> n >> p >> q >> r >> s;
    for (int i = 0; i < n; i++)
        arr[i] = ((ll)i * (ll)p + (ll)q) % r + s;
    
    sum[0] = 0;
    for (int i = 1; i <= n; i++)
        sum[i] = sum[i-1] + arr[i-1];
    S = sum[n];
    ll best = 0;
     int it = 0;
      
    for (int i = 0; i < n; i++)
    {
       int lb = i+1;
       int rb = n;
       P = sum[i];
       int ans = -1;
     //  if (i % 100 == 0) cerr << i << "(" << it << ")" << endl;
       while (lb <= rb)
       {
           it++;
           int mid = (lb + rb) >> 1;
           if (F(mid) > F(mid-1))
           {
               rb = mid - 1;
           } else
           {
               ans = mid;
               lb = mid + 1;
           }
       }

       if (ans == -1) ans = i+1;
       ll R = (ll)1e18;
       for (int j = ans - 1; j <= min(n, ans + 1); j++)
          R = min(R, max(sum[j] - P, S - sum[j]));
       R = max(R, P);
       best = max(best, S - R);
    }
    cout << "Case #" << test << ": " << (ld)best / (ld)S << endl;
}

int main()
{
    int t;
    cin >> t;
    cout.precision(15);
    for (int i = 1; i <= t; i++)
    {
        solve(i);
        cerr << "DONE " << i << "  " << (double)clock() / (double)CLOCKS_PER_SEC << endl;
    }
    return 0;
}