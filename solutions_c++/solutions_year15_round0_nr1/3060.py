#include <bits/stdc++.h>
using namespace std;

char str[1111];

int main()
{
	int T, S, ans, sum;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		scanf("%d%s", &S, str);

		sum = ans = 0;
		for (int s = 0; s <= S; s++)
		{
			if (sum < s)
			{
				ans += (s - sum);
				sum = s;
			}
			sum += (str[s] - '0');
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}