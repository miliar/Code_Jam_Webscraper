#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>


void main()
{
int X,R,C, fitcells, winner;
int cases,index_cases;
freopen("D-small-attempt0.in" , "rt" , stdin ) ;
freopen("D-small-attempt0.out" , "wt" , stdout ) ;
//freopen("D-large.in" , "rt" , stdin ) ;
//freopen("D-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&X);
	scanf("%d",&R);
	scanf("%d",&C);
	fitcells = (R*C)%X;
//	printf("fitcells = %d\n",fitcells);
	if((((R>=X)&&(C>=X-1))||
	    ((R>=X-1)&&(C>=X)))     &&
	   (X<7)					&&
	   (fitcells ==0)
	  )
		winner=0;
	else winner=1;
	printf("Case #%d: ",index_cases+1);
	if (winner) printf("RICHARD\n");
	else printf("GABRIEL\n");
	
}
//fclose(stdin) ;
//fclose(stdout) ;
}