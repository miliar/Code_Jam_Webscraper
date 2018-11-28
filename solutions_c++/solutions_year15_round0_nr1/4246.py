#include <cstdio>
int T;
int Ti;
int seq[1010];
int n;
int main()
{
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++)
	{
		scanf("%d",&n);
		int i;
		for(i=0;i<n+1;i++)
		{
			scanf("%1d",&seq[i]);
		}
		int total = 0, added = 0;
		for(i=0;i<n+1;i++)
		{
			if(total<i)
			{
				added += (i-total);
				total = i;
			}
			total += seq[i];
		}
		printf("Case #%d: %d\n", Ti, added);
	}
	return 0;
}

