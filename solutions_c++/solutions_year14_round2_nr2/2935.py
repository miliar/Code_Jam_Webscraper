#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

using namespace std;

int main()
{

int T=0,Tcount=1;
scanf("%d\n",&T);
long A,B,K;
long AI=0,BI=0;
double count=0;

for(Tcount=1;Tcount<=T;Tcount++)
{

	scanf("%ld %ld %ld\n",&A,&B,&K);	
	count=0;
		
	for(BI=0;BI<B;BI++)
	{
		for(AI=0;AI<A;AI++)
		{
		if((AI&BI)<K) 
		{	count++;
			//printf("%ld %ld\n",AI,BI);
		}
		}
	}
	
	
	printf("Case #%d: %.0lf\n",Tcount,count);
}


return 0;
}
