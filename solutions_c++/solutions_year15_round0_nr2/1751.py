#include <stdio.h>

int n;
int a[2000];

int main()
{
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(TT=0;TT<T;TT++)
	{
		int i, j, k;
		scanf("%d", &n);
		for(i=0;i<n;i++) scanf("%d", &a[i]);
		int max=0;
		for(i=0;i<n;i++)
		{
			if(max < a[i]) max=a[i];
		}
		int dab=0x7fffffff;
		for(i=1;i<=max;i++)
		{
			int sum=0;
			for(j=0;j<n;j++)
			{
				int u;
				if(a[j]%i == 0)
				{
					u=a[j]/i;
				}
				else u=a[j]/i+1;
				sum += u-1;
			}
			if(dab > sum+i) dab=sum+i;
		}
		printf("Case #%d: %d\n", TT+1, dab);
	}
}