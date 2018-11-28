#include <stdio.h>
using namespace std;

void visit(long long int N, bool vis[])
{
	while(N != 0)
	{
		vis[N % 10] = true;
		N /= 10;
	}
}

int main()
{
	long long int T, N, count = 0, j, i;
	bool vis[10], all;

	scanf("%lld", &T);

	while(T--)
	{
		count++;
		scanf("%lld", &N);
		if(N == 0)
		{
			printf("Case #%lld: INSOMNIA\n", count);
			continue;
		}
		for(i = 0; i <= 9; i++)
		{
			vis[i] = false;
		}
		all = false;
		j = 1;

		while(all != true)
		{
			visit(j * N, vis);
			all = true;

			for(i = 0; i <= 9; i++)
			{
				if(vis[i] == false)
				{
					all = false;
				}
			}
			j++;
		}
		printf("Case #%lld: %lld\n", count, (j - 1) * N);
	}
	return 0;
}