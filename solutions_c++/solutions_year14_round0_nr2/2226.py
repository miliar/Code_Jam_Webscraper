#include<stdio.h>
int main()
{
	int i,t,p;
	scanf("%d",&t);
	for(p=1;p<=t;p++) {
		double c,x,f,t,t1,t2,can;
		scanf("%lf%lf%lf",&c,&f,&x);
		can=2.0;
		t=0;
		while(1)
		{
			
			t1=x/can;
			t2=c/can+(x/(can+f));
			if(t1<t2)
			{
				t=t+t1;
				break;
			}
			else
			{
				t=t+c/can;
				can=can+f;
			}
		}
		printf("Case #%d: %.7lf\n",p,t);
	}
return 0;
}
