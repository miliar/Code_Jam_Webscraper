#include <cstdio>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("google_out_large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int n;
		scanf("%d", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else
		{
			int table[10] = { 0 };
			int cnt = 0, k;
			for (k = n; cnt < 10; k += n)
			{
				int tmp = k;
				while (tmp)
				{
					if (table[tmp % 10] == 0)
					{
						table[tmp % 10]++;
						cnt++;
					}
					tmp /= 10;
				}
			}
			printf("Case #%d: %d\n", i, k - n);
		}
	}
}