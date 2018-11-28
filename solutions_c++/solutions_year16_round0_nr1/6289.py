#include<cstdio>
#include<cstdlib>

int tCase;
int solve(int n)
{
	int m=1;
	int map = 0;
	int tmp;
	while((tmp = n*m) > 0)
	{
		while(tmp > 0)
		{
			map = map | (1 << (tmp%10));
			tmp /= 10;
		}
		if(map == 1023)
			return n*m;
		m++;
	}
	return 0;
}
int main()
{
	// freopen("in.txt","w",stdout);
	// printf("1000001\n");
	// for(int i=0;i<=1000000;i++)
	// 	printf("%d\n",i);
	// exit(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	scanf("%d",&tCase);
	for(int i=1;i<=tCase;i++)
	{
		printf("Case #%d: ",i);
		scanf("%d",&n);
		int ans = solve(n);
		if(ans == 0)
			printf("INSOMNIA");
		else
			printf("%d",ans);
		printf("\n");
	}
	return 0;
}