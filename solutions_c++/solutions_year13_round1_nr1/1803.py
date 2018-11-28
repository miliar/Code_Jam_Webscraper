#include <stdio.h>

int main()
{
	int L,m,n,r,t,testcase;
	scanf("%d",&testcase);
	for (m=1;m<=testcase;m++)
	{
		n=0;
    	scanf("%d %d",&r,&t);
    	L=0;
    	while(1)
    	{
			L=L+(r+1)*(r+1)-r*r;
			if (L>t) break;
			r+=2;
			n+=1;
		}
		printf("Case #%d: %d\n",m,n);
	}
	return 0;
}
    
            
