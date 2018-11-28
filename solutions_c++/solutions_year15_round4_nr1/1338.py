#include <cstdio>
#include <cstdlib>
#include <climits>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <bitset>
#include <cmath>
#include <set>
using namespace std;
char g[105][105];
int n, m;
int g2[105][105][4];
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t; scanf("%d", &t);
	int kase = 0;
	while (t--){
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++)scanf("%s", &g[i]);
		memset(g2, 0, sizeof(g2));
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m;j++){
			for (int j2 = 0; j2 < j;j2++)
			if (g[i][j2] != '.')g2[i][j][0] |= 1;
			for (int j2 = j+1; j2 < m; j2++)
			if (g[i][j2] != '.')g2[i][j][1] |= 1;

			for (int i2 = 0; i2 < i; i2++)
			if (g[i2][j] != '.')g2[i][j][2] |= 1;
			for (int i2 = i+1; i2 < n; i2++)
			if (g[i2][j] != '.')g2[i][j][3] |= 1;
		}
		int ans = 0;
		bool flag = true;
		for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		if (g[i][j] != '.'){
			if (g[i][j] == '<'&&g2[i][j][0])continue;
			if (g[i][j] == '>'&&g2[i][j][1])continue;
			if (g[i][j] == '^'&&g2[i][j][2])continue;
			if (g[i][j] == 'v'&&g2[i][j][3])continue;
			if (g2[i][j][0] + g2[i][j][1] + g2[i][j][2] + g2[i][j][3] == 0)flag = false;
			ans++;
		}
		if (flag==false)printf("Case #%d: IMPOSSIBLE\n", ++kase);
		else printf("Case #%d: %d\n", ++kase,ans);
	}
	return 0;
}