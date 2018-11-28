#include <cstdio>
#include <iostream>

using namespace std;


int n;
int a[1009];

int solve()
{
	int maxA = 0;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", a+i);
		maxA = max(maxA, a[i]);
	}

	int ans = maxA;

	for (int s = 1; s <= maxA; s++)
	{
		int t = 0;

		for (int i = 0; i < n; i++)
		{
			t += a[i] / s;

			if (a[i] % s != 0)
			{
				t++;
			}

			t--;
		}

		ans = min(ans, t + s);
	}

	return ans;
}

int main()
{
	int TC;

	cin >> TC;

	for (int tc = 1; tc <= TC; tc++)
	{
		printf("Case #%d: %d\n", tc, solve());
	}
}