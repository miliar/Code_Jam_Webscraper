#include<stdio.h>
int a[1001];
int solve()
{
	int n, i, c=0, re=0;
	scanf("%d", &n);
	for(i=0; i<=n; i++)scanf("%1d", a+i);
	for(i=0; i<=n; i++)
	{
		if(i <= c) c+=a[i];
		else
		{
			re += i-c;
			c = i+a[i];
		}
	}
	return re;
}
int main()
{
	int T, i;
	scanf("%d", &T);
	for(i=1; i<=T; i++)
	{
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}