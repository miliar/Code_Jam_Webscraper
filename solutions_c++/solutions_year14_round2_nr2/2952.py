#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define REP(i,a,b)\
		for(int i = int(a); i<int(b);i++)		


int main()
{
 	int a,b,x,cont,n,i,j;
	scanf("%d",&n);
	REP(k,1,n+1){
 	scanf("%d %d %d",&a,&b,&x);
      cont=0;
		for(i=0;i<a;i++)
		{
		   for(j=0;j<b;j++)
		   {
		      if((i&j)<x) cont++;
		   }
		}
      printf("Case #%d: %d\n",k,cont);
	}

 	
 	return 0;
}
