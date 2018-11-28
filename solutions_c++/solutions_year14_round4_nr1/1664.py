#include <cstdio>
#include <algorithm>

const int MAXN = 10005;
int t,n,x,sizes[MAXN];

int main()
{
	scanf("%d", &t);
	for(int test = 1; test <= t; ++test)
	{
		scanf("%d%d", &n, &x);
		for(int i = 0; i < n; ++i)
			scanf("%d", &sizes[i]);
		std::sort(sizes,sizes+n);
		
		int sol = 0,tmp = n-1;
		for(int i = 0; i <= tmp; ++i)
		{
			while(i < tmp && sizes[i] + sizes[tmp] > x)
				{ tmp--; sol++; }
			if(i < tmp && sizes[i] + sizes[tmp] <= x)
				tmp--;
			sol++;
		}

		printf("Case #%d: %d\n", test, sol);
	}
}
