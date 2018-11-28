#include<stdio.h>
#include<math.h>
#include<string.h>
bool isPalindrome(long long int value)
{
	char data[1005]={0};
	sprintf(data, "%lld", value);
	int len = strlen(data);
	for(int i = 0 ; i < len / 2 ; i++)
	{
		if(data[i]!=data[len-i-1]) return false;
	}
	return true;
}
int main()
{
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int Case = 1 ; Case <= T ; Case++)
	{
		long long int n,m;
		scanf("%lld%lld",&n,&m);
		int start = sqrt((long double)n), end = sqrt((long double)m);
		long long int count=0;
		if(start*start < n) start++;
		for(int i = start ; i <= end ; i++)
		{
			if(isPalindrome(i*i) && isPalindrome(i))
			{
				count++;
			}
		}
		printf("Case #%d: %lld\n",Case,count);
	}
	return 0;
}
/*
#include<stdio.h>
int n,m;
int data[105][105];
int _x[]={0,-1,1,0}, _y[]={-1,0,0,1};
void DFS(int x, int y, int value)
{
	if(data[x][y]!=value) return;
	data[x][y]=-1;
	for(int i = 0 ; i < 4 ; i++)
	{
		DFS(x+_x[i], y+_y[i], value);
	}
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int Case = 1 ; Case <= T ; Case++)
	{
		scanf("%d%d",&n,&m);
		for(int i = 1 ; i <= n ; i++)
		{
			for(int j = 1 ; j <= m ; j++)
			{
				scanf("%d",&data[i][j]);
			}
		}
		for(int i = 1 ; i <= n ; i++)
		{
			if(data[i][1] > 0)
			{
				DFS(i, 1, data[i][1]);
			}
			if(data[n][i] > 0)
			{
				DFS(n, i, data[n][i]);
			}
		}
		for(int i = 1 ; i <= m ; i++)
		{
			if(data[1][i] > 0)
			{
				DFS(1, i, data[1][i]);
			}
			if(data[n][i] > 0)
			{
				DFS(n, i, data[n][i]);
			}
		}
		bool result=true;
		for(int i = 1 ; i <= n ; i++)
		{
			for(int j = 1 ; j <= m ; j++)
			{
				if(data[i][j]>0)
				{
					result = false;
					break;
				}
			}
		}
		if(result)
			printf("Case #%d: YES\n", Case);
		else
			printf("Case #%d: NO\n",Case);
	}
	return 0;
}
*/