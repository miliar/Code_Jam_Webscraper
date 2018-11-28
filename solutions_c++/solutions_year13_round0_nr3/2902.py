#include <stdio.h>

const int MAXT = 100;
int T;
int START,LAST;

unsigned int n0;


int assertPalindrome()
{

 if( n0 < 10 )
 	return 1;
 if( n0 < 100)
	return (n0%10==n0/10);
 if( n0 < 1000)
	return (n0/100==n0%10);
	
	return 0;
	
}
int sol()
{

	int l0,l1,r0;
	r0=n0=0;
	
	for(l0=1; l0<=1000; l0++)
 	 {
		
		n0=l0;
		if(assertPalindrome())
		{
		n0=l0*l0;
		if( n0 >= START && n0 <=LAST)
		{	
		if(assertPalindrome())
			{			
//			printf("%d ",n0);
			r0++;			 	
			}
		}
		}
	 }

	return r0;

}

int main()
{

	int l0,l1,l2;
	
	freopen("./input","r",stdin);

	scanf("%d",&T);
	for(l0 = 1; l0 <= T; l0++)
	{
	scanf("%d %d",&START,&LAST);
	printf("Case #%d: %d\n",l0,sol());
	}


}

