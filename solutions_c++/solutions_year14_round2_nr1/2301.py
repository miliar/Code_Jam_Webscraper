#include <stdio.h>
#include <string.h>
#include <limits.h>

int main()
{
	int tc, ct;
	scanf("%d",&tc);
	int i;
	int result;
	int n;
	char s[128][128];
	int pd[128][128];
	for(int ct=1;ct<=tc;ct++)
	{
		for(i=0;i<128;i++)
			for(int j=0;j<128;j++)
			{
				s[i][j]=0;
				pd[i][j] = 0;
			}
		result = 0;
		printf("Case #%d: ", ct);
		scanf("%d", &n);
		for(i=0;i<n;i++)
			scanf("%s", s[i]);
		if(n==2)
		{
			int j, k;
			if(s[0][0] != s[1][0])
			{
				puts("Fegla Won");
				continue;
			}
			pd[strlen(s[0])][strlen(s[1])] = 0;
			for(i=strlen(s[0]);i>=0;i--)
				for(j=strlen(s[1]);j>=0;j--)
				{
					int best = INT_MAX-1;
					if(s[0][i] == s[1][j])
						best = pd[i+1][j+1];
					if(j>0 && (s[0][i] == s[1][j-1]))
					{
						int best1 = 1 + pd[i+1][j];
						if(best > best1) best = best1;
					}
					if(i>0 && (s[0][i-1] == s[1][j]))
					{
						int best1 = 1 + pd[i][j+1];
						if(best > best1) best = best1;
					}
					pd[i][j] = best;
				}
			if(pd[0][0] == INT_MAX-1)
				puts("Fegla Won");
			else
				printf("%d\n", pd[0][0]);
		}
	}
	return 0;
}
