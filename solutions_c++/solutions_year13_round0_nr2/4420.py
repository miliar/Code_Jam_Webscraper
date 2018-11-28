#include <bits/stdc++.h>

using namespace std;

int a[101][101],visited[101][101],n,m;

pair<int,int> findmin()
{
	int minm = 1000000;
	int i,j;
	pair<int,int > minidx(-1,-1);
	for(i = 0;i < n;i++)
	{
		for(j = 0;j < m;j++)
		{
			if(visited[i][j]==0)
			{
				if(minm > a[i][j])
				{
					minm = a[i][j];
					minidx = make_pair(i,j);
				}
			}
		}
	}
	return minidx;
}

int main()
{
	int k,i,j,t,flag,tflag;
	pair<int,int > idx;
	scanf("%d",&t);
	for(k = 1;k <= t;k++)
	{
		memset(visited,0,sizeof(visited));
		scanf("%d %d",&n,&m);
		for(i = 0;i < n;i++)
		{
			for(j = 0;j < m;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}	
		tflag = 0;
		while(1)
		{
		
			idx = findmin();
			if(idx.first == -1)
			{
				break;
			}
			flag =0 ;
			for(j = 0;j < m;j++)
			{
				if((visited[idx.first][j]==0) && (a[idx.first][j] != a[idx.first][idx.second]))
				{
					flag = 1;
					break;
				}
			}	
			if(flag == 0)
			{
				for(j = 0;j < m;j++)
				{
					visited[idx.first][j] = 1;
				}	
			}
			else
			{
				flag = 0;
				for(i = 0;i < n;i++)
				{
					if((visited[i][idx.second] == 0) && (a[i][idx.second] != a[idx.first][idx.second]))
					{
						flag = 1;
						break;
					}
				}	
				if(flag == 0)
				{
					for(i = 0;i < n;i++)
					{
						visited[i][idx.second] = 1;
					}	
				}
				else
				{
					tflag = 1;
					break;
				}
			}
		}
		if(tflag == 1)
		{
			printf("Case #%d: NO\n",k);
		}
		else
		{
			printf("Case #%d: YES\n",k);
		}
	}
	return 0;
}
