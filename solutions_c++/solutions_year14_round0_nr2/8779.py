#include<stdio.h>
int main()
{
	int len,i=0,flag;
	double c,f,x,t,t1,t2,r=2;
	scanf("%d",&len);
	for(i=0;i<len;i++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
	t1=0;
	flag=1;
	r=2;
	t=x/r;
	t2=0;
	//printf("%f",t[i]);
	while(t>t1)
	{
	t2+=c/r;
	t1=t2+(x/(r+f));
	if(t1<t)
	{
	r=r+f;
	t=t1;
	t1=t2+c/r+(x/(r+f));
    }   
    
}
    
    
    	printf("Case #%d: %.7lf\n",i+1,t);
    }
   /* for(i=0;i<len;i++)
	{
		printf("Case #%d: %d",i+1,t[i]);
	}*/
return (0);	
	
}
