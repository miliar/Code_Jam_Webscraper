//be naame khodaa

#include <bits/stdc++.h>

using namespace std;

bool mark[10];

int main()
{
	int n, t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int ans = 0, sum = 0;
		fill(mark, mark + 10, false);
		cin >> n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		while (sum < 10)
		{
			ans += n;
			int x = ans;
			while (x)
			{
				if (!mark[x%10]) sum++;
				mark[x%10] = true;
				x /= 10;
			}
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
