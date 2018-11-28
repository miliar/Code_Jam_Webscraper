#include<stdio.h>

int main()
{
 unsigned long long count;
 long T,A,B,K,i,j,cas;
 
 scanf("%ld",&T);
 
 cas=1;
 
 while(T--)
 {
 scanf("%ld%ld%ld",&A,&B,&K);
 
 count=0;
 
 for(i=0;i<A;i++)
 {for(j=0;j<B;j++)
	{ if((i&j)<K)
	  {count++;}
	}
 }
 printf("Case #%ld: %u\n",cas,count);
 cas++;
 }
 return 0;
 
}