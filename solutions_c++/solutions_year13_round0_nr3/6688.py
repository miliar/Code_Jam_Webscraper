#include<stdio.h>
#include <math.h>

int palin(int);
int main()
{
	
	int t, c, a, b, i, y, j;
	
	scanf("%d",&t);
	
	 c=1;
	 
	while(t>0)
	{
	   y=0;
	   
     scanf("%d",&a);
     
     scanf("%d",&b);
     
     for(i=a; i<=b; i++)
     {
			if(palin(i))
			{
				j= sqrt(i);
				
				if(j*j==i)
				if(palin(j))
				y++;
			}
		
	 }


     printf("Case #%d: %d\n",c,y);

     c++;
     t--;
	}
	
	
	
	return 0;
	
}

int palin(int a)
{
	int n = a, r, x=0;
	
	while(n)
	{
	r=n%10;
	x=x*10 +r;
	n/=10;	
	}
	
	if(x==a)
	return 1;
	else
	return 0;
	
}
