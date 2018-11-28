#include <cstdio>
const int maxn = 1005;
int n, ans, sum;
char buf[maxn];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test, tt;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d%s", &n, buf);
		ans = sum = 0;
		for (int i = 0; i <= n; i++)
		{
			if (buf[i] == '0')
				continue;
			if (sum < i)
			{
				ans += i - sum;
				sum = i;
			}
			sum += buf[i] - '0';
		}
		printf("Case #%d: %d\n", tt, ans);
	}
}
