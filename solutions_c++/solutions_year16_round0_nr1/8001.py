#include <cstdio>
#include <cstdlib>

using namespace std;


int main()
{
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca ++)
	{
		long long n;
		scanf("%d", &n);

		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", ca);
			continue;
		}

		bool use[10];
		for (int i = 0; i < 10; i ++) use[i] = 0;

		int num = 0;

		long long N = n;
		for (int i = 1; ; i ++)
		{
			N = n * i;
			long long x = N;
			while (x > 0)
			{
				if (use[x % 10] == 0)
					use[x % 10] = 1, num ++;
				x /= 10;
			}
			if (num == 10)
			{
				printf("Case #%d: %d\n", ca, N);
				break;
			}
		}
	}
}