#include<stdio.h>

int main()
{
	 double C,F,X,j,k,l,m,count;
	 int counter=1,i;
	 scanf("%d",&i);
	 while(i!=0)
	 {
	 	count=0,k=2;
	 	scanf("%lf",&C);
	 	scanf("%lf",&F);
	 	scanf("%lf",&X);
	 	
	 	m=X/k;
	 	l=(C/k) + (X/(k+F));
	 	while(l<m)
	 	{
	 		count=count + (C/k);
	 		k=k+F;
	 		m=X/k;
	 		l=(C/k) + (X/(k+F));
	 	}
	 	count=count+m;
	 	
	 	printf("case #%d: %.7lf\n",counter,count);
	 	
	 	counter++;
	    i--;
	 }
	 
	 return 0;
	 
}
