#include "stdio.h"


int main()
{
	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	for(int I=1; I<=N; ++I)
	{
		int n, m;
		int lawn[100][100];
		int i, j, k;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;++i)
		{
			for(j=0; j<m;++j)
				scanf("%d",&lawn[i][j]);
		}
		bool possible = true;

		for(i=0;i<n && possible;++i)
		{
			// get min,max
			int rmin = lawn[i][0], rmax = lawn[i][0];
			for(j=1; j<m;++j)
			{
				if(rmin > lawn[i][j])
					rmin = lawn[i][j];
				if(rmax < lawn[i][j])
					rmax = lawn[i][j];
			}
			if( rmin == rmax )
				continue;
			for(j=0; j<m && possible; ++j)
			{
				if( lawn[i][j] < rmax )
				{
					for(k=0; k<n && possible; ++k)
					{
						if( lawn[k][j] > lawn[i][j] )
							possible = false;
					}
				}
			}
		}

		for(j=0;j<m && possible;++j)
		{
			// get min,max
			int rmin = lawn[0][j], rmax = lawn[0][j];
			for(i=1; i<n;++i)
			{
				if(rmin > lawn[i][j])
					rmin = lawn[i][j];
				if(rmax < lawn[i][j])
					rmax = lawn[i][j];
			}
			if( rmin == rmax )
				continue;
			for(i=0; i<n && possible; ++i)
			{
				if( lawn[i][j] < rmax )
				{
					for(k=0; k<m && possible; ++k)
					{
						if( lawn[i][k] > lawn[i][j] )
							possible = false;
					}
				}
			}
		}

		printf("Case #%d:", I);
		if( possible )
			printf(" YES");
		else
			printf(" NO");

		printf("\n");
	}
	return 0;
}

