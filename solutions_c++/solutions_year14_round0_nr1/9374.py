#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int p[4][4], q[4][4];
bool used[16];

int main()
{
	//cin.sync_with_stdio(0);
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif
	int t;
	scanf("%d", &t);
	int ans1, ans2;
	vector <int> ans;
	for (int i = 1; i <= t; ++i)
	{
		ans.clear();
		memset(used, 0, sizeof used);
		scanf("%d", &ans1);
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				scanf("%d", &p[j][k]);
				if (j + 1 == ans1)
					used[p[j][k] - 1] = true;
			}
		}
		scanf("%d", &ans2);
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				scanf("%d", &q[j][k]);
				if (j + 1 == ans2)
				{
					if (used[q[j][k] - 1])
						ans.push_back(q[j][k]);
				}
			}
		}
		printf("Case #%d: ", i);
		if (ans.size() == 1)
			printf("%d\n", ans[0]);
		else if (ans.size() == 0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
	}
    return 0;
}