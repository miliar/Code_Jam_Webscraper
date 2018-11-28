#include<stdio.h>
#include<string>

int n, m;
char data[1005];
int main(void)
{
	int T, i, j, t=0;

	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);

	scanf("%d",&T);
	while(T--)
	{
		scanf("%s %d",&data[1], &m);
		n = strlen(&data[1]);

		int ans=0;
		for(i=1;i<=n-m+1;i++)
		{
			if(data[i]=='-')
			{
				ans++;
				for(j=i;j<=i+m-1;j++)
					data[j]^=6;
			}
		}

		for(i=1;i<=n;i++)
		{
			if(data[i]=='-')
				break;
		}

		t++;
		printf("Case #%d: ",t);
		if(i==n+1)
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");

	}
}