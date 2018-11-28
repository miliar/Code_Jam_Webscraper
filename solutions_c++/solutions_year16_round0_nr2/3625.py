#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>
#include <queue>

using namespace std;

#pragma comment(linker, "/STACK:100000000")

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define fr(i,a,b) for(int i = (a);i <= (b);i++)
#define fd(i,a,b) for(int i = (a);i >= (b);i--)

int ri(){int x;scanf("%d",&x);return x;}

int dp[1<<11];

int solve(string str) {
	int val = 0;
	for(int i = 0; i < sz(str); i++) {
		val *= 2;
		if(str[i] == '+') val++;
	}
	if(dp[val] == -2) return 1e5;
	if(dp[val] != -1) return dp[val];
	dp[val] = -2;
	int res = 1e5;
	bool ok = true;
	for(int i = 0; i < sz(str); i++) {
		if(str[i] != '+') ok = false;
	}
	if(ok) return dp[val] = 0;
	for(int i = 0; i < sz(str); i++) {
		string s = str;
		for(int j = 0; j <= i; j++) {
			if(j < i - j) {
				swap(s[j], s[i-j]);
			}
			if(s[j] == '+') s[j] = '-';
			else s[j] = '+';
		}
		res = min(res, solve(s) + 1);
	}

	return dp[val] = res;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		string s;
		cin >> s;
		memset(dp, -1, sizeof(dp));
		queue<string> q;
		int step = 0;
		int ans = -1;
		q.push(s);
		while(!q.empty()) {
			for(int i = 0, maxi = sz(q); i < maxi; i++) {
				string str = q.front();
				q.pop();
				int val = 0;
				for(int i = 0; i < sz(str); i++) {
					val *= 2;
					if(str[i] == '+') val++;
				}
				if(dp[val] != -1) continue;
				dp[val] = step;
				bool ok = true;
				for(int i = 0; i < sz(str); i++) {
					if(str[i] != '+') ok = false;
				}
				if(ok && ans == -1) ans = step;
				for(int i = 0; i < sz(str); i++) {
					string t = str;
					for(int j = 0; j <= i; j++) {
						if(j < i - j) {
							swap(t[j], t[i-j]);
						}
						if(t[j] == '+') t[j] = '-';
						else t[j] = '+';
					}
					q.push(t);
				}
			}
			step++;
		}

		printf("%d\n", ans);
	}


	return 0;
}
