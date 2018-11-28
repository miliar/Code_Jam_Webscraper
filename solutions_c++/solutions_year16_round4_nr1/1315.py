#include "stdio.h"
#include "string.h"
#include "math.h"
#include "memory.h"

const char trans[3] = {'P','R','S'};

//P,R,S
int ans[15][3];

int n;

char buf[50000];

int count = 0;

void dfs(int d,int cur)
{
	if (d == n)
	{
		buf[count] = trans[cur];
		count ++;
		return;
	}
	if (cur == 0)
	{
		dfs(d+1,cur);
		dfs(d+1,cur+1);
		return;
	}
	else
	if (cur == 1)
	{
		dfs(d+1,1);
		dfs(d+1,2);
		return;
	}
	else
	{
		dfs(d+1,0);
		dfs(d+1,2);
	}
}

int main()
{
	int i,j,k;
	ans[0][0] = 1;
	ans[0][1] = 0;
	ans[0][2] = 0;
	for (i=0;i<=13;i++)
	{
		ans[i+1][0] = ans[i][0] + ans[i][2];
		ans[i+1][1] = ans[i][0] + ans[i][1];
		ans[i+1][2] = ans[i][1] + ans[i][2];
	}
	
	int t;
	scanf("%d",&t);
	for (i=0;i<t;i++)
	{
		int p,r,s;
		count = 0;
		scanf("%d %d %d %d",&n,&r,&p,&s);
		printf("Case #%d: ",i+1);
		memset(buf,0,sizeof(buf));
		if ((ans[n][0] == p) && (ans[n][1] == r) && (ans[n][2] == s))
		{
			dfs(0,0);
		}
		else
		if ((ans[n][0] == r) && (ans[n][1] == s) && (ans[n][2] == p))
		{
			dfs(0,1);
		}
		else
		if ((ans[n][0] == s) && (ans[n][1] == p) && (ans[n][2] == r))
		{
			dfs(0,2);
		}
		else
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		int time = 1;
		j=2;
		while (time<=n)
		{
			k = 0;
			while (k<r+p+s)
			{
				if (strcmp(buf+k,buf+k+j/2)>0)
				{
					int l;
					char tmp;
					for (l=0;l<j/2;l++)
					{
						tmp = buf[k+l];
						buf[k+l] = buf[k+l+j/2];
						buf[k+l+j/2] = tmp;
					}
				}
				k += j;
			}
			j *= 2;
			time ++;
		}
		printf("%s\n",buf);
	}
	return 0;
}
