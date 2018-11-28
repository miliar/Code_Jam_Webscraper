#include <stdio.h>

int F = 0;
int N;
void CheckN(int T)
{
	while (T)
	{
		F |= (0x1 << (T % 10));

		T /= 10;
	}

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	setbuf(stdout, NULL);


	int T;
	scanf("%d", &T);


	for (int i = 1; i <= T; i++)
	{
		int ans = 0;

		N=F = 0;
		scanf("%d", &N);


		int NN = N;
		if (N)
		{
			while (F < 0x3FF)
			{
				CheckN(NN);
				ans++;

				if (F == 0x3FF)
					break;

				NN += N;
			}
		}


		if (ans == 0)
		{
			printf("Case #%d: INSOMNIA\n", i);
		}
		else
		{
			printf("Case #%d: %d\n", i, NN);
		}

	}

	return 0;
}