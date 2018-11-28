#include<stdio.h>
int a[1001];
int solve()
{
	int n, i, j;
	scanf("%d", &n);
	for(i=1; i<=n; i++)scanf("%d", a+i);
	int min = 1000, re;
	for(i=1; i<=1000; i++)
	{
		re = i;
		for(j=1; j<=n; j++)
		{
			re += (a[j]-1)/i;
		}
		if(min > re) min = re;
	}
	return min;
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++) printf("Case #%d: %d\n", i, solve());
	return 0;
}