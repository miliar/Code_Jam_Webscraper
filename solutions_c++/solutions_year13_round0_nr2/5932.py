#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int n,m;
int a[100][100];
int check[100][100];

int rowprobe(int i,int j)
{
	int x = a[i][j];
	int k;
	for(k = 0;k<j;k++)
	{
		if(a[i][k]>x)
		{
			return 0;
		}
	}
	for(k=j+1;k<m;k++)
	{
		if(a[i][k]>x)
			return 0;
	}
	for(k=j+1;k<m;k++)
	{
		if(a[i][k]<x)
			check[i][k]=1;
		else
			check[i][k]=3;
	}
	return 1;
}

int colprobe(int i,int j)
{
	int x = a[i][j];
	int k;
	for(k = 0;k<i;k++)
	{
		if(a[k][j]>x)
		{
			return 0;
		}
	}
	for(k=i+1;k<n;k++)
	{
		if(a[k][j]>x)
			return 0;
	}
	for(k=i+1;k<n;k++)
	{
		if(a[k][j]<x)
			check[k][j]=1;
		else
			check[k][j]=3;
	}
	return 1;
}

int main()
{
	int t,i,j,k;
	bool found;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				if(a[i][j]!=100)
					check[i][j] = 0;
				else
					check[i][j] = 3;
			}
		}
		found = 1;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(check[i][j]==3)
					continue;
				if(check[i][j]==-1)
				{
					found = 0;
					break;
				}
				if(check[i][j]==1)
				{
					if(colprobe(i,j))
					{
						check[i][j] = 3;
					}
					else
					{
						found = 0;
						break;
					}
				}
				if(check[i][j]==2)
				{
					if(rowprobe(i,j))
						check[i][j] = 3;
					else
					{
						found = 0;
						break;
					}
				}
				else
				{
					if(rowprobe(i,j))
					{
						check[i][j] = 3;
					}
					else if(colprobe(i,j))
					{
						check[i][j] = 3;
					}
					else
					{
						found = 0;
						break;
					}
				}
			}
		}
		printf("Case #%d: ",k);
		if(found)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}