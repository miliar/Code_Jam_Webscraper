//============================================================================
// Name        : codejam.cpp
// Author      : huangxs139
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int mat[5][5];
	bool vis[20];
	int n, ans;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		memset(vis, 0, sizeof(vis));
		ans = 0;
		scanf("%d", &n);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &mat[i][j]);
		for (int j = 1; j <= 4; j++)
			vis[mat[n][j]] = 1;
		scanf("%d", &n);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &mat[i][j]);
		for (int j = 1; j <= 4; j++)
			if (vis[mat[n][j]]) {
				if (!ans)
					ans = mat[n][j];
				else
					ans = -1;
			}
		printf("Case #%d: ", ++cas);
		if (!ans)
			printf("Volunteer cheated!\n");
		else if (ans == -1)
			printf("Bad magician!\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
