#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int cases, index_cases;
int i,N,m[1000],minrate, dif;
double min, min2;


void main()
{

//freopen("A-small-attempt0.in" , "rt" , stdin ) ;
//freopen("A-small-attempt0.out" , "wt" , stdout ) ;
freopen("A-large.in" , "rt" , stdin ) ;
freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{

	min = 0;
	min2 = 0;
	minrate=0;
	scanf("%d",&N);
	for (i=0;i<N;i++)
	{
		scanf("%d",&m[i]);
	}
	for (i=1;i<N;i++)
	{
		dif = m[i-1]-m[i];
		if (dif>0)
		{
			min = min+dif ;
			if (dif>minrate) minrate = dif;
		}
	}
//	printf("min %g, minrate %d \n",min,minrate);
	for (i=1;i<N;i++)
	{
		if (m[i-1]>minrate)	min2 = min2+minrate ;
		else min2 = min2 + m[i-1];
	}
	

	printf("Case #%d: %.0f %.0f\n",index_cases+1,min, min2);
}
fclose(stdin) ;
fclose(stdout) ;

}