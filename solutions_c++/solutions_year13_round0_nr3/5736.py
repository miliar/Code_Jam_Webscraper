#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	bool c[1002];
	bool ok[1002];
	memset(c, false, sizeof(c));
	memset(ok, false, sizeof(ok));
	for (int i = 1; i <= 9; ++i)
		c[i] = c[11 * i] = true;
	for (int i = 1; i <= 9; ++i)
		for (int j = 1; j <= 9; ++j)
			c[101 * i + 10 * j] = true;
	for (int i = 1; i * i <= 1000; ++i)
		if (c[i] && c[i * i])
			ok[i * i] = true;
	int A, B;
	int sum[1002];
	sum[0] = 0;
	for (int i = 1; i <= 1000; ++i)
	{
		sum[i] = sum[i - 1];
		if (ok[i])
			sum[i]++;
	}
	int T;
	scanf("%d", &T);
	int case_num = 0;
	while ((++case_num) <= T)
	{
		scanf("%d%d", &A, &B);
		printf("Case #%d: %d\n", case_num, sum[B] - sum[A - 1]);
	}
	return 0;
}
