#include <stdio.h>
#include <string.h>


int lmax[101],rmax[101];
int N,M;
int h[101][101];

int can()
{
	int i,j;
	for ( i=0;i<N;++i )
	{
		for ( j=0;j<M;++j )
		{
			if ( h[i][j] < lmax[i] && h[i][j] < rmax[j] )
				return 0;
		}
	}
	return 1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,st,i,j;
	scanf("%d",&st);
	for ( t=1;t<=st;++t )
	{
		scanf("%d%d",&N,&M);

		memset( lmax,0,sizeof(lmax) );
		memset( rmax,0,sizeof(rmax) );
		for ( i=0;i<N;++i )
		{
			for (j=0;j<M;++j )
			{
				scanf("%d",&h[i][j]);
				if ( h[i][j] > lmax[i] ) lmax[i] = h[i][j];
				if ( h[i][j] > rmax[j] ) rmax[j] = h[i][j];
			}
		}
		printf("Case #%d: %s\n",t,can()?"YES":"NO");
	}
	return 0;
}