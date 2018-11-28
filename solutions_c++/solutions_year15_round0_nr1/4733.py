#include <stdio.h>

int naver()
{
	int n, sum=0, add=0;
	char x;

	scanf("%d ",&n);
	for(int i=0;i<=n;i++)
	{
		scanf("%c",&x);
		if( x!='0' && sum < i )
		{
			add += i-sum;
			sum = i;
		}
		sum+=x-'0';
	}

	return add;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int tcn;
	scanf("%d",&tcn);
	for(int tc=1;tc<=tcn;tc++)
	{
		printf("Case #%d: %d\n",tc,naver());
	}

	return 0;
}