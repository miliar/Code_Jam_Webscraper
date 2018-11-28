#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000 + 10;

char k[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int cas = 0;
	while (T--)
	{
		int smax;
		scanf("%d%s", &smax, k);
		int sum = 0, num = 0;
		for (int i = 0; i <= smax; ++i)
		{
			if (num >= i)
			{
				num += k[i] - '0';
			}
			else
			{
				sum += i - num;
				num = i + k[i] - '0';
			}
		}
		printf("Case #%d: %d\n", ++cas, sum);
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}