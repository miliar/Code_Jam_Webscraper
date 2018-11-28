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

int T, a[10][10], ck, b[10][10], n, use1[10], use2[10];
char s[10];

void dfs(int t){
	if(t > n) return;
	bool flag = 0;
	for(int i = 1; i <= n; ++i)
		if(!use1[i])
			for(int j = 1; j <= n; ++j)
				if(b[i][j] && !use2[j]){
					use1[i] = 1, use2[j] = 1;
					dfs(t + 1);
					use1[i] = 0, use2[j] = 0;
					flag = 1;
				}
	if(!flag) ck = 0;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
#endif
	cin >> T;
	for(int t = 1; t <= T; ++t){
		scanf("%d", &n);
		for(int i = 1; i <= n; ++i){
			scanf("%s", s + 1);
			for(int j = 1; j <= n; ++j)
				a[i][j] = s[j] - '0';
		}
		int ans = n * n;
		for(int mask = 0; mask < 1 << (n * n); ++mask){
			bool flag = 1; int us = 0;
			for(int i = 1; i <= n; ++i)
				for(int j = 1; j <= n; ++j){
					if(a[i][j] && !((mask >> ((i - 1) * n + j - 1)) & 1)) flag = 0;
					if(!a[i][j] && ((mask >> ((i - 1) * n + j - 1)) & 1)) ++us;
					b[i][j] = a[i][j] | ((mask >> ((i - 1) * n + j - 1)) & 1);
				}
			if(!flag) continue;
			ck = 1;
			memset(use1, 0, sizeof(use1));
			memset(use2, 0, sizeof(use2));
			dfs(1);
			if(ck) ans = min(ans, us);
		}
		printf("Case #%d: %d\n", t, ans);
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
