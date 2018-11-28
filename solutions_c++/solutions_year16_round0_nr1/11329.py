#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int cases, index_cases;
int i,N,seen,current,x;

int rgvp(int a,int b)
{
int q,p;
if(b>0)
{
	for (q=0, p=1;q<b;q++)
	{
		p=p*a;
	}
	return (p);
}
else return(1);
}

int digits(int a)
{
	int i,aux, dig,currdig;
	for(aux = a,i=1, dig=0;aux>0;aux=aux/10)
	{
		currdig = aux%10;
		dig = dig | rgvp(2,currdig);
	}
return (dig);
}

void main()
{

freopen("A-small-attempt0.in" , "rt" , stdin ) ;
freopen("A-small-attempt0.out" , "wt" , stdout ) ;
//freopen("A-large.in" , "rt" , stdin ) ;
//freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);

//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&N);
	printf("Case #%d: ",index_cases+1);
	seen = 0;
	if (N!=0)
	{
		for (i=1;;i++)
		{
			current = i * N;
			x=digits(current);
			seen = seen|x;
			if(seen>=1023) break;
		}
		printf("%d\n",current);
	}
	else
	{
		printf("INSOMNIA\n");
	}
}
fclose(stdin) ;
fclose(stdout) ;

}