#include <cstdio>

void solve(void)
{
	int K;
	int C;
	int S;
	scanf("%d %d %d",&K, &C, &S);
	for (int c = 1; c < S; c++)
	{
		printf("%d ",c);
	}
	printf("%d\n",S);	
}

int main()
{
	int n;
	int c;
	scanf("%d",&c);
	for (n = 0; n < c; n++)
	{
		printf("Case #%d: ",n+1);
		solve();
	}
}
