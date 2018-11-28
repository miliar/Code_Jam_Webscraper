#define MAXN 1000
#define INF 1000
#include <cstdio>

int ntest;
int D;
int P[MAXN + 5];

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		scanf("%d", &D);
		for(int i = 0;i < D;++i)
			scanf("%d", &P[i]);
		int mini = INF;
		for(int i = INF;i >= 1;--i)
		{
			int cost = 0;
			int limit = i;
			int minp = 0;
			for(int j = 0;j < D;++j)
				if(P[j] > limit)
				{
					int npart = P[j] / limit;
					if(P[j] % limit == 0)
						--npart;
					cost += npart;
					minp = limit;
				}
				else if(P[j] > minp)
					minp = P[j];
			cost += minp;
			if(cost < mini)
			{
				mini = cost;
				
			}
		}
		printf("Case #%d: %d\n", test, mini);
	}
}
