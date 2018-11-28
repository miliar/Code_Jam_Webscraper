/*************************************************************************
    > File Name: b.cpp
    > Author: withwind
    > Mail: withwind93@gmail.com 
    > Created Time: 2013/4/13 10:10:56
 ************************************************************************/
#include <limits.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
using namespace std;
int a[110][110];
int n,m,flag;
void check(int x,int y)
{
	int bo = 0;
	int i,j;
	for(i=1;i<=n;i++)
	{
		if(a[i][y] > a[x][y])	break;	
	}
	if(i == n+1)	bo=1;	
	/***/
	for(i=1;i<=m;i++)
	{
		if(a[x][i] > a[x][y])	break;	
	}
	if(i == m+1)	bo=1;

	flag = bo;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k;
	int t;
	scanf("%d",&t);
	for(int casen=1;casen<=t;casen++)
	{
		int count = 0;
		scanf("%d %d",&n,&m);
		for(i = 1;i<=n;i++)
		  for(j=1;j<=m;j++)
		  {
			scanf("%d",&a[i][j]);		
		  }
		flag = 1;

		for(i = 1;i<=n;i++)
		{
		  for(j=1;j<=m;j++)
		  {
			 check(i,j);
			if(flag == 0)
			{
			//	printf("i = %d %d\n",i,j);
				break;
			}
		  }
		  if(flag == 0)	break;
		}
		printf("Case #%d: ",casen);
		if(flag)	printf("YES\n");
		else		printf("NO\n");
	}
	return 0;
}
