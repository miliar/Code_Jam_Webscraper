#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

double seconds (double a, double b, float c, float d, float x)
{
double direct, nextfarm, faster;

direct = x/b;
nextfarm = c/b;
faster = x/(b+d);
if (direct < (nextfarm + faster))
 return (a + direct);
else return seconds (a+nextfarm,b+d,c,d,x);
}
void main()
{
int cases,index_cases;
float C,F,X;
double time;
int i;

freopen("B-small-attempt0.in" , "rt" , stdin ) ;
freopen("B-small-attempt0.out" , "wt" , stdout ) ;
//freopen("C-large.in" , "rt" , stdin ) ;
//freopen("C-large.out" , "wt" , stdout ) ;


cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);
//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%f",&C);
	scanf("%f",&F);
	scanf("%f",&X);

	time = seconds(0,2,C,F,X);

	printf("Case #%d: %.7f\n",index_cases+1,time);


}
fclose(stdin) ;
fclose(stdout) ;
}