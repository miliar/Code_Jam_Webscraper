#include "stdio.h"
#include "memory.h"
#include "string.h"
#include "stdlib.h"

int n;

char s1[100],s2[100];

char ans1[100],ans2[100];

char best1[100],best2[100],bestdiff[100];

int len;

int compare(char a1[100],char a2[100],int x)
{
	int curdiff[30];
	memset(curdiff,0,sizeof(curdiff));
	int i,j,k;
	for (i=25;i>=0;i--)
	{
		curdiff[i] += a1[i]-a2[i];
		if (curdiff[i] < 0)
		{
			curdiff[i] += 10;
			curdiff[i-1] --;
		}
	}
	int res = 0;
	for (i=0;i<25;i++)
	{
		if (curdiff[i] > bestdiff[i])
		{
			res = 1;
			break;
		}
		if (curdiff[i] < bestdiff[i])
		{
			res = -1;
			break;
		}
	}
	if (res == 1) return 0;
	if (res == 0)
	{
		if (x == 1)
		{
			if (strcmp(best1,ans1) < 0) return 0;
			if ((strcmp(best1,ans1) == 0) && (strcmp(best2,ans2) < 0)) return 0;
		}
		if (x == 2)
		{
			if (strcmp(best2,ans2) < 0) return 0;
			if ((strcmp(best2,ans2) == 0) && (strcmp(best1,ans1) < 0)) return 0;
		}
	}
	for (i=0;i<25;i++)
	{
		bestdiff[i] = curdiff[i];
	}
	return 1;
}

void verify(int sgn)
{
	int i,j,k;
	if (sgn == 0)
	{
		for (i=0;i<20;i++)
		{
			if (bestdiff[i] != 0)
			{
				break;
			}
		}
		if (bestdiff[i] != 0)
		{
			memset(best1,0,sizeof(best1));
			memset(best2,0,sizeof(best2));
			for (i=0;i<25;i++)
			{
				best1[i] = ans1[i];
				best2[i] = ans2[i];
			}
			memset(bestdiff,0,sizeof(bestdiff));
			return;
		}
		if (strcmp(best1,ans1) < 0) return;
		if ((strcmp(best1,ans1) == 0) && (strcmp(best2,ans2) < 0)) return;
		memset(best1,0,sizeof(best1));
		memset(best2,0,sizeof(best2));
		for (i=0;i<25;i++)
			{
				best1[i] = ans1[i];
				best2[i] = ans2[i];
			}
		memset(bestdiff,0,sizeof(bestdiff));
		return;
	}
	if (sgn == 1)
	{
		if (compare(ans1,ans2,1))
		{
			memset(best1,0,sizeof(best1));
			memset(best2,0,sizeof(best2));
			for (i=0;i<25;i++)
			{
				best1[i] = ans1[i];
				best2[i] = ans2[i];
			}
		}
		return;
	}
	if (sgn == 2)
	{
		if (compare(ans2,ans1,2))
		{
			memset(best1,0,sizeof(best1));
			memset(best2,0,sizeof(best2));
			for (i=0;i<25;i++)
			{
				best1[i] = ans1[i];
				best2[i] = ans2[i];
			}
		}
		return;
	}
}

/*
d = depth
sgn :	0: equal 
	1: 1 larger
	2: 2 larger
*/
void dfs(int d,int sgn)
{
	if (d == len)
	{
		verify(sgn);
		return;
	}
	switch (sgn)
	{
		case 0:
		{
			if ((s1[d] != '?') && (s2[d] != '?'))
			{
				ans1[d] = s1[d] - '0';
				ans2[d] = s2[d] - '0';
				if (s1[d] > s2[d])
				{
					dfs(d+1,1);
					return;
				}
				if (s1[d] < s2[d])
				{
					dfs(d+1,2);
					return;
				}
				dfs(d+1,0);
				return;
			}
			if ((s1[d] == '?') && (s2[d] == '?'))
			{
				ans1[d] = 1;
				ans2[d] = 0;
				dfs(d+1,1);
				ans1[d] = 0;
				dfs(d+1,0);
				ans2[d] = 1;
				dfs(d+1,2);
				return;
			}
			if (s1[d] == '?')
			{
				ans2[d] = s2[d] - '0';
				if (s2[d] != '0')
				{
					ans1[d] = ans2[d]-1;
					dfs(d+1,2);
				}
				ans1[d] = ans2[d];
				dfs(d+1,0);
				if (s2[d] != '9')
				{
					ans1[d] = ans2[d] +1;
					dfs(d+1,1);
				}
				return;
			}
			if (s2[d] == '?')
			{
				ans1[d] = s1[d] - '0';
				if (s1[d] != '0')
				{
					ans2[d] = ans1[d]-1;
					dfs(d+1,1);
				}
				ans2[d] = ans1[d];
				dfs(d+1,0);
				if (s1[d] != '9')
				{
					ans2[d] = ans1[d] +1;
					dfs(d+1,2);
				}
				return;
			}
			break;
		}
		case 1:
		{
			ans1[d] = s1[d]-'0';
			if (s1[d] == '?') ans1[d] = 0;
			ans2[d] = s2[d]-'0';
			if (s2[d] == '?') ans2[d] = 9;
			dfs(d+1,1);
			break;
		}
		case 2:
		{
			ans1[d] = s1[d]-'0';
			if (s1[d] == '?') ans1[d] = 9;
			ans2[d] = s2[d]-'0';
			if (s2[d] == '?') ans2[d] = 0;
			dfs(d+1,2);
			break;
		}
	}
}

int main()
{
	scanf("%d",&n);
	int i,j;
	for (i=0;i<n;i++)
	{
		memset(ans1,0,sizeof(ans1));
		memset(ans2,0,sizeof(ans2));
		memset(best1,0,sizeof(best1));
		memset(best2,0,sizeof(best2));
		memset(bestdiff,0,sizeof(bestdiff));
		scanf("%s %s",s1,s2);
		j = strlen(s1);
		len = j;
		int k;
		for (k=0;k<len;k++)
		{
			best1[k] = 10;
			best2[k] = 10;
			bestdiff[k] = 10;
		}
		dfs(0,0);
		j--;
		while (j+1)
		{
			best1[j] += '0';
			best2[j] += '0';
			j--;
		}
		printf("Case #%d: %s %s\n",i+1,best1,best2);
	}	
	return 0;
}
