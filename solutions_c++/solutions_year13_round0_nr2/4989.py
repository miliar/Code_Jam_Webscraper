#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<functional>

int checkrow(int pat[100][100],int lawn[100][100],int m,int row,int num)
{	
	for(int x=0;x<m;x++)
	{
		if(num < pat[row][x])
		{
			return 0;
		}
	}
	return 1;
}
int checkcol(int pat[100][100],int lawn[100][100],int n,int col,int num)
{	
	for(int x=0;x<n;x++)
	{
		if(num < pat[x][col])
			return 0;
	}
	
	return 1;
}
int findpos(int pat[100][100],int lawn[100][100],int n,int m,int num,int *row,int *col)
{
	for(int x=0;x<n;x++)
	{
		for(int y=0;y<m;y++)
		{
			if(pat[x][y]==num)
			{
				if(pat[x][y]!=lawn[x][y])
				{
					*row=x;
					*col=y;
					return 1;
				}
			}
		}
	}
	return 0;
}
int main()
{
	int t,n,m;
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int pat[100][100],lawn[100][100]={0},max=0;
		int r,c;
		std::set<int, std::greater<int>> heights;
		std::set<int, std::greater<int>>::iterator it;
		scanf("%d %d",&n,&m);
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				scanf("%d",&pat[j][k]);
				if(max<pat[j][k])
					max=pat[j][k];
				heights.insert(pat[j][k]);
			}
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				lawn[j][k]=max;
			}
		}
		it=heights.begin();
		it++;
		while(it!=heights.end())
		{
			int num=*it;
			
			if(findpos(pat,lawn,n,m,num,&r,&c))
			{	
				if(checkrow(pat,lawn,m,r,num))
				{
					for(int x=0;x<m;x++)
					{
						lawn[r][x]=num;
					}
				}
				else if(checkcol(pat,lawn,n,c,num))
				{
					for(int x=0;x<n;x++)
					{
						lawn[x][c]=num;
					}
				}
				else
					break;
			}
			else
			{
				it++;
			}
		}
		printf("Case #%d: ",i);
		if(it==heights.end())
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}