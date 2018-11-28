#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

int a[5][5];
int b[5][5];
int r1, r2, cnt, mark;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		cnt = 0;
		scanf("%d", &r1);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &a[i][j]);
		scanf("%d", &r2);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				scanf("%d", &b[i][j]);
		for (int i = 1; i <= 4; ++i)
			for (int j = 1; j <= 4; ++j)
				if (a[r1][i] == b[r2][j]) {
					cnt++;
					mark = a[r1][i];
				}
		if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", cas);
		else if (cnt == 1) printf("Case #%d: %d\n", cas, mark);
		else printf("Case #%d: Bad magician!\n", cas);
	}
	return 0;
}

