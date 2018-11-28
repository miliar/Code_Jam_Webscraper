#include <stdio.h> 

int main ()
{
	int n1,n2,m1,m2;
	double c,f,x,time,time1,time2; 
	scanf("%d",&n1);
	n2=1;
	while (n2<=n1)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		time=x/c-2.0/f-f/f;
		m1=time;
		time2=0;
	    for(m2=0;m2<m1;m2++)
	        time2=time2+c/(m2*f+2.0);
	    time=time2+x/(m2*f+2.0);
	    time1=time2+c/(m2*f+2.0)+x/(m2*f+f+2.0);
	    if(time1-time<0.0000001)
	        	time=time1;
	    printf("Case #%d: %.7f\n",n2,time);
		n2++;
	}
	return 0;
}
