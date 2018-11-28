#include<cstdio>
#include<cstring>
int main()
{
	int digit[2000] = { 0 };
	int boolean[10] = { 0 };
	int now = 0;
	int ans = 0;
	int nCase = 1;
	int TEN = 0;
	int n;
	int s;
	//freopen("A-large.in", "r", stdin);
	//freopen("test.txt", "w", stdout);
	scanf("%d", &s);
	while (s--)
	{
	    scanf("%d", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", nCase);
		else
		{
			memset(boolean, 0, sizeof(boolean));
			TEN = 0;
			//n的线性递增循环
			for (int j = 1;j > 0;j++)
			{

				int b = 0;
				now = n * j;
				ans = now;
				//取位循环
				for (int i = 0;i >= 0;i++)
				{
					digit[i] = now % 10;
					now /= 10;
					if (boolean[digit[i]] == 0)
					{
						boolean[digit[i]] = 1;
						TEN++;
					}
					if (TEN == 10)
					{
						b = 1;
						break;
					}
					if (now == 0)
					{
						break;
					}
				}
				if (b == 1)
				{
					printf("Case #%d: %d\n", nCase, ans);
					break;
				}
			}
		}
		nCase++;
	}

	return 0;
}
