#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <queue>

using namespace std;

int p1[4][4], p2[4][4];
int r1, r2;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		scanf("%d", &r1);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++)
				scanf("%d", &p1[i][j]);
		}
		scanf("%d", &r2);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++)
				scanf("%d", &p2[i][j]);
		}

		vector<int> ans;
		for (int i = 1; i <= 16; i++)
		{
			int b1 = -1, b2 = -1;
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					if (i == p1[j][k])
						b1 = j;
					if (i == p2[j][k])
						b2 = j;
				}
			}
			if (b1 == r1 - 1 && b2 == r2 - 1)
				ans.push_back(i);
		}
		if (ans.size() == 1)
			printf("Case #%d: %d\n", tt + 1, ans[0]);
		else if (ans.size() > 1)
			printf("Case #%d: Bad magician!\n", tt + 1);
		else
			printf("Case #%d: Volunteer cheated!\n", tt + 1);
	}
	

	return 0;
}