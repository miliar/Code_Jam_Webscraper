/*
 * lawnmower.cpp
 *
 *  Created on: Apr 14, 2013
 *      Author: stephenfebrian
 */

#include <cstdio>
#include <cstring>
#include <string>

int mat[101][101];
int y,x;

int checkHor(int yy, int xx, int numYX)
{
	int res = 0;
	//go right
	for(int i=xx;i<x;i++)
	{
		if(mat[yy][i] > numYX)
		{
			res = 1;
			break;
		}
	}
	if(res == 1) return res;

	//go left
	for(int i=xx;i>=0;i--)
	{
		if(mat[yy][i] > numYX)
		{
			res = 1;
			break;
		}
	}
	return res;
}

int checkVer(int yy, int xx, int numYX)
{
	int res = 0;
	//go down
	for(int i=yy;i<y;i++)
	{
		if(mat[i][xx] > numYX)
		{
			res = 1;
			break;
		}
	}
	if(res == 1) return res;

	//go left
	for(int i=yy;i>=0;i--)
	{
		if(mat[i][xx] > numYX)
		{
			res = 1;
			break;
		}
	}
	return res;
}

int checkMat(int yy, int xx)
{
	int numYX = mat[yy][xx];
	int res1 = checkHor(yy,xx,numYX);
	int res2 = checkVer(yy,xx,numYX);
	if(res1 == 1 && res2 == 1)
	{
		return 1;
	}
	return 0;
}

int main()
{
	freopen("lawnmower.in","r",stdin);
	freopen("lawnmower.out","w",stdout);
	int cases;
	int retCase = 0;
	scanf("%d",&cases);
	for(int i=0;i<cases;i++)
	{
		scanf("%d %d",&y,&x);
		for(int j=0;j<y;j++)
			for(int k=0;k<x;k++)
				scanf("%d",&mat[j][k]);
		retCase = 0;
		for(int j=0;j<y;j++)
		{
			for(int k=0;k<x;k++)
			{
				int res = checkMat(j,k);
				if(res == 1)
				{
					retCase = 1;
					break;
				}
			}
			if(retCase == 1) break;
		}
		if(retCase == 1)
		{
			printf("Case #%d: NO\n",i+1);
		}
		else
		{
			printf("Case #%d: YES\n",i+1);
		}
	}
	fclose(stdout);
}



