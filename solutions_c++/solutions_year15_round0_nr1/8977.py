
#include <iostream>
#include <cstdio>
using namespace std;

int N,au[1000];

int up(int smax,int fa)
{
	int p = 0, fark = fa;
	for (int j = 0; j <= smax; j++)
	{
		if (au[j] == 0)continue;
		else if (j <= p)
		{
			p += au[j];
		}
		else
		{
			au[0]++;
			return up(smax,fa+1);
		}
	}
	return fa;
}

int main()
{
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		int smax;
		scanf("%d", &smax);
		for (int j = 0; j <= smax; j++)
		{
			scanf("%1d", &au[j]);
		}
		
		printf("Case #%d: %d\n", i + 1, up(smax, 0));
	}
}