//看看会不会爆int!
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define FOR(i, l, r) for(int i = l; i <= r; i++)
#define ROF(i, r, l) for(int i = r; i >= l; i--)
#define all(a) a.begin(), a.end()

int T, n, k;
double a[300], f[300][300], g[300][300];

int main(){
#ifndef ONLINE_JUDGE
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	cin >> T;
	for(int t = 1; t <= T; ++t){
		scanf("%d%d", &n, &k);
		for(int i = 1; i <= n; ++i) scanf("%lf", a + i);
		sort(a + 1, a + n + 1);
		memset(f, 0, sizeof(f));
		memset(g, 0, sizeof(g));
		f[0][0] = 1;
		for(int i = 1; i <= n; ++i){
			for(int j = 1; j <= i; ++j)
				f[i][j] = f[i - 1][j - 1] * a[i] + f[i - 1][j] * (1 - a[i]);
			f[i][0] = f[i - 1][0] * (1 - a[i]);
		}
		g[n + 1][0] = 1;
		for(int i = n; i >= 1; --i){
			for(int j = 1; i + j - 1 <= n; ++j)
				g[i][j] = g[i + 1][j - 1] * a[i] + g[i + 1][j] * (1 - a[i]);
			g[i][0] = g[i + 1][0] * (1 - a[i]);
		}
		double ans = 0;
		for(int i = 0; i <= k; ++i){
			double res = 0;
			for(int j = 0; j <= i && j <= k / 2; ++j)
				res += f[i][j] * g[n - (k - i) + 1][k / 2 - j];
			ans = max(ans, res);
		}
		printf("Case #%d: %.8f\n", t, ans);
	}
  return 0;
}
/*
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         佛祖保佑       永无BUG
*/
