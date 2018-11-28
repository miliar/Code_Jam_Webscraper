#include<stdio.h>

int T;
int N, M;
char a[111][111];

int Find(int l1, int l2, int dx, int dy)
{
	l1 += dx;
	l2 += dy;
	while(l1 >= 0 && l1 < N && l2 >= 0 && l2 < M)
	{
		if(a[l1][l2] != '.') return 1;
		l1 += dx;
		l2 += dy;
	}
	return 0;
}

int main(void)
{
	int l0, l1, l2, l3, l4;
	int ret;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &N, &M);
		for(l1 = 0; l1 < N; l1++) scanf("%s", a[l1]);

		ret = 0;
		for(l1 = 0; l1 < N; l1++) for(l2 = 0; l2 < M; l2++)
		{
			if(a[l1][l2] == '<')
			{
				if(Find(l1, l2, 0, -1) == 0)
				{
					ret++;
					if(Find(l1, l2, 0, -1) == 0 && Find(l1, l2, 0, 1) == 0 && Find(l1, l2, -1, 0) == 0 && Find(l1, l2, 1, 0) == 0)
					{
						ret = -1;
						goto maki;
					}
				}
			}
			else if(a[l1][l2] == '>')
			{
				if(Find(l1, l2, 0, 1) == 0)
				{
					ret++;
					if(Find(l1, l2, 0, -1) == 0 && Find(l1, l2, 0, 1) == 0 && Find(l1, l2, -1, 0) == 0 && Find(l1, l2, 1, 0) == 0)
					{
						ret = -1;
						goto maki;
					}
				}
			}
			else if(a[l1][l2] == 'v')
			{
				if(Find(l1, l2, 1, 0) == 0)
				{
					ret++;
					if(Find(l1, l2, 0, -1) == 0 && Find(l1, l2, 0, 1) == 0 && Find(l1, l2, -1, 0) == 0 && Find(l1, l2, 1, 0) == 0)
					{
						ret = -1;
						goto maki;
					}
				}
			}
			else if(a[l1][l2] == '^')
			{
				if(Find(l1, l2, -1, 0) == 0)
				{
					ret++;
					if(Find(l1, l2, 0, -1) == 0 && Find(l1, l2, 0, 1) == 0 && Find(l1, l2, -1, 0) == 0 && Find(l1, l2, 1, 0) == 0)
					{
						ret = -1;
						goto maki;
					}
				}
			}
		}
maki:
		printf("Case #%d:", l0);
		if(ret == -1)
		{
			printf(" IMPOSSIBLE\n");
		}
		else
		{
			printf(" %d\n", ret);
		}
	}
}
