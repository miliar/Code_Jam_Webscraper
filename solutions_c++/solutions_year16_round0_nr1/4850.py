#include <bits/stdc++.h>
using namespace std;

/*
*/

int solve(int x)
{
	if (x == 0)
		return -1;
	int msk = 0;
	int cur = 0;
	while (msk != (1<<10) - 1)
	{
		cur += x;
		int cur2 = cur;
		while (cur2)
		{
			msk |= (1<<(cur2 % 10));
			cur2 /= 10;
		}
	}
	return cur;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		int x;
		scanf("%d", &x);
		int r = solve(x);
		
		if (r == -1)
		{
			printf("Case #%d: INSOMNIA\n", z);
		}
		else
		{
			printf("Case #%d: %d\n", z, r);
		}
	}
}