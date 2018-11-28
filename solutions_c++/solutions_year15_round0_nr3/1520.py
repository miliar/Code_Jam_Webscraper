#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<math.h>
#include<queue>
#include<set>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
int t, n, m;
string g, v;
bool pre[10000], suf[10000];
int mat[4][4] = { { 0, 1, 2, 3 }, { 1, 0, 3, 2 }, { 2, 3, 0, 1 }, { 3, 2, 1, 0 } };
bool neg[4][4] = { { 0, 0, 0, 0 }, { 0, 1, 0, 1 }, { 0, 1, 1, 0 }, { 0, 0, 1, 1 } };
int dp[4][10000];
int calc(int c, int i){
	if (c == 4)
		return 1;
	if (i == g.size())
		return 0;
	if (dp[c][i] != -1)
		return dp[c][i];
	int ret = 0;
	int pos = 0;
	int s = 0;
	for (int k = i; k < g.size() && !ret; ++k){
		s += neg[pos][g[k]];
		pos = mat[pos][g[k]];
		int M = pos;
		if (s & 1)
			M *= -1;
		if (M == c && c < 3)
			ret |= calc(c + 1, k + 1);
		else if (M == c && c == 3 && k + 1 == g.size())
			ret |= calc(c + 1, k + 1);
	}
	return dp[c][i] = ret;
}
int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> n >> m >> v;
		for (int i = 0; i < n; ++i){
			if (v[i] == 'i')
				v[i] = 1;
			else if (v[i] == 'j')
				v[i] = 2;
			else v[i] = 3;
		}
		g = v;
		for (int i = 1; i < m; ++i)
			g += v;
		//memset(pre, 0, sizeof(pre));
		//memset(suf, 0, sizeof(pre));
		bool one = 1, three = 1;
		memset(dp, -1, sizeof(dp));
		/*int j = g.size() - 1;
		int pos = g[0], pos2 = g[j];
		int s = 0, ss = 0;
		for (int i = 1; i < n; ++i){
			--j;
			s += neg[pos][g[i]];
			ss += neg[pos2][g[j]];
			pos = mat[pos][g[i]];
			pos2 = mat[pos2][g[j]];
			pre[i] = (pos == 1) && (s % 2 == 0);
			suf[i] = (pos2 == 3) && (ss % 2 == 0);
		}
		for (int i = 0; i < n; ++i){
			one |= pre[i];
			three |= suf[i];
		}*/
		if (one & three & calc(1, 0))
			printf("Case #%d: YES\n", k);
		else
			printf("Case #%d: NO\n", k);
	}
}