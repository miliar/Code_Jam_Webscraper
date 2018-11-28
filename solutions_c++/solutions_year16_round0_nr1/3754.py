#include <stdio.h>


int t, n, count[15];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A_large_result.txt", "w", stdout);
	scanf("%d", &t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d", &n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		int g = n;
		while(1)
		{
			int f = g;
			while(1)
			{
				count[f%10]=1;
				f/=10;
				if(f==0)break;
			}
			int s=0;
			for(int j=0;j<10;j++)
			{
				s+=count[j];
			}
			if(s==10)
			{
				printf("Case #%d: %d\n", i, g);
				break;
			}
			g+=n;
		}
		for(int j=0;j<10;j++)
		{
			count[j]=0;
		}
	}
	return 0;
}
