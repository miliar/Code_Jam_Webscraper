#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>



void main()
{
int cases,index_cases,N,M,i,j;
int lawn[100][100];
int maxr[100],maxc[100];
int possible;

//freopen("B-small-attempt0.in" , "rt" , stdin ) ;
//freopen("B-small-attempt0.out" , "wt" , stdout ) ;
freopen("B-large.in" , "rt" , stdin ) ;
freopen("B-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	possible=1;
	scanf("%d",&N);
	scanf("%d",&M);
//	printf("N = %d, M=%d\n",N,M);
	memset(&maxc,0,sizeof(maxc));
	memset(&maxr,0,sizeof(maxr));
	for (i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
		{
			scanf("%d",&lawn[i][j]);

			if (lawn[i][j]>maxr[i]) maxr[i] = lawn[i][j];
			if (lawn[i][j]>maxc[j]) maxc[j] = lawn[i][j];
		}
	
	}

	for (i=0;(possible) && (i<N);i++)
	{
		for(j=0;(j<M)&&(possible);j++)
		{
			if((lawn[i][j]!= maxr[i])&&(lawn[i][j]!= maxc[j]))possible = 0;
		}
	
	}



/*	for (i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
		{
			printf("%d",lawn[i][j]);
		}
		printf("- Max= %d\n", maxr[i] );
	}
	for(j=0;j<M;j++)
	{
		printf("%d",maxc[j]);
	}
	printf("\n");
*/
	printf("Case #%d: ",index_cases+1);
	if (possible) printf("YES\n");
	else printf("NO\n");
}
//fclose(stdin) ;
//fclose(stdout) ;
}