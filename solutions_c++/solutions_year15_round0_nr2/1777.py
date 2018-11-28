#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

int n, mx;
int a[2000];

bool can(int limit)
{
	for (int eat = 1; eat <= mx; eat++)
	{
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			for (int parts = 1; parts <= a[i]; parts++)
			{
				if ((a[i] + parts - 1) / parts <= eat)
				{
					sum += parts - 1;
					break;
				}
			}
		}

		if (sum + eat <= limit)
			return true;
	}
	return false;
}

void Solution()
{
	cin >> n;
	mx = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
		mx = max(a[i], mx);
	}

	int ans = mx;

	for (int eat = 1; eat <= mx; eat++)
	{
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			for (int parts = 1; parts <= a[i]; parts++)
			{
				if ((a[i] + parts - 1) / parts <= eat)
				{
					sum += parts - 1;
					break;
				}
			}
		}

		ans = min(ans, eat + sum);
	}

	cout << ans;
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}