#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(x) (x) * (x)
#define forn(i, l, r) for(int i = l; i < r; i ++)                      
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it ++)
#define y1 salnk
#define N 200100              
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;

int t, n, k, cnt[N], s, antimask;
double p[N], dp[N], pd[N], cur, res;

int get(int x) {
 	int res = 0;
 	for (int i = 0; i < 30; i++)
 		if (x & (1<<i))res++;
 	return res;
}

int main () {
    //freopen("in", "r", stdin);
       cin >> t;
       int qq = 0;
       
       for (int i = 0; i < (1 << 16); i++)
       	cnt[i] = get(i);

       while (t--) {
        	cin >> n >> k;
        	qq++;
        	for (int i = 0; i < n; i++) 	
        		cin >> p[i];
          for (int mask = 0; mask < (1<<n); mask++) {
           	if (cnt[mask] * 2 != k) continue;
           	dp[mask] = 1.0;
           	pd[mask] = 1.0;
           	for (int i = 0; i < n; i++)
           		if (mask & (1<<i)) {
           		 	dp[mask] *= p[i];
           		 	pd[mask] *= (1-p[i]);
           		}

          }

        	res = 0;

        	for (int mask = 0; mask < (1 << n); mask++) {
        	 	if (cnt[mask] != k) continue;
        	 
        	 	s = mask;
        	 	cur = 0;
        	 	while (s > 0) {
        	 	 	if ((cnt[s] << 1) == k) {
        	 	 	   antimask = mask ^ s;
        	 	 	   cur += dp[s] * pd[antimask];
        	 	 	}
        	 	 	s = (s-1) & mask;
        	 	}
        	 	res = max(res, cur);
        	}
        	cout << "Case #" << qq << ": ";
        	printf("%.10f\n", res);
       }
       return 0;
}