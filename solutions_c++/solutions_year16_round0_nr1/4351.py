#include <stdio.h>
#include <memory.h>

#define N 1000000
#define M 100

int p = 0;

void process()
{
	int n, cnt = 10, m;
	bool check[10];
	memset(check, false, sizeof(check));
	scanf("%d", &n);
	m = n;
	for (int i = 0; i < M; i++)
	{
		int cur = m;
		if (i > 0 && n == m)
			break;
		while (cur > 0)
		{
			int temp = cur % 10;
			if (!check[temp])
			{
				cnt--;
				check[temp] = true;
				if (cur == 10 && !check[0])
				{
					cnt--;
					check[0] = true;
				}
				if (cnt == 0)
					break;
			}
			
			cur /= 10;
		}
		if (cnt == 0)
		{
			printf("Case #%d: %d\n",p, m);
			return;
		}
		m += n;
	}
	printf("Case #%d: INSOMNIA\n",p);
}

int main()
{
	int c;
	scanf("%d", &c);
	for (p = 1; p <= c;p++)
	{
		process();
	}
}