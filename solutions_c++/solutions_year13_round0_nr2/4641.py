// google2013_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include "stdlib.h"
#include "memory.h"


int a[101][101];
int b[101][101];

int _tmain(int argc, _TCHAR* argv[])
{
	int cas, t = 0;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	while(cas--)
	{
		t++;
		int n, m;
		scanf("%d%d",&n,&m);
		int i,j;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));

		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		
		for(i=0; i<n; i++)
		{
			int mx = 0;
			for(j=0; j<m; j++)
			{
				if(a[i][j] > mx)
					mx = a[i][j];
			}
			for(j=0; j<m; j++)
			{
				if(a[i][j] == mx)
					b[i][j] = 1;
			}
		}

		for(j=0; j<m; j++)
		{
			int mx = 0;
			for(i=0; i<n; i++)
			{
				if(a[i][j] > mx)
					mx = a[i][j];
			}
			for(i=0; i<n; i++)
			{
				if(a[i][j] == mx)
					b[i][j] = 1;
			}
		}

		bool fail = false;
		for(i=0; i<n; i++)
		{
			int mx = 0;
			for(j=0; j<m; j++)
			{
				if(b[i][j] == 0)
					fail = true;
			}
		}
		if(fail == false)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);
	}
	return 0;
}

