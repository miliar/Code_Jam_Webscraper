#include <iostream>
using namespace std;
int arr[4][4];
int arr2[4][4];
int a[20];
int b[20];
int r1, r2;

void solve(int tc)
{
	int i, j, k, ans;
	scanf("%d", &r1);
	for (i = 1; i <= 16; i++)
	{
		a[i] = b[i] = 0;
	}
	for (i = 1; i <= 4; i++)
	{
		int v = 0;
		if (i == r1)
		{
			v = 1;
		}
		for (j = 0; j < 4; j++)
		{
			scanf("%d", &k);
			a[k] = v;
		}
	}
	scanf("%d", &r2);
	for (i = 1; i <= 4; i++)
	{
		int v = 0;
		if (i == r2)
		{
			v = 1;
		}
		for (j = 0; j < 4; j++)
		{
			scanf("%d", &k);
			b[k] = v;
		}
	}
	k = 0;
	for (i = 1; i <= 16; i++)
	{
		if (a[i] == b[i] && a[i] == 1)
		{
			k++;
			ans = i;
		}
	}
	if (k == 1)
	{
		printf("Case #%d: %d\n", tc, ans);
	}
	else if (k == 0)
	{
		printf("Case #%d: Volunteer cheated!\n", tc);
	}
	else
	{
		printf("Case #%d: Bad magician!\n", tc);
	}	
}
int main()
{
//	freopen("c:\\data\\A-small-attempt0.in", "r", stdin);
//	freopen("c:\\data\\A-small-attempt0.out", "w", stdout);
	
	int tc;
	scanf("%d", &tc);
	int i;
	for (i = 1; i <= tc; i++)
	{
		solve(i);
	}
	return 0;
}