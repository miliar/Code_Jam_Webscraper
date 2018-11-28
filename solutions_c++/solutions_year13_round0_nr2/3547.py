#include <stdio.h>     
#include <iostream>
#include <string.h>     
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>
#include <fstream>
#include <sstream>
#pragma comment(linker, "/STACK:327772160")
using namespace std;
int Map[110][110];
int l , r;
bool check(int n)
{
	for ( int i = 0; i < l; i ++)
	{
		for ( int j = 0 ; j < r; j ++)
		{
			if (Map[i][j]==n)
			{
				int Count = 0;
				for ( int k = 0; k < r;k ++)
				{
					if (Map[i][k] > Map[i][j])
						Count++;
				}
				
				if ( Count > 0)
				{
				Count = 0;
				for ( int k = 0; k < l;k ++)
				{
					if (Map[k][j] > Map[i][j])
						Count++;
				}
				
				if ( Count >0)
					return false;
				}

			}
		}
	}
	return true;
}
int main()
{
	//#ifndef _DEBUG
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
//#endif
	int T;
	int C;
	scanf("%d",&T);
	for ( int k = 1 ; k <= T; k++)
	{
		
		scanf("%d%d",&l,&r);
		int Max = -1;
		for ( int i = 0 ; i < l ; i ++)
		{
			for ( int j = 0; j < r; j ++)
			{
				scanf("%d",&Map[i][j]);
				if ( Map[i][j] > Max)
				{
					Max = Map[i][j];
				}
			}
		}
		bool ans = true;
		for ( int i = Max - 1; i >=1; i --)
		{
			if ( !check(i))
			{
				ans = false;
				break;
			}
		}
		if ( ans)
		{
			printf("Case #%d: YES\n",k);
		}
		else
		{
			printf("Case #%d: NO\n",k);
		}
	}
	return 0;	
}