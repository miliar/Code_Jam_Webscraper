#include <stdio.h>
int n, k, c, s;
int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D_small_result.txt", "w", stdout);
	scanf("%d", &n);
	for(int i=1;i<=n;i++)
	{
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", i);
		for(int j=1;j<=k;j++)
		{
			printf(" %d", j);
		}
		puts("");
		
	}
	
	
	return 0;
}
