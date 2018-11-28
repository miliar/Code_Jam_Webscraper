#include <cstdio>
using namespace std;

#define BIT(y,x) (1 << ((y)*(w)+(x)))

int doit()
{
	int w, h, n;
	scanf("%d %d %d", &w, &h, &n);
	int ret = 4*n;
	for (int i = 0; i < (1 << (w*h)); ++i)
	{
		int bits = 0;
		for (int j = 0; (1 << j) <= i; ++j)
		{
			if ((i & (1 << j)) != 0)
				++bits;
		}
		if (bits != n)
			continue;
		int cost = 0;
		for (int y = 1; y < h; ++y)
		{
			for (int x = 0; x < w; ++x)
			{
				int me = i & BIT(y,x);
				int other = i & BIT(y-1,x);
				if (me != 0 && other != 0)
					++cost;
			}
		}
		for (int y = 0; y < h; ++y)
		{
			for (int x = 1; x < w; ++x)
			{
				int me = i & BIT(y,x);
				int other = i & BIT(y,x-1);
				if (me != 0 && other != 0)
					++cost;
			}
		}
		if (cost < ret)
		{
			ret = cost;
			/*
			printf("%d", cost);
			for (int y = 0; y < h; ++y)
			{
				printf(" ");
				for (int x = 0; x < w; ++x)
					printf("%d", (BIT(y,x) & i) != 0 ? 1 : 0);
			}
			printf("\n");
			*/
		}
	}
	return ret;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int ret = doit();
		printf("Case #%d: %d\n", i+1, ret);
	}
	return 0;
}
