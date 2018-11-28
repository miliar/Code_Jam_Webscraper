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

int T, n;

string f(int t){
	if(t == 0) return "R";
	if(t == 1) return "S";
	return "P";
}

pair<vector<int>, string> work(int n, int t){
	vector<int> res; res.resize(3);
	res[t]++;
	if(!n) return mkp(res, f(t));
	auto res1 = work(n - 1, t), res2 = work(n - 1, (t + 1) % 3);
	if(res1.se > res2.se) swap(res1, res2);
	for(int i = 0; i < 3; ++i) res[i] = res1.fi[i] + res2.fi[i];
	string s = res1.se + res2.se;
	return mkp(res, s);
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	cin >> T;
	for(int t = 1; t <= T; ++t){
		scanf("%d", &n);
		vector<int> a; a.resize(3);
		scanf("%d%d%d", &a[0], &a[2], &a[1]);
		string ans = "";
		for(int i = 0; i < 3; ++i){
			auto res = work(n, i);
			auto num = res.fi;
			if(num == a){
				if(!ans.size()) ans = res.se;
				else ans = min(ans, res.se);
			}
		}
		printf("Case #%d: ", t);
		if(ans.size()) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
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
