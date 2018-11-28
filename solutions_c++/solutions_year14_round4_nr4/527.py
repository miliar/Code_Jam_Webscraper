#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int cas, n, m, ans, num;
int u[10], f[10];
string ch[10];
set<string> ss;

int calc()
{
	int ret = m; string st;
	for (int i = 0; i < m; i++) {
		ss.clear();
		for (int j = 0; j < n; j++) {
			if (u[j] != i) continue;
			st = "";
			for (int k = 0; k < ch[j].size(); k++) {
				st += ch[j][k];
				if (ss.count(st)) continue;
				++ret; ss.insert(st);
			}
		}
	}
	return ret;
}

void dfs(int x)
{
	if (x == n) {
		for (int i = 0; i < m; i++)
			if (f[i] == 0) return;
		int tmp = calc();
		if (tmp == ans) ++num; else if (tmp > ans){
			ans = tmp; num = 1;
		}
		return;
	}
	for (int i = 0; i < m; i++) {
		u[x] = i; ++f[i];
		dfs(x + 1);
		--f[i];
	}
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		scanf("%d%d", &n, &m); ans = 0; num = 1;
		for (int i = 0; i < n; i++) 
			cin >> ch[i];
		dfs(0);
		printf("Case #%d: %d %d\n", t, ans, num);
	}
	return 0;
}

