#define _CRT_SECURE_NO_WARNINGS
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


int dp[1 << 10];


int reverse(int n,int bit) {
	int res = bit & ~((1<<n)-1);
	for (int i = 0; i < n;i++) {
		int b = bit >> (n - 1 - i) & 1;
		b ^= 1;
		res |= b << i;
	}
	return res;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	/*int t;
	cin >> t;
	rep(tcase, t) {
		string s;
		cin >> s;
		int n = s.size();
		memset(dp, -1, sizeof(dp));
		int bs = 0;
		rep(i, n) {
			if (s[i] == '+')bs |= 1 << i;
		}
		dp[bs] = 0;
		queue<int> q;
		q.push(bs);
		int ans = -1;
		while (1) {
			int a = q.front();
			q.pop();
			if (a == (1 << n) - 1) {
				break;
			}
			for (int i = 1; i <= n;i++) {
				int na = reverse(i, a);
				if (dp[na]==-1) {
					dp[na] = dp[a] + 1;
					q.push(na);
				}
			}
		}
		cout << "Case #" << tcase + 1 << ": " << dp[(1<<n)-1] << endl;
	}*/
	int t;
	cin >> t;
	rep(tcase, t) {
		string s;
		cin >> s;
		int n = s.size();
		int ans = 0;
		s += '+';
		rep(i,n) {
			if (s[i] != s[i + 1])ans++;
		}
		cout << "Case #" << tcase + 1 << ": " << ans << endl;
	}
	return 0;
}