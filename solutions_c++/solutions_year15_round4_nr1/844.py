#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <cstring>
#include <cmath>
using namespace std;
int r,c,count1;
int vis[103][103];
char a[103][103];
int func(int i,int j,char st)
{
	if(i<0 || i>=r)
		return 0;
	if(j<0 || j>=c)
		return 0;
	if(vis[i][j]==1)
	{
		return 1;
	}
	int ret;
	if(a[i][j]=='.')
	{
		if(st=='^')
		ret = func(i-1,j,'^');
		else if(st=='v')
		ret = func(i+1,j,'v');
		else if(st=='>')
			ret = func(i,j+1,'>');
		else if(st=='<')
			ret = func(i,j-1,'<');
		else
			ret = -1;
		return ret;
	}
	if(a[i][j]=='^')
	{
		vis[i][j]=1;
		ret = func(i-1,j,'^');
		if(ret)
		{
			return 1;
		}
		ret = func(i+1,j,'v');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i,j+1,'>');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i,j-1,'<');
		if(ret)
		{
			count1++;
			return 1;
		}
		vis[i][j]=0;
		return 0;
	}
	if(a[i][j]=='v')
	{
		vis[i][j]=1;
		ret = func(i+1,j,'v');
		if(ret)
		{
			return 1;
		}
		ret = func(i-1,j,'^');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i,j+1,'>');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i,j-1,'<');
		if(ret)
		{
			count1++;
			return 1;
		}
		vis[i][j]=0;
		return 0;
	}
	if(a[i][j]=='>')
	{
		vis[i][j]=1;
		ret = func(i,j+1,'>');
		if(ret)
		{
			return 1;
		}
		ret = func(i-1,j,'^');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i+1,j,'v');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i,j-1,'<');
		if(ret)
		{
			count1++;
			return 1;
		}
		vis[i][j]=0;
		return 0;
	}
	if(a[i][j]=='<')
	{
		vis[i][j]=1;
		ret = func(i,j-1,'<');
		if(ret)
		{
			return 1;
		}
		ret = func(i-1,j,'^');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i+1,j,'v');
		if(ret)
		{
			count1++;
			return 1;
		}
		ret = func(i,j+1,'>');
		if(ret)
		{
			count1++;
			return 1;
		}
		vis[i][j]=0;
		return 0;
	}
}
int main()
{
	int t,flag;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&r);
		scanf("%d",&c);
		for(int j=0;j<r;j++)
		{
			scanf("%s",a[j]);
			for(int k=0;k<c;k++)
			{
				vis[j][k]=0;
			}
		}
		flag=1;
		count1=0;
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				if(func(j,k,'.')==0)
				{
					flag=0;
					break;
				}
			}
			if(flag==0)
			{
				break;
			}
		}
		if(flag)
		{
			printf("Case #%d: %d\n",i,count1);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",i);
		}
	}
	return 0;
}