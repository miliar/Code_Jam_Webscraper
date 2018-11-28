#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>


void main()
{
int cases,index_cases,i,r,t,paint,n;

freopen("A-small-attempt0.in" , "rt" , stdin ) ;
freopen("A-small-attempt0.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&r);
	scanf("%d",&t);

	for (n=1;;n++)
	{
			paint = n * ((2*(n+r))-1);
			if (paint > t) break;
	}


	printf("Case #%d: %d\n",index_cases+1, n-1);
}
fclose(stdin) ;
fclose(stdout) ;

}