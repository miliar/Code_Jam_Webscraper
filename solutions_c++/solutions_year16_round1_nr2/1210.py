#include<bits/stdc++.h>

bool par[2550];

int main()
{
	int nt;
	scanf(" %d",&nt);
	for(int t=1; t<=nt; t++)
	{
		int n,m=0;
		memset(par,0,sizeof(par));
		scanf(" %d",&n);
		for(int i=1; i<2*n; i++)
			for(int j=0; j<n; j++)
			{
				int a;
				scanf(" %d",&a);
				par[a] = not par[a];
				if(a>m) m = a;
			}
		printf("Case #%d:",t);
		for(int i=0; i<=m; i++)
			if(par[i])
				printf(" %d",i);
		printf("\n");
	}
	return 0;
}
	
