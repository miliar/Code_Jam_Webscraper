#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#define max 105
typedef enum Status_code{FAILURE,SUCCESS}sc;
sc cp(int n)
{
   int reverse = 0,temp;
   sc S=FAILURE;
   temp = n;
 
   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }
 
   if ( n == reverse )
      S=SUCCESS; 
   return S;
}
int main()
{
#ifndef Pratik
	freopen("input.in","rt",stdin);
	freopen("output.out", "wt",stdout);
#endif
	int t,i,j,l=0,q,count=0,m,a[max];
	float sqt;
	sc S=FAILURE;
	sc S1=FAILURE;
	scanf("%d",&t);
	while(l<t)
	{
		count=0;
		scanf("%d%d",&i,&j);
		for(q=i;q<=j;q++)
		{
			//printf("q=%d",q);
			S=cp(q);
			if(S==SUCCESS)
			{
				sqt=sqrt(q);
				m=sqt;
				if(sqt==m)
				{
					S1=cp(sqt);
					if(S1==SUCCESS)
					count++;
				//	printf("in for looop \ncount=%d\n",count);
				}
			}
		}
		a[l]=count;
		//printf("in while loop\n %d\n",count);
		l++;
	}
	for(l=0;l<t;l++)
	{
		printf("Case #%d: %d\n",l+1,a[l]);
	}
	
	return 0;
}
