#include<stdio.h>
#include<string.h>
#include<algorithm>
int N, a[1010], cnt;
void swap(int i, int j)
{
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
	++ cnt;
}
void process()
{
	int i = 1, j = N;
	cnt = 0;
	for(;;)
	{
		if(i == j) break;
		int p = i;
		for(int k = i; k <= j; k ++)
		{
			if(a[k] < a[p]) p = k;
		}
		if(p - i < j - p)
		{
			while(p > i)
			{
				swap(p - 1, p);
				-- p;
			}
			++ i;
		}
		else
		{
			while(p < j)
			{
				swap(p, p + 1);
				++ p;
			}
			-- j;
		}
	}
	printf("%d\n", cnt);
}
int main()
{
	freopen("B-large.in", "rb", stdin);
	freopen("B-large.out", "wb", stdout);
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt ++)
	{
		scanf("%d", &N);
		for(int i = 1; i <= N; i ++)
		{
			scanf("%d", &a[i]);
		}
		printf("Case #%d: ", tt);
		process();
	}
	return 0;
}
