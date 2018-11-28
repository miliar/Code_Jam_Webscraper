#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int cases, index_cases;
int i,N,sum, friends;
char str[1001];


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



	scanf("%d",&N);
	scanf("%s",&str);
//	printf("str %d = %s, %d \n", index_cases, str, strlen(str));
	friends =0;
	sum=0;
	for (i=0;i<=N;i++)
	{
		if((( (str[i]-48)!=0)&&(sum <i)))
		{
			friends += i-sum;
			sum=i;
		}
		sum += str[i]-48;
//		printf("sum %d=%d, friends = %d\n",i,sum,friends);
	}
	printf("Case #%d: %d\n",index_cases+1,friends);
}
fclose(stdin) ;
fclose(stdout) ;

}