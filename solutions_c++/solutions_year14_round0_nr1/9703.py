//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

int shift(int n, int k)
{
	if (n%k == n%(k/10))
		return 0;

	int ans = n%k, nn=n/k;
	while (nn) { ans *= 10; nn/=10; }
	ans += n/k;
	return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T, t, r0, r1;
	int mat0[4][4], mat1[4][4];
	int row0[4], row1[4];
	bool inRow0[17], inRow1[17];

	scanf("%d", &T);
	for (t=1; t<=T; ++t)
	{
		scanf("%d", &r0); --r0;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
				scanf("%d", &mat0[i][j]);
		}

		scanf("%d", &r1); --r1;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
				scanf("%d", &mat1[i][j]);
		}
	
		memset(inRow0, 0, sizeof(inRow0));	
		memset(inRow1, 0, sizeof(inRow1));

		for (int i = 0; i < 4; ++i)
		{
			inRow0[mat0[r0][i]] = 1;
			inRow1[mat1[r1][i]] = 1;
		}

		int cnt = 0;
		int ans = -1;
		for (int i = 1; i <= 16; ++i)
		{
			if (inRow0[i] && inRow1[i])
			{
				++cnt;
				ans = i;
			}
		}

		if (cnt == 1)
		{
			printf("Case #%d: %d\n", t, ans);
		}
		else if (cnt > 1)
		{
			printf("Case #%d: Bad magician!\n", t);
		}
		else
			printf("Case #%d: Volunteer cheated!\n", t);
	}
}
